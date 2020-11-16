import sys, csv, time, initvars
from nodbdb import nodb_client

#init vars from a file named initvars.py (am I not enormously creative?)
#blob_url has both the url + sas sign
blob_url = initvars.a_blob_url
sas_key = initvars.adlsas_key

#a query like "SELECT * FROM BlobStorage WHERE Tail_Number = 'N706JB'"
query = initvars.query

#Timing: make the query and get results
start = time.perf_counter()
csv_reader = nodb_client.query(query, blob_url, sas_key) 
end = time.perf_counter()

#Loop through results, issue:find out why there are empty rows
if csv_reader is None:
    print("No result found. Sorry human, better luck nextime ¯\_(ツ)_/¯")
else:
    for row in csv_reader:
        if row:
            print(str(row)) #print("*".join(row))
#Show (in sarcastic voice) *very precise* elapsed seconds
print(f"Time taken is {end - start}")