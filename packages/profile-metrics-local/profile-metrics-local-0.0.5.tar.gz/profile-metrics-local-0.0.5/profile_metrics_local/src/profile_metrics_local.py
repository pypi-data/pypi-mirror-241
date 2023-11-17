from typing import Dict
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from dotenv import load_dotenv

load_dotenv()
from circles_local_database_python.generic_crud import GenericCRUD   # noqa: E402
from logger_local.Logger import Logger  # noqa: E402

PROFILE_METRICS_LOCAL_COMPONENT_ID = 233
PROFILE_METRICS_LOCAL_COMPONENT_NAME = "profile metrics local"
DEVELOPER_EMAIL = "tal.g@circ.zone"
object_for_logger_code = {
    'component_id': PROFILE_METRICS_LOCAL_COMPONENT_ID,
    'component_name': PROFILE_METRICS_LOCAL_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}
logger = Logger.create_logger(object=object_for_logger_code)

SCHEMA_NAME = "profile_metrics"
TABLE_NAME = "profile_metrics_table"
VIEW_NAME = "profile_metrics_view"
DEFAULT_ID_COLUMN_NAME = "profile_metrics_id"


class ProfileMetricsLocal(GenericCRUD):

    @staticmethod
    def insert(profile_id: int, profile_metrics_type: int, value: int) -> int:
        logger.start(object={'profile_id': profile_id, 'profile_metrics_type': profile_metrics_type, 'value': value})
        generic_crud = GenericCRUD(schema_name=SCHEMA_NAME, default_table_name=TABLE_NAME,
                                   default_id_column_name=DEFAULT_ID_COLUMN_NAME)
        profile_metrics_id = generic_crud.insert(
            table_name=None,
            json_data={'profile_id': profile_id, 'profile_metrics_type': profile_metrics_type, 'value': value})
        logger.end(object={'profile_metrics_id': profile_metrics_id})
        return profile_metrics_id

    @staticmethod
    def update(profile_metrics_id: int, profile_id: int, profile_metrics_type: int, value: int) -> None:
        logger.start(object={'profile_metrics_id': profile_metrics_id, 'profile_id': profile_id,
                     'profile_metrics_type': profile_metrics_type, 'value': value})
        json_data = {'profile_id': profile_id, 'profile_metrics_type': profile_metrics_type, 'value': value}
        generic_crud = GenericCRUD(schema_name=SCHEMA_NAME, default_table_name=TABLE_NAME,
                                   default_id_column_name=DEFAULT_ID_COLUMN_NAME)
        profile_metrics_id = generic_crud.update_by_id(
            table_name=None, id_column_name=DEFAULT_ID_COLUMN_NAME, id_column_value=profile_metrics_id,
            json_data=json_data)
        logger.end()

    @staticmethod
    def delete(profile_metrics_id: int) -> None:
        logger.start(object={'profile_metrics_id': profile_metrics_id})
        generic_crud = GenericCRUD(schema_name=SCHEMA_NAME, default_table_name=TABLE_NAME,
                                   default_id_column_name=DEFAULT_ID_COLUMN_NAME)
        generic_crud.delete_by_id(table_name=TABLE_NAME, id_column_name=DEFAULT_ID_COLUMN_NAME,
                                  id_column_value=profile_metrics_id)
        logger.end()

    @staticmethod
    def select_one_dict_by_id(profile_metrics_id: int) -> Dict[str, int]:
        logger.start(object={'profile_metrics_id': profile_metrics_id})
        select_clause_value = 'profile_id, profile_metrics_type, value'
        generic_crud = GenericCRUD(schema_name=SCHEMA_NAME, default_table_name=VIEW_NAME,
                                   default_id_column_name=DEFAULT_ID_COLUMN_NAME)
        profile_metrics_dict = generic_crud.select_one_dict_by_id(
            view_table_name=VIEW_NAME, select_clause_value=select_clause_value, id_column_name=None,
            id_column_value=profile_metrics_id)
        logger.end(object={'profile_metrics_dict': profile_metrics_dict})
        return profile_metrics_dict
