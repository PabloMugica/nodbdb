import sys, csv, time 
from multiprocessing import Pool
from os.path import splitext as get_ext
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient, DelimitedTextDialect, BlobQueryError

def get_explanations():
    return "Sorry human, I thought 'twas a good idea"

def query(a_query, a_blob_url, a_sas_key):
   
    # here get the file type 
    a_file_name, a_file_type = get_ext(a_blob_url)

    if a_file_type == '.csv':
        blob_client = BlobClient.from_blob_url(blob_url= a_blob_url + a_sas_key)
        qa_reader = blob_client.query_blob(a_query, blob_format=DelimitedTextDialect(has_header=True), encoding='utf-8')
        return csv.reader(qa_reader.records())
    elif a_file_type == '.json':
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