from __future__ import annotations

import datetime
import random
from typing import Optional
from mongoengine import *
from mongoengine import signals
from operator import itemgetter
import json
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Union
from urllib.parse import quote_plus as quote

from bson import DBRef, ObjectId, dbref
from pymongo.cursor import Cursor
from pymongo.command_cursor import CommandCursor

from mongoengine import connect


if TYPE_CHECKING:

    from ..confighelper import ConfigHelper
    from ..websockets import WebRequest

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, DBRef):
            return o.as_doc()
        if isinstance(o, Cursor):
            return list(o)
        if isinstance(o, CommandCursor):
            return list(o)
        if isinstance(o, datetime):
            return o.timestamp()
        if isinstance(o, ListableDocument):
            d = o.select_related()
            return {k: v for k, v in d._data.items() if v is not None}
        if isinstance(o, EmbeddedDocument):
            f = o._fields_ordered
            return {k: getattr(o, k) for k in f if getattr(o, k) is not None}
        if isinstance(o, bytes):
            return o.decode()
        return json.JSONEncoder.default(self, o)

class JSONDecoder(json.JSONDecoder):
    def decode(self, s: str):
        s = s.replace("\"_id\":", "\"id\":").replace("\"_cls\":", "\"cls\":")
        return json.JSONDecoder.decode(self, s)

def parse_json(data):
    return json.loads(JSONEncoder().encode(data), cls=JSONDecoder)

def handler(event):
    """Signal decorator to allow use of callback functions as class decorators."""
    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls

        fn.apply = apply
        return fn

    return decorator


@handler(signals.pre_save)
def update_date_tracking(sender, document):
    document.update_date = datetime.utcnow()


class ListQuerySet(QuerySet):
    def get_items(self, search: Optional[str] = None, sort_by: str = 'id', sort_desc: bool = False, skip: int = 0, limit: int = 10, **kwargs):
        query = self.order_by(
            f"{'-' if sort_desc else '+'}{sort_by}")[skip:limit]
        if search is not None:
            query = query.search_text(search)
        return query.count(), [i for i in query]

    def get_item(self, id: str):
        return self.get(id=id)


class ItemFrequenciesQuerySet(ListQuerySet):
    def get_field_frequencies(self, field: str,  search: Optional[str] = None, sort_desc: bool = True, skip: int = 0, limit: int = 100, **kwargs):
        frqus = self.item_frequencies(field)
        if search is not None and len(search) > 0:
            frqus = {k: v for k, v in frqus.items() if search in str(k)}
        frqus_list = sorted(frqus.items(), key=itemgetter(1),
                            reverse=sort_desc)[skip:limit]
        return len(frqus_list), [{'id': kv[0], 'count': kv[1]} for kv in frqus_list]


class ListableDocument(Document):
    meta = {'allow_inheritance': True, 'queryset_class': ListQuerySet, 'abstract': True}
    creation_date = DateTimeField(default=datetime.utcnow())
    update_date = DateTimeField()

    @queryset_manager
    def get_items(doc_cls, queryset: QuerySet, search: Optional[str] = None, sort_by: str = 'id', sort_desc: bool = False, skip: int = 0, limit: int = 100, **kwargs):
        return queryset.get_items(search, sort_by, sort_desc, skip, limit, **kwargs)

    @queryset_manager
    def get_item(doc_cls, queryset: QuerySet, id: str):
        return queryset.get_item(id)

class RoleEntity(EmbeddedDocument):
    name = StringField(required=True)
    id = ObjectIdField(required=True)

@update_date_tracking.apply
class Role(ListableDocument):
    meta = {'queryset_class': ItemFrequenciesQuerySet, 'collection': 'roles'}

    entity = EmbeddedDocumentField(RoleEntity)
    name = StringField(required=True)
    scopes = ListField(StringField())

    @queryset_manager
    def get_scopes(doc_cls, queryset: QuerySet, search: Optional[str] = None, sort_desc: bool = True, skip: int = 0, limit: int = 100, **kwargs):
        return queryset.get_field_frequencies(
            'scopes', search, sort_desc, skip, limit, **kwargs)

@update_date_tracking.apply
class UserSettings(ListableDocument):
    meta = {'collection': 'user_settings'}
    settings = DictField()
    user_id = StringField(required=True)



"""Stores public user info"""
@update_date_tracking.apply
class User(ListableDocument):
    meta = {'collection': 'users'}

    email = EmailField(required=True, unique=True)
    username = StringField(min_length=1, max_length=50)
    avatar = URLField()
    role = ReferenceField(Role, reverse_delete_rule=DENY)
    verified = BooleanField(default=False)

    @queryset_manager
    def get_user(doc_cls, queryset: ListQuerySet, id: str):
        return queryset.get_item(id)

class MongoDatabase:
    def __init__(self, config: ConfigHelper) -> None:
        self.server = config.get_server()
        self.database_path = config.get(
            'database_path', 'localhost'
        )
        self.database_port: int = config.getint(
            'database_port', 49153
        )
        self.database_name = config.get(
            'database_name', 'stereotech_cloud'
        )
        self.user = config.get(
            'user_name', ''
        )
        self.pw = config.get(
            'password', ''
        )
        self.rs = config.get(
            'rs', ''
        )
        self.auth_src = config.get(
            'auth_src', ''
        )
        self.tlsCAFile = config.get(
            'tlscafile', ''
        )

        url = f'mongodb://{quote(self.user)}:{quote(self.pw)}@{self.database_path}:{self.database_port}/{self.database_name}?tls=true&tlsCAFile={self.tlsCAFile}&replicaSet={self.rs}&authMechanism=DEFAULT&authSource={self.auth_src}'
        connect(host=url)


def load_component(config: ConfigHelper) -> MongoDatabase:
    return MongoDatabase(config)
