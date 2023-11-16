from azure.storage.blob import BlobServiceClient, BlobType, ContainerClient
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
import os
import tempfile
import logging


class BlobManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    def blob_exists(self, container_name, blob_name):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )

        # If blob exists don't upload
        exists = blob_client.exists()

        if exists:
            print(f"{blob_name} was found in the {container_name} container")
        else:
            print(f"{blob_name} was not found in the {container_name}")
        return exists

    def blob_delete(self, container, blob_name):
        blob_client = self.blob_service_client.get_blob_client(
            container=container, blob=blob_name
        )
        try:
            blob_client.delete_blob()
            print(f"deleted {blob_name} from the {container} container")
            return True
        except:
            print(f"failed to delete {blob_name} from {container} container")
            return False

    def blob_upload(self, container_name, blob_name, local_file_path):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )

        # check if container exists
        container = self.container_create(container_name)
        logging.info(f"container {container_name} exists")

        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"uploaded {blob_name} to the {container_name} container")

    def blob_download(self, container_name, blob_name, output_file_path):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )

        with open(output_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        print(f"File downloaded successfully to {output_file_path}")

    def blob_list_all_in_container(self, container_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_list = container_client.list_blobs()

        # Iterate over the blob_list to get the blob names
        blob_names = [blob.name for blob in blob_list]

        return blob_names

    def container_list_all(self):
        containers = []
        for container in self.blob_service_client.list_containers():
            containers.append(container.name)

        return containers

    def container_create(self, container_name):
        try:
            container_client = self.blob_service_client.create_container(container_name)
            print(f"Container {container_name} created")
            return container_client
        except HttpResponseError as e:
            if (
                e.status_code == 409
            ):  # HTTP status code 409 means 'Conflict', i.e., the resource already exists
                print(f"Container {container_name} already exists")
                return True

    def container_delete(self, container_name):
        try:
            container_client = self.blob_service_client.get_container_client(container_name)
            container_client.delete_container()
            print(f"Container {container_name} deleted")
        except ResourceNotFoundError:
            print(f"Container {container_name} not found.")

    def container_rename(self, old_name, new_name):
        # Create a new container
        try:
            self.container_create(new_name)
        except Exception as e:
            print(f"Failed to create container {new_name}. Error: {str(e)}")
            return

        # Get reference to the old container
        try:
            old_container_client = self.blob_service_client.get_container_client(old_name)
        except ResourceNotFoundError:
            print(f"Container {old_name} not found.")
            return

        # Copy all the blobs from old container to new container
        try:
            blobs = self.blob_list_all_in_container(old_name)
            for blob in blobs:
                old_blob_client = old_container_client.get_blob_client(blob)
                # Download the blob to a stream
                data = old_blob_client.download_blob().readall()
                # Create a temporary file and write the data to it
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(data)
                # Upload the temporary file to the new container
                self.blob_upload(new_name, blob, temp_file.name)
                # Delete the temporary file
                os.remove(temp_file.name)

            print(f"All blobs copied from container {old_name} to {new_name}")
        except Exception as e:
            print(f"Failed to copy blobs. Error: {str(e)}")
            return

        # Delete the old container
        try:
            self.container_delete(old_name)
        except ResourceNotFoundError:
            print(f"Container {old_name} not found.")

