from typing import Dict
try:
    # Works when running the tests from this package
    from constants_profiles_local import *
except Exception as e:
    # Works when importing this module from another package
    from src.constants_profiles_local import *
from circles_local_database_python.generic_crud import GenericCRUD  # noqa: E402
from circles_local_database_python.connector import Connector  # noqa: E402
from logger_local.Logger import Logger  # noqa: E402
from circles_number_generator.number_generator import NumberGenerator  # noqa: E402
from dotenv import load_dotenv
load_dotenv()

logger = Logger.create_logger(object=OBJECT_TO_INSERT_CODE)


class ProfilesLocal(GenericCRUD):

    def __init__(self):
        super().__init__(schema_name="profile", default_id_column_name="profile_id")
        logger.start()
        logger.end()

    '''
    person_id: int,
    data: Dict[str, any] = {
        'profile_name': profile_name,
        'name_approved': name_approved,
        'lang_code': lang_code,
        'user_id': user_id,                             #Optional
        'is_main': is_main,                             #Optional
        'visibility_id': visibility_id,
        'is_approved': is_approved,
        'profile_type_id': profile_type_id, #Optional
        'preferred_lang_code': preferred_lang_code,     #Optional
        'experience_years_min': experience_years_min,   #Optional
        'main_phone_id': main_phone_id,                 #Optional
        'rip': rip,                                     #Optional
        'gender_id': gender_id,                         #Optional
        'stars': stars,
        'last_dialog_workflow_state_id': last_dialog_workflow_state_id
    },
    profile_id: int
    '''

    def insert(self, person_id: int, profile_dict: Dict[str, any]) -> int:
        logger.start(object={'data': str(profile_dict)})

        profile_table_json = {
            "`number`": NumberGenerator.get_random_number("profile", "profile_table", "`number`"),
            "user_id": profile_dict['user_id'],
            "person_id": person_id,
            "is_main": profile_dict['is_main'],
            "visibility_id": profile_dict['visibility_id'],
            "is_approved": profile_dict['is_approved'],
            "profile_type_id": profile_dict['profile_type_id'],
            "preferred_lang_code": profile_dict['preferred_lang_code'],
            "experience_years_min": profile_dict['experience_years_min'],
            "main_phone_id": profile_dict['main_phone_id'],
            "rip": profile_dict['rip'],
            "gender_id": profile_dict['gender_id'],
            "stars": profile_dict['stars'],
            "last_dialog_workflow_state_id": profile_dict['last_dialog_workflow_state_id']
        }

        super().insert("profile_table", profile_table_json)
        profile_id = self.cursor.lastrowid()
        profile_ml_table_json = {
            "profile_id": profile_id,
            "lang_code": profile_dict['lang_code'],
            "`name`": profile_dict['profile_name'],
            "name_approved": profile_dict['name_approved']
        }
        super().insert("profile_ml_table", profile_ml_table_json)

        logger.end(object={'profile_id': profile_id})
        return profile_id

    '''
    profile_id: int,
    data: Dict[str, any] = {
        'profile_name': profile_name,
        'name_approved': name_approved,
        'lang_code': lang_code,
        'user_id': user_id,                             #Optional
        'is_main': is_main,                             #Optional
        'visibility_id': visibility_id,
        'is_approved': is_approved,
        'profile_type_id': profile_type_id, #Optional
        'preferred_lang_code': preferred_lang_code,     #Optional
        'experience_years_min': experience_years_min,   #Optional
        'main_phone_id': main_phone_id,                 #Optional
        'rip': rip,                                     #Optional
        'gender_id': gender_id,                         #Optional
        'stars': stars,
        'last_dialog_workflow_state_id': last_dialog_workflow_state_id
    }
    person_id: int                                      #Optional
    '''

    def update(self, profile_id: int, profile_dict: Dict[str, any]) -> None:
        logger.start(object={'profile_id': profile_id,
                     'data': str(profile_dict)})
        profile_table_json = {
            "person_id": profile_dict['person_id'],
            "user_id": profile_dict['user_id'],
            "is_main": profile_dict['is_main'],
            "visibility_id": profile_dict['visibility_id'],
            "is_approved": profile_dict['is_approved'],
            "profile_type_id": profile_dict['profile_type_id'],
            "preferred_lang_code": profile_dict['preferred_lang_code'],
            "experience_years_min": profile_dict['experience_years_min'],
            "main_phone_id": profile_dict['main_phone_id'],
            "rip": profile_dict['rip'],
            "gender_id": profile_dict['gender_id'],
            "stars": profile_dict['stars'],
            "last_dialog_workflow_state_id": profile_dict['last_dialog_workflow_state_id']
        }
        super().update_by_id(table_name="profile_table", id_column_name="profile_id",
                             id_column_value=profile_id, data_json=profile_table_json)

        profile_ml_table_json = {
            "profile_id": profile_id,
            "lang_code": profile_dict['lang_code'],
            "`name`": profile_dict['profile_name'],
            "name_approved": profile_dict['name_approved']
        }
        super().update_by_id(table_name="profile_ml_table", id_column_name="profile_id",
                             id_column_value=profile_id, data_json=profile_ml_table_json)
        logger.end()

    # TODO develop get_profile_object_by_profile_id( self, profile_id: int ) -> Profile[]:
    def get_profile_dict_by_profile_id(self, profile_id: int) -> Dict[str, any]:
        logger.start(object={'profile_id': profile_id})
        profile_ml_dict = self.select_one_dict_by_id(
            view_table_name="profile_ml_view", id_column_value=profile_id)
        profile_dict = self.select_one_dict_by_id(
            view_table_name="profile_view", id_column_name="profile_id", id_column_value=profile_id)
        logger.end(object={'profile_ml_dict': str(
            profile_ml_dict), 'profile_view': str(profile_dict)})
        if not profile_ml_dict or not profile_dict:
            return {}
        return {**profile_ml_dict, **profile_dict}

    def delete_by_profile_id(self, profile_id: int):
        logger.start(object={'profile_id': profile_id})
        self.delete_by_id(table_name="profile_table",
                          id_column_value=profile_id)
        logger.end()
