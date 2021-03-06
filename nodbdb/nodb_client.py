import os, time, fire, json
#from multiprocessing import Pool
from os.path import splitext as get_ext
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient, DelimitedTextDialect, DelimitedJsonDialect, BlobQueryError, _quick_query_helper

#Get config from json file
BASE_PATH = os.path.dirname(os.path.realpath(__file__))
with open(BASE_PATH+'/config.json') as json_data_file:                                                                                                                            
    config = json.load(json_data_file)

store_conn = config['store_connection']

def query(a_query = store_conn['query_sql'], a_blob_url = store_conn['file_csv'], a_sas_key = store_conn['access_key']):
    """ Helper to query json and/or csv files on a Blob/Datalake """
    result_set = []
    start = time.perf_counter()
    #Get the file extension/type 
    a_file_name, a_file_type = get_ext(a_blob_url)

    blob_client = BlobClient.from_blob_url(blob_url= a_blob_url + a_sas_key)

    if a_file_type      == '.csv':
        qa_reader = blob_client.query_blob(a_query, blob_format=DelimitedTextDialect(has_header=True), encoding='utf-8')
    elif a_file_type    == '.json':
        qa_reader = blob_client.query_blob(a_query, blob_format=DelimitedJsonDialect(delimeter=' '), encoding='utf-8',output_format = DelimitedJsonDialect(delimiter='\n'))
    elif a_file_type    == '.parquet':
        qa_reader = None
        print("We'll do something about this")
    else:
        qa_reader = None
        print(f"Sorry, can't query a {a_file_type} file type")
        
    end = time.perf_counter()
    #Show (sarcastic voice) *usefully accurate* elapsed seconds and return records
    print(f"Time taken to get results {end - start} seconds")
    
    if qa_reader is None:
        print("No result found. Sorry human, better luck nextime ¯\_(ツ)_/¯")
    else:
        for row in qa_reader.records():
            if row:
                result_set.append(row)
    
    return result_set

def query_dir():
    """TBI (to be implemented) :D"""
    # Should it have to have a recursive option, a starmap_async exec?
    # some_args = []
    # pool = Pool()
    # result = pool.starmap(query, some_args) 
    # print("main script")
    # print(result.get())
    # print("end main script")
    return 

def read_the_news():
    """This would read the change feed. TBI (to be implemented) :D"""
    return

if __name__ == '__main__':
    #query()
    fire.Fire({
        "query": query,
        "query_dir": query_dir,
        "read_the_news": read_the_news
    })