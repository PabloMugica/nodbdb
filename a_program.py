import sys, csv, time, initvars
from nodbdb import nodb_client

#init vars from a file named initvars.py (imported as module)
#blob_url has both the url + sas sign
blob_url = initvars.a_blob_url
#a query like "SELECT * FROM BlobStorage WHERE Tail_Number = 'N706JB'"
query = initvars.query

#Timing: make the query and get results
start = time.perf_counter()

csv_reader = nodb_client.query_a_csv_blob(query, blob_url) 

print(f'What da ... is this?: {nodb_client.get_explanations()}')

end = time.perf_counter()

#Loop through results, issue:find out why there are empty rows
for row in csv_reader:
    if row:
        print(str(row)) #print("*".join(row))

#Show *very precise* elapsed seconds
print(f"Time taken is {end - start}")