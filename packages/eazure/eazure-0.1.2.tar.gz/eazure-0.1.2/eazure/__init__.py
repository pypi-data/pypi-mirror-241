from .blob import BlobManager
from .table import TableManager
from .queue import QueueManager


class Client:
    connection_string = None

    def __init__(self, connection_string=None):
        self.connection_string = connection_string or Client.connection_string

    # BLOB METHODS
    def blob_download(self, container_name, blob_name, output_file_path, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.blob_download(container_name, blob_name, output_file_path)

    def blob_upload(self, container_name, blob_name, input_file_path, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        blob_manager.blob_upload(container_name, blob_name, input_file_path)

    def blob_exists(self, container_name, blob_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.blob_exists(container_name, blob_name)

    def blob_delete(self, container_name, blob_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.blob_delete(container_name, blob_name)

    def blob_list_all_in_container(self, container_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.blob_list_all_in_container(container_name)

    def container_create(self, container_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.container_create(container_name)

    def container_list_all(self, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.container_list_all()

    def container_delete(self, container_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.container_delete(container_name)

    def rename_container(self, container_name, new_container_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.container_rename(container_name, new_container_name)

    # TABLE METHODS
    def table_create(self, table_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.table_create(table_name)

    def table_entity_create(self, table_name, new_entity, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.table_entity_create(table_name, new_entity)

    def table_entity_get_all(self, table_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.table_entity_get_all(table_name)

    def table_entity_get_single(self, table_name, partition_key, row_key, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.table_entity_get_single(table_name, partition_key, row_key)

    def table_entity_update(self, table_name, partition_key, row_key, new_entity, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.table_entity_update(table_name, partition_key, row_key, new_entity)

    def table_entity_remove(self, table_name, partition_key, row_key, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.table_entity_remove(table_name, partition_key, row_key)

    def table_entity_get_column_value(self, table_name, partition_key, row_key, column_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.table_entity_get_column_value(table_name, partition_key, row_key, column_name)

    # QUEUE METHODS
    def queue_get_item(self, queue_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        queue_manager = QueueManager(connection_string)
        return queue_manager.queue_get_item(queue_name)

    def queue_add_message(self, queue_name, message, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        queue_manager = QueueManager(connection_string)
        return queue_manager.queue_add_message(queue_name, message)

    def queue_get_length(self, queue_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        queue_manager = QueueManager(connection_string)
        return queue_manager.queue_get_length(queue_name)

    def queue_delete_message(self, queue_name, message_id, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        queue_manager = QueueManager(connection_string)
        return queue_manager.queue_delete_message(queue_name, message_id)
