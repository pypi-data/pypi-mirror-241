from __future__ import annotations
import logging
import copy
from typing import TYPE_CHECKING, Any, Dict
from mongoengine import context_managers
from stereotech_cloud_commons.components.mongo_database import UserSettings

if TYPE_CHECKING:
    from stereotech_cloud_commons.confighelper import ConfigHelper
    from stereotech_cloud_commons.websockets import WebRequest
    from stereotech_cloud_commons.components.mongo_database import MongoDatabase

def merge_nested_dicts(d1, d2):
    for key, value in d2.items():
        if key in d1 and isinstance(d1[key], dict) and isinstance(value, dict):
            merge_nested_dicts(d1[key], value)
        else:
            d1[key] = value
    return d1

def merge_lists(list1, list2):
    return list1 + list2

def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key in set(dict1) | set(dict2):
        if key in dict1 and key in dict2:
            if isinstance(dict1[key], list) and isinstance(dict2[key], list):
                merged_dict[key] = merge_lists(dict1[key], dict2[key])
            elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                merged_dict[key] = merge_nested_dicts(copy.deepcopy(dict1[key]), dict2[key])
            else:
                merged_dict[key] = dict2[key]
        elif key in dict1:
            merged_dict[key] = copy.deepcopy(dict1[key])
        else:
            merged_dict[key] = copy.deepcopy(dict2[key])
    return merged_dict

class Settings:
    def __init__(self, config: ConfigHelper) -> None:
        """Service for managing user settings."""
        self.server = config.get_server()
        self.entity_name = config.get('entity_name', None)
        if self.entity_name is not None:
            self.context = context_managers.switch_collection(UserSettings, f'{self.entity_name}_user_settings')
        else:
            self.context = context_managers.switch_collection(UserSettings, 'user_settings')

        logging.info("Settings service loaded")

        self.server.register_endpoint("/settings", ["GET", "POST"],
                                      self.handle_manage_user_settings)

    async def handle_manage_user_settings(self, web_request: WebRequest) -> UserSettings:
        action = web_request.get_action()

        user = web_request.get_current_user()
        if user is None:
            raise self.server.error('User not provided')
        user_id = user.get('id', None)

        if action == "GET":
            try:
                with self.context as UserSettings:
                    user_settings = UserSettings.objects.get(user_id=user_id) # type: ignore
                    return user_settings
            except:
                return {}

        elif action == "POST":
            data: Dict[str, Any] = web_request.get_args()
            with self.context as UserSettings:
                try:
                    user_settings: UserSettings = UserSettings.objects.get(user_id=user_id)
                    user_settings.settings = merge_dicts(user_settings.settings, data)
                except:
                    user_settings = UserSettings(user_id=user_id, settings=data)
                user_settings.save()
                return user_settings


def load_component(config: ConfigHelper) -> Settings:
    return Settings(config)
