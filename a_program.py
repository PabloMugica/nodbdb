#init vars from a file named initvars.py (am I not enormously creative?)
import sys, csv, time, initvars
from nodbdb import nodb_client

blob_url = initvars.a_json_blob_url
sas_key = initvars.adlsas_key

#a sql query like "SELECT * FROM BlobStorage WHERE Tail_Number = 'N706JB'"
query = initvars.query_json

#Query single file and time it
start = time.perf_counter()
blob_reader = nodb_client.query(query, blob_url, sas_key) 
end = time.perf_counter()

#Query a dir
#Code

#Loop through results, issue:find out why there are empty rows
if blob_reader is None:
    print("No result found. Sorry human, better luck nextime ¯\_(ツ)_/¯")
else:
    for row in blob_reader.records():
        if row:
            print(row)
#Show (sarcastic voice) *usefully accurate* elapsed seconds
print(f"Time taken is {end - start}")