import os, uuid
import config
from django.http.response import JsonResponse
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)

CONTAINER_NAME = "storage"
BLOB_NAME = "staricemountainCountTwitterPicture"

def upload_from_url(url: str):
	blob_service_client = BlobServiceClient.from_connection_string(config.AZURE_STORAGE_CONNECTION_STRING)
	blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

	if (blob_client.exists):
		blob_client.delete_blob()
		blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

	blob_client.upload_blob_from_url(url)

