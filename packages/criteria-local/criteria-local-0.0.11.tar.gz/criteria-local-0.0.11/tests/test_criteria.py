""" Imposr sys"""
import sys
import os
from circles_local_database_python.generic_crud import GenericCRUD
import pytest
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from logger_local.Logger import Logger
from dotenv import load_dotenv
script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_directory, '..'))
from src.criteria import (
    DEVELOPER_EMAIL, CRITERIA_LOCAL_PYTHON_COMPONENT_ID,
    CRITERIA_LOCAL_PYTHON_COMPONENT_NAME, CriteriaLocal)


object_init = {
    'component_id': CRITERIA_LOCAL_PYTHON_COMPONENT_ID,
    'component_name': CRITERIA_LOCAL_PYTHON_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Unit_Test.value,
    'testing_framework': LoggerComponentEnum.testingFramework.pytest.value,
    "developer_email": DEVELOPER_EMAIL
}

TEST_SCHEMA = 'criteria'
TEST_VIEW = 'criteria_view'
ID_COLUMN = 'criteria_id'
ID_COLUMN_VALUE = CriteriaLocal().get_test_id(1, 1, 1, 1)

logger = Logger.create_logger(object=object_init)

load_dotenv()


def test_delete_criteria() -> None:
    """
    Test the deletion of a criterion and verify the change in the database.

    This function deletes a criterion using the `CriteriaLocal` class and then checks
    if the "end_timestamp" value has changed in the database, indicating that the
    criterion has been deleted. It uses the `GenericCRUD` class to perform the
    database operations.

    :rtype: None
    """
    logger.start("START TEST")
    before = GenericCRUD(schema_name=TEST_SCHEMA).select_one_tuple_by_id(
        view_table_name=TEST_VIEW, select_clause_value="end_timestamp",
        id_column_name=ID_COLUMN, id_column_value=ID_COLUMN_VALUE)
    CriteriaLocal().delete(ID_COLUMN_VALUE)
    after = GenericCRUD(schema_name=TEST_SCHEMA).select_one_tuple_by_id(
        view_table_name=TEST_VIEW, select_clause_value="end_timestamp",
        id_column_name=ID_COLUMN, id_column_value=ID_COLUMN_VALUE)
    assert before != after
    logger.end()
