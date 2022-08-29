# Import elasticsearch module
from elasticsearch import Elasticsearch 
#import json


# Method to store data in elasticsearch
def send_data_to_es(data):
 es=Elasticsearch(['https://localhost:9200'])
 res = es.index(index='employee',doc_type='devops',body=data)
 print(res)

# Method to get data from elasticsearch
def get_data_from_es():
 es=Elasticsearch(['https://localhost:9200'])
 r = es.search(index="employee", body={"query": {"match": {'Name':'john'}}})
 print(r)
 print(type(r))
 print(r["hits"]["hits"][0]["_source"])

# Main function from where the execution starts
if __name__== "__main__":
 # Define a dictoinary having required data to be stored in ES
 data = {"Name": "john", "Age":27, "address": "winterfell"}
 # Call method to store data in ES
 send_data_to_es(data)
 # Call method to get data from ES
 #get_data_from_es()