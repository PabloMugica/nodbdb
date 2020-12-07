#init vars from a file named initvars.py (am I not enormously creative?)
import initvars
from nodbdb import nodb_client

blob_url = initvars.a_csv_blob_url
sas_key = initvars.adlsas_key

#a sql query like "SELECT * FROM BlobStorage WHERE Tail_Number = 'N706JB'"
query = initvars.query_csv

#Query single file
blob_reader = nodb_client.query(query, blob_url, sas_key) 

#Query a dir

#Results
print(blob_reader)