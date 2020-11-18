# nodbdb

Well, it's a helper to query files in an Azure blob/data lake storage using Azure Storage [Query Acceleration](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-query-acceleration).<br>
As you do in a DB.<br>
But it's not a DB.  

## Use Case
Imagine you have a couple of files in an Azure Data Lake Storage, csv and/or json files. Say you need to query and/or make simple aggregations about information in them. You don't have to have it in *real time*, you know sql and know how to throw a couple of lines of python too. You start thinking in a creative way to do it when...

***A rabbit hole opens right in front of your eyes.***

***A pack of consultants emerges from it, almost shouting in unison:*** 
>**We have THE Solution!**

Then they started each their own monotone monologue.<br>
Consultant 1: "You should create a notebook in Azure Databricks!!!"<br>
Consultant 2: "You can use Polybase from a Synapse Analytics instance!!!"<br>
Consultant 3: "You need to create a Synapse Analytics *PREVIEW* Workspace and then you can choose either SQL or Spark to query them!!!<br>
There was a Consultant 4 a little behind, looking down and murmuring: "You could've done it just fine with Azure Data Lake Analytics"

_... to be continued ..._

While I'm hopefully learning and working on ending this, here's a very good explanation of the feature and how to [code it in C#](https://dev.to/shibayan/query-acceleration-for-adls-alternative-to-the-lightweight-synapse-analytics-5027)

### Features
- Access via URI + SAS key
- Query a csv file
- Query a json file
### Futures
- Make this a CLI tool
