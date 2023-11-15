""" import GENERICRUD"""
from circles_local_database_python.generic_crud import GenericCRUD
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from logger_local.Logger import Logger

CRITERIA_LOCAL_PYTHON_COMPONENT_ID = 210
CRITERIA_LOCAL_PYTHON_COMPONENT_NAME = 'criteria-local-python'
DEVELOPER_EMAIL = 'jenya.b@circ.zone'

object_init = {
    'component_id': CRITERIA_LOCAL_PYTHON_COMPONENT_ID,
    'component_name': CRITERIA_LOCAL_PYTHON_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    "developer_email": DEVELOPER_EMAIL
}

logger = Logger.create_logger(object=object_init)


class Criterion:
    """ Criterion class """

    def __init__(self, entity_type_id: int = None, group_list_id: int = None,
                 gender_list_id: int = None, location_id: int = None) -> None:
        """
        Initialize a Criterion object.

        :param entity_type_id: The entity type ID.
        :param group_list_id: The group list ID.
        :param gender_list_id: The gender list ID.
        :param location_id: The location ID.
        :type entity_type_id: int
        :type group_list_id: int
        :type gender_list_id: int
        :type location_id: int
        :rtype: None
        """
        self.entity_type_id = entity_type_id
        self.group_list_id = group_list_id
        self.gender_list_id = gender_list_id
        self.location_id = location_id


class CriteriaLocal(GenericCRUD):
    """
    CriteriaLocal class
    """

    def __init__(self) -> None:
        """
        Initialize the CriteriaLocal object.

        This class inherits from GenericCRUD.

        :rtype: None
        """
        super().__init__(schema_name="criteria")

    def insert_criteria(self, criterion: Criterion) -> None:
        """
        Insert a criterion into the database.

        :param criterion: The criterion to insert.
        :type criterion: Criterion
        :rtype: None
        """
        # TODO Can we use __str__ or other method?
        logger.start("Insert criteria", object={
            "entity_type_id": criterion.entity_type_id,
            "group_list_id": criterion.group_list_id,
            "gender_list_id": criterion.gender_list_id,
            "location_id": criterion.location_id
        })
        criteria_json = {
            "entity_type_id": criterion.entity_type_id,
            "group_list_id": criterion.group_list_id,
            "gender_list_id": criterion.gender_list_id,
            "location_id": criterion.location_id
        }
        GenericCRUD(schema_name="criteria").insert(
            table_name="criteria_table", json_data=criteria_json)
        logger.end()

    def update_min_age(self, criteria_id: int, min_age: float, kids: bool) -> None:
        """
        Update the minimum age for a criterion.

        :param criteria_id: The ID of the criterion to update.
        :param min_age: The new minimum age.
        :param kids: Whether the age is for kids.
        :type criteria_id: int
        :type min_age: float
        :type kids: bool
        :rtype: None
        """
        logger.start("Update minimum ages", object={
                     "criteria_id": criteria_id, "min_age": min_age})
        if kids:
            kids_age_json = {
                "min_kids_age": min_age,
            }
            self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                              id_column_value=criteria_id, json_data=kids_age_json)
            logger.end("Minimum kids ages update")
        else:
            age_json = {
                "min_age": min_age,
            }
            self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                              id_column_value=criteria_id, json_data=age_json)
            logger.end("Minimum ages update")

    def update_max_age(self, criteria_id: int, max_age: float, kids: bool) -> None:
        """
        Update the maximum age for a criterion.

        :param criteria_id: The ID of the criterion to update.
        :param max_age: The new maximum age.
        :param kids: Whether the age is for kids.
        :type criteria_id: int
        :type max_age: float
        :type kids: bool
        :rtype: None
        """
        logger.start("Update maximum ages", object={
                     "criteria_id": criteria_id, "max_age": max_age})
        if kids:
            kids_age_json = {
                "max_kids_age": max_age,
            }
            self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                              id_column_value=criteria_id, json_data=kids_age_json)
            logger.end("Maximum kids ages update")
        else:
            age_json = {
                "max_age": max_age,
            }
            self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                              id_column_value=criteria_id, json_data=age_json)
            logger.end("Maximum ages update")

    def update_min_number_of_kids(self, criteria_id: int, min_number_of_kids: int) -> None:
        """
        Update the minimum number of kids for a criterion.

        :param criteria_id: The ID of the criterion to update.
        :param min_number_of_kids: The new minimum number of kids.
        :type criteria_id: int
        :type min_number_of_kids: int
        :rtype: None
        """
        logger.start("Update minimum number of kids", object={
                     "criteria_id": criteria_id, "min_number_of_kids": min_number_of_kids})
        number_of_kids_json = {
            "min_number_of_kids": min_number_of_kids,
        }
        self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                          id_column_value=criteria_id, json_data=number_of_kids_json)
        logger.end()

    def update_max_age_number_of_kids(self, criteria_id: int, max_number_of_kids: int) -> None:
        """
        Update the maximum number of kids for a criterion.

        :param criteria_id: The ID of the criterion to update.
        :param max_number_of_kids: The new maximum number of kids.
        :type criteria_id: int
        :type max_number_of_kids: int
        :rtype: None
        """
        logger.start("Update maximum number of kids", object={
                     "criteria_id": criteria_id, "max_number_of_kids": max_number_of_kids})
        number_of_kids_json = {
            "max_number_of_kids": max_number_of_kids,
        }
        self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                          id_column_value=criteria_id, json_data=number_of_kids_json)
        logger.end()

    def update_min_max_height(self, criteria_id: int, min_height: int, max_height: int) -> None:
        """
        Update the minimum and maximum height for a criterion.

        :param criteria_id: The ID of the criterion to update.
        :param min_height: The new minimum height.
        :param max_height: The new maximum height.
        :type criteria_id: int
        :type min_height: int
        :type max_height: int
        :rtype: None
        """
        logger.start("Update minimum and maximum height", object={
                     "criteria_id": criteria_id, "min_height": min_height,
                     "max_height": max_height})
        number_of_kids_json = {
            "min_height": min_height,
            "max_height": max_height
        }
        self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                          id_column_value=criteria_id, json_data=number_of_kids_json)
        logger.end()

    def update_partner_experience_level(self, criteria_id: int,
                                        partner_experience_level: int) -> None:
        """
        Update the partner experience level for a criterion.

        :param criteria_id: The ID of the criterion to update.
        :param partner_experience_level: The new partner experience level.
        :type criteria_id: int
        :type partner_experience_level: int
        :rtype: None
        """
        logger.start("Update partner experience level",
                     object={"criteria_id": criteria_id,
                             "partner_experience_level": partner_experience_level})
        experience_level_json = {
            "partner_experience_level": partner_experience_level
        }
        self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                          id_column_value=criteria_id, json_data=experience_level_json)
        logger.end()

    def update_number_of_partners(self, criteria_id: int, number_of_partners: int) -> None:
        """
        Update the number of partners for a criterion.

        :param criteria_id: The ID of the criterion to update.
        :param number_of_partners: The new number of partners.
        :type criteria_id: int
        :type number_of_partners: int
        :rtype: None
        """
        logger.start("Update number of partners", object={"criteria_id": criteria_id,
                                                          "number_of_partners": number_of_partners})
        number_of_partners_json = {
            "number_of_partners": number_of_partners
        }
        self.update_by_id(table_name="criteria_table", id_column_name="criteria_id",
                          id_column_value=criteria_id, json_data=number_of_partners_json)
        logger.end()

    def delete(self, criteria_id: int) -> None:
        """
        Delete a criterion from the database.

        :param criteria_id: The ID of the criterion to delete.
        :type criteria_id: int
        :rtype: None
        """
        logger.start("Delete criteria", object={"criteria_id": criteria_id})
        self.delete_by_id(table_name="criteria_table",
                          id_column_name="criteria_id", id_column_value=criteria_id)
        logger.end(f"Criteria deleted criteria_id= {criteria_id}",
                   object={'criteria_id': criteria_id})

    def get_test_id(self, entity_type_id: int = None, group_list_id: int = None,
                    gender_list_id: int = None, location_id: int = None) -> int:
        """
        Create a test criterion and return its ID.

        :param entity_type_id: The entity type ID.
        :param group_list_id: The group list ID.
        :param gender_list_id: The gender list ID.
        :param location_id: The location ID.
        :type entity_type_id: int
        :type group_list_id: int
        :type gender_list_id: int
        :type location_id: int
        :return: The ID of the created test criterion.
        :rtype: int
        """
        logger.start("Create test criteria", object={
            "entity_type_id": entity_type_id,
            "group_list_id": group_list_id,
            "gender_list_id": gender_list_id,
            "location_id": location_id
        })
        criteria_json = {
            "entity_type_id": entity_type_id,
            "group_list_id": group_list_id,
            "gender_list_id": gender_list_id,
            "location_id": location_id
        }
        GenericCRUD("criteria").insert(
            "criteria_table", criteria_json)
        test_criteria = self.select_one_dict_by_id(
            view_table_name="criteria_view",
            select_clause_value="criteria_id", order_by="criteria_id DESC")
        for key in test_criteria:
            test_id = int(test_criteria[key])
        logger.end("Test criteria created")
        return test_id
