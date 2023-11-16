from azure.data.tables import TableServiceClient, TableClient
from azure.core.exceptions import ResourceExistsError, HttpResponseError
import json
import logging


class TableManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.table_service_client = TableServiceClient.from_connection_string(connection_string)

    def table_create(self, table_name):
        table_client = self.table_service_client.create_table_if_not_exists(table_name=table_name)
        print(f'table created or located: {table_name}')
        return table_client

    def table_entity_create(self, table_name, new_entity):
        table = TableClient.from_connection_string(self.connection_string, table_name=table_name)

        try:
            table.create_entity(entity=new_entity)
            return True
        except ResourceExistsError:
            logging.info(f'Entity already exists in table: {table_name}')
            self.update_entity(table_name, new_entity['PartitionKey'], new_entity['RowKey'], new_entity)
        except Exception as e:
            logging.error(f'Failed to create entity in table: {table_name}. Error: {str(e)}')
            return False

    def table_entity_get_all(self, table_name):
        table = TableClient.from_connection_string(self.connection_string, table_name=table_name)
        entities = table.list_entities()
        entities_list = [entity for entity in entities]
        entities_json = json.dumps(entities_list, default=str)
        return entities_json

    def table_entity_get_single(self, table_name, partition_key, row_key):
        table = TableClient.from_connection_string(self.connection_string, table_name=table_name)

        try:
            entity = table.get_entity(partition_key, row_key)
            return entity
        except Exception as e:
            logging.error(f'Failed to retrieve entity with PartitionKey={partition_key} and RowKey={row_key} from table: {table_name}. Error: {str(e)}')
            return None

    def table_entity_update(self, table_name, partition_key, row_key, properties_to_update):
        table = TableClient.from_connection_string(self.connection_string, table_name=table_name)

        try:
            entity = table.get_entity(partition_key, row_key)
            for key, value in properties_to_update.items():
                entity[key] = value
            table.update_entity(entity)
            return True
        except:
            logging.error(f'Failed to update entity in table: {table_name}')
            return False

    def table_entity_remove(self, table_name, partition_key, row_key):
        table = TableClient.from_connection_string(self.connection_string, table_name=table_name)

        try:
            entity = table.get_entity(partition_key, row_key)
            table.delete_entity(entity=entity)
            return True
        except:
            logging.error(f'Failed to remove entity in table: {table_name}')
            return False

    def table_entity_get_column_value(self, table_name, partition_key, row_key, column_name):
        table = TableClient.from_connection_string(self.connection_string, table_name=table_name)
        logging.info(f'getCellValue: PK: {partition_key} | RK: {row_key}')
        entity = table.get_entity(partition_key, row_key)
        return entity[column_name]
