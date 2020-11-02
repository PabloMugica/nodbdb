import sys, csv 
import time
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient, DelimitedTextDialect, BlobQueryError

def get_explanations():
    return "Chillax, 'tis just a storage"

def query_a_csv_blob(a_query, a_blob_url):

    blob_client = BlobClient.from_blob_url(blob_url= a_blob_url)
    qa_reader = blob_client.query_blob(a_query, blob_format=DelimitedTextDialect(has_header=True), encoding='utf-8')
    return csv.reader(qa_reader.records())

#In the future refactor to class
# class nodbdb_client(Resource):
#     def get(self):
#         return "'cause 'tis a storage"

#     def query_a_blob(self, a_query, a_blob_url):
#         return 0

#     def insert_a_blob(self, a_blob, a_path):
#         return 0