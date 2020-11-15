import sys, csv, time 
from multiprocessing import Pool
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient, DelimitedTextDialect, BlobQueryError

def get_explanations():
    return "Chillax, 'tis just a storage"

def query(a_query, a_blob_url, a_file_type):
    if a_file_type == 'csv':
        blob_client = BlobClient.from_blob_url(blob_url= a_blob_url)
        qa_reader = blob_client.query_blob(a_query, blob_format=DelimitedTextDialect(has_header=True), encoding='utf-8')
        return csv.reader(qa_reader.records())
    elif a_file_type == 'json':
        print("Here goes the result when querying a json. TBI (to be implemented) :D")
        return 
    else:
        print(f"Sorry, can't query a {a_file_type} file type")
        return

def read_the_news():
    return "This would read the change feed. TBI (to be implemented) :D"

def query_a_dir():
    # some_args = []
    # pool = Pool()
    # result = pool.starmap_async(query, some_args)
    # print("main script")
    # print(result.get())
    # print("end main script")
    return "TBI (to be implemented) :D"

#In the future refactor to class
# class nodbdb_client(Resource):
#     def get(self):
#         return "'cause 'tis a storage"

#     def query_a_blob(self, a_query, a_blob_url):
#         return 0

#     def insert_a_blob(self, a_blob, a_path):
#         return 0