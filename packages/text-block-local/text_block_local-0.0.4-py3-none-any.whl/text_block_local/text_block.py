import json
import re
import time
from datetime import datetime

import mysql.connector
from user_context_remote.user_context import UserContext
from circles_local_database_python.generic_crud import GenericCRUD
from circles_number_generator.number_generator import NumberGenerator
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum

MAX_ERRORS = 5
TEXT_BLOCK_COMPONENT_ID = 143
TEXT_BLOCK_COMPONENT_NAME = "text_block_local_python_package"
DEVELOPER_EMAIL = "akiva.s@circ.zone"
object1 = {
    'component_id': TEXT_BLOCK_COMPONENT_ID,
    'component_name': TEXT_BLOCK_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}
logger = Logger.create_logger(object=object1)


class TextBlocks(GenericCRUD):
    def __init__(self):
        super().__init__(schema_name="text_block")
        UserContext.login_using_user_identification_and_password()
        self.errors_count = 0

    def get_block_fields(self, block_type_id: int) -> dict:
        """Retrieves regular expressions and field IDs based on the provided `block_type_id`."""
        logger.start("Getting regex and field_id from block_id ...")
        self.set_schema(schema_name="field")
        block_fields = dict(self.select_multi_tuple_by_where(view_table_name="block_type_field_view",
                                                             select_clause_value="field_id, regex",
                                                             where="block_type_id = %s OR block_type_id IS NULL",
                                                             params=(block_type_id,)))

        logger.end("Regex and field ids retrieved", object={'block_fields': block_fields})
        return block_fields

    def get_fields(self) -> dict:
        """Retrieves field IDs and names from the database."""
        logger.start("Getting field ids and names ...")
        self.set_schema(schema_name="field")
        fields = dict(self.select_multi_tuple_by_where(view_table_name="field_view",
                                                       select_clause_value="field_id, name"))

        logger.end("Field names and ids retrieved", object={'fields': fields})
        return fields

    def get_block_type_ids_regex(self) -> dict:
        """Retrieves block type IDs and regular expressions from the database."""
        logger.start("Getting block type ids and names ...")
        self.set_schema(schema_name="text_block_type")
        block_types = dict(self.select_multi_tuple_by_where(view_table_name="text_block_type_regex_view",
                                                            select_clause_value="text_block_type_id, regex"))

        logger.end("Block types retrieved", object={'block_types': block_types})
        return block_types

    def get_block_types(self) -> dict:
        """Retrieves block type IDs and names from the database."""
        logger.start("Getting block type ids and names ...")
        self.set_schema(schema_name="text_block_type")
        block_types = dict(self.select_multi_tuple_by_where(view_table_name="text_block_type_ml_view",
                                                            select_clause_value="text_block_type_id, name"))

        logger.end("Block types retrieved", object={'block_types': block_types})
        return block_types

    def get_text_block_ids_types(self) -> dict:
        """Retrieves text block IDs and types from the database."""
        logger.start("Getting text blocks from text_block_table ...")
        self.set_schema(schema_name="text_block")
        result = self.select_multi_tuple_by_where(view_table_name="text_block_view",
                                                  select_clause_value="text_block_id, text_block_type_id, text_without_empty_lines, text")
        text_block_ids_types = {}
        for text_block_id, type_id, text_without_empty_lines, text in result:
            if text_without_empty_lines:
                text_block_ids_types[text_block_id] = (type_id, text_without_empty_lines)
            else:
                text_block_ids_types[text_block_id] = (type_id, text)

        logger.end("Text blocks retrieved", object={'text_blocks_ids_types': text_block_ids_types})
        return text_block_ids_types

    def process_text_block(self, text_block_id: int = 0, update: bool = True, since_date: datetime = None) -> None:
        if not text_block_id and not since_date:
            logger.exception("No text_block_id or since_date provided")
            return

        if since_date is not None:
            self.process_text_blocks_updated_since_date(since_date)
        else:
            self.process_single_text_block(text_block_id, update)

    def process_text_blocks_updated_since_date(self, since_date: datetime) -> None:
        self.set_schema(schema_name="text_block")
        text_block_ids = self.select_multi_tuple_by_where(view_table_name="text_block_view",
                                                          select_clause_value="text_block_id",
                                                          where="updated_timestamp >= %s",
                                                          params=(since_date,))
        for text_block_id in text_block_ids:
            self.process_single_text_block(text_block_id[0])

    def process_single_text_block(self, text_block_id: int, update: bool = True) -> None:
        """
        1. Retrieves the text and other details of the text block.
        2. Reformat the text if needed.
        3. Identifies and updates the text block type.
        4. Extract fields from the text based on the block type's regular expressions.
        5. Updates the text block with the extracted fields in JSON format.
        """

        try:
            text, text_block_type_id, profile_id = self.get_text_block_details(text_block_id)

            # reformat text
            text = text.replace("\n", " ")

            if text_block_type_id is None:
                text_block_type_id = self.identify_and_update_text_block_type(text_block_id, text, update)

            fields_dict = self.extract_fields_from_text(text, text_block_type_id)
            self.update_text_block_fields(text_block_id, fields_dict)

        except mysql.connector.errors.DatabaseError as e:
            if "Lock wait timeout exceeded" in str(e) and self.errors_count < MAX_ERRORS:  # prevent infinite loop
                self.errors_count += 1
                logger.warn("Lock wait timeout exceeded. Retrying UPDATE after a short delay.")
                time.sleep(2)
                self.process_single_text_block(text_block_id, update)
            else:
                logger.exception("Database Error", object=e)

        except Exception as e:
            logger.exception("Error processing text block", object=e)

        self.errors_count = 0

    def get_text_block_details(self, text_block_id: int) -> tuple:
        """Retrieves text and related details for a given text block ID."""
        logger.start("Getting text block details ...", object={'text_block_id': text_block_id})
        self.set_schema(schema_name="text_block")
        result = self.select_one_tuple_by_id(view_table_name="text_block_view",
                                             select_clause_value="text_without_empty_lines, text, text_block_type_id, profile_id",
                                             id_column_name="text_block_id",
                                             id_column_value=text_block_id)

        if result[0]:
            text, text_block_type_id, profile_id = (result[0], result[2], result[3])
        else:
            text, text_block_type_id, profile_id = (result[1], result[2], result[3])

        return text, text_block_type_id, profile_id

    def extract_fields_from_text(self, text: str, text_block_type_id: int) -> dict:
        """Extracts fields from the text based on the block type's regular expressions."""
        fields_dict = {}
        block_fields = self.get_block_fields(text_block_type_id)
        fields = self.get_fields()

        for field_id, regex in block_fields.items():
            if not regex:
                continue
            try:
                re.compile(regex)
                matches = re.findall(regex, text)

                field = fields[field_id]

                if not matches:
                    continue
                fields_dict[field] = matches

                for match in matches:
                    self.process_field(field_id, match)

            except re.error as e:
                logger.exception(f"Invalid regex: {regex}", object=e)

        return fields_dict

    def update_text_block_fields(self, text_block_id: int, fields_dict: dict) -> None:
        """Updates the text block with the extracted fields in JSON format."""
        logger.start("Updating text block fields ...", object={'text_block_id': text_block_id})
        fields_json = json.dumps(fields_dict)
        self.set_schema(schema_name="text_block")
        self.update_by_id(table_name="text_block_table", id_column_name="text_block_id", id_column_value=text_block_id,
                          data_json={"fields_extracted_json": fields_json})

    def identify_and_update_text_block_type(self, text_block_id: int, text: str, update: bool = True) -> int:
        """Identifies and updates the text block type."""
        logger.start("Identifying and updating block type for text block", object={
            'text_block_id': text_block_id, 'text': text, 'update': update})
        text_block_type_id = self.identify_text_block_type(text_block_id, text)
        if not update:
            return text_block_type_id
        self.set_schema(schema_name="text_block")

        # SQL UPDATE text_block.text_block_type
        if text_block_type_id is not None:
            self.update_by_id(table_name="text_block_table", id_column_name="text_block_id", id_column_value=text_block_id,
                              data_json={"text_block_type_id": text_block_type_id})

        return text_block_type_id

    def identify_text_block_type(self, text_block_id: int, text: str) -> int:
        """Identifies the text block type."""
        logger.start("Identifying block type for text block", object={'text_block_id': text_block_id, 'text': text})
        self.set_schema(schema_name="text_block_type")

        potential_block_type_ids = self.get_block_type_ids_regex()  # TODO: why do we need this? It's not used anywhere.

        try:
            system_id, system_entity_id = self.select_one_tuple_by_id(view_table_name="text_block_type_view",
                                                                      select_clause_value="system_id, system_entity_id",
                                                                      id_column_name="text_block_type_id",
                                                                      id_column_value=text_block_id)
            # filter results with system_id and system_entity if possible
            if system_entity_id:
                results = self.select_multi_tuple_by_where(view_table_name="text_block_type_view",
                                                           select_clause_value="regex",
                                                           where="system_id = %s AND system_entity_id = %s",
                                                           params=(system_id, system_entity_id))

            else:
                results = self.select_multi_tuple_by_id(view_table_name="text_block_type_view",
                                                        select_clause_value="regex",
                                                        id_column_name="system_id",
                                                        id_column_value=system_id)
            regex_list = [regex[0] for regex in results]
            potential_block_type_ids = dict(self.select_multi_tuple_by_where(
                view_table_name="text_block_type_regex_view",
                select_clause_value="text_block_type_id, regex",
                where="regex IN %s",
                params=(regex_list,)))
        except Exception as e:
            logger.exception("No system id for text block", object=e)

        # classify block_type using regex
        for regex in potential_block_type_ids:
            try:
                re.compile(regex)
                match = re.search(regex, text)
                if match:
                    return potential_block_type_ids[regex]
            except re.error as e:
                logger.exception(f"Invalid regex: {regex}", object=e)

        # if no block type id has been found by this point
        logger.end("Unable to identify block_type_id for text block", object={'text_block_id': text_block_id})

    def check_all_text_blocks(self, update: bool = True) -> None:
        """Checks all text blocks and updates their block type if needed."""
        # For all text_blocks
        logger.start("Checking all text blocks ...")
        text_block_ids_types = self.get_text_block_ids_types()
        block_types = self.get_block_types()
        for block_type_id in text_block_ids_types:
            existing_block_type = text_block_ids_types[block_type_id][0]
            if existing_block_type:
                logger.info("\nOld block type: " + str(existing_block_type) + ", '" + block_types[
                    existing_block_type] + "' for text block " + str(block_type_id))
            else:
                logger.info("Old block type: None")
            text = (text_block_ids_types[block_type_id][1]).replace("\n", " ")
            new_block_type = self.identify_and_update_text_block_type(block_type_id, text, update)
            if new_block_type is not None:
                logger.info("Identified block type: " + str(new_block_type) + " " + block_types[new_block_type])
        logger.end("All text blocks checked")

    def update_logger_with_old_and_new_field_value(self, field_id: int, field_value_old: str,
                                                   field_value_new: str) -> None:
        """Updates the logger with the old and new field value."""
        logger.start("Updating logger with old and new field value", object={
            'field_id': field_id, 'field_value_old': field_value_old, 'field_value_new': field_value_new})
        self.set_schema(schema_name="logger")
        data_json = {"field_id": field_id, "field_value_old": field_value_old, "field_value_new": field_value_new}
        self.insert(table_name="logger_table", data_json=data_json)
        logger.end("Logger updated")

    def create_person_profile(self, fields_dict: dict) -> int:
        """Creates a person and profile based on the provided fields."""
        logger.start("Creating person and profile ...")
        self.set_schema(schema_name="person")
        created_user_id = UserContext().get_effective_user_id()
        number = NumberGenerator.get_random_number("person", "person_table")
        if "First Name" in fields_dict and "Last Name" in fields_dict:
            first_name = fields_dict["First Name"][0]
            last_name = fields_dict["Last Name"][0]
            data_json = {"number": number, "first_name": first_name, "last_name": last_name,
                         "last_coordinate": "POINT(0.0000, 0.0000)", "created_user_id": created_user_id}
        elif "Birthday" in fields_dict:
            birthday = fields_dict["Birthday"][0]
            data_json = {"number": number, "birthday_original": birthday, "last_coordinate": "POINT(0.0000, 0.0000)",
                         "created_user_id": created_user_id}
        else:
            data_json = {"number": number, "last_coordinate": "POINT(0.0000, 0.0000)",
                         "created_user_id": created_user_id}
        self.insert(table_name="person_table", data_json=data_json)

        person_id = self.cursor.lastrowid()
        visibility_id = 0  # TODO: replace this magic number.
        self.set_schema(schema_name="profile")
        data_json = {"number": number, "person_id": person_id, "visibility_id": visibility_id,
                     "created_user_id": created_user_id}
        self.insert(table_name="profile_table", data_json=data_json)

        profile_id = self.cursor.lastrowid()
        logger.end("Person and profile created", object={'person_id': person_id, 'profile_id': profile_id})

        return profile_id

    def process_field(self, processing_id, match):
        pass
        # if processing_id == 1: #birthday YYYY-MM-DD

        # else if processing_id ==2: #phone

        # return processed_value