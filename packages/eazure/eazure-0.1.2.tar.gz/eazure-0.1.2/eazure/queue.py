from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage, TextBase64EncodePolicy
from azure.core.exceptions import AzureError
import base64
import logging


class QueueManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.queue_service_client = QueueServiceClient.from_connection_string(connection_string)

    def queue_get_item(self, queue_name):
        queue_client = QueueClient.from_connection_string(conn_str=self.connection_string, queue_name=queue_name)
        peeked_messages = queue_client.peek_messages(max_messages=1)

        for peeked_message in peeked_messages:
            decoded_message = base64.b64decode(peeked_message.content).decode('utf-8')
            msg_id = peeked_message.id
            return decoded_message, msg_id

    def queue_add_message(self, queue_name, message):
        try:
            queue_client = self.queue_service_client.get_queue_client(queue=queue_name)
            queue_client.message_encode_policy = TextBase64EncodePolicy()
            queue_client.send_message(message)
            print("Message added to the queue successfully!")
        except AzureError as e:
            logging.error(f"An error occurred: {e.message}")

    def queue_get_length(self, queue_name):
        queue_client = QueueClient.from_connection_string(conn_str=self.connection_string, queue_name=queue_name)
        properties = queue_client.get_queue_properties()
        count = properties.approximate_message_count
        print("Message count: " + str(count))
        return properties.approximate_message_count

    def queue_delete_message(self, queue_name, message_id):
        queue_client = QueueClient.from_connection_string(conn_str=self.connection_string, queue_name=queue_name)
        queue_client.delete_message(message_id=message_id)
        return queue_client
