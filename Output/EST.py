from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import json
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
#today = datetime.today().strftime("%Y-%m-%d")

def write() :
    indexName = 'iaido2'
    es = Elasticsearch(["http://192.168.0.15:9200"])
    with open('mapping.json', 'r') as f:
        mapping = json.load(f)

    if es.indices.exists(index=indexName):
        pass
    else:
        es.indices.create(index=indexName, body=mapping)
    doc = {
        "category": "kkk",
        "c_key": "1234",
        "price": "11400",
        "status": 1,
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }

    es.index(index=indexName, body=doc)

    searchCount = {
        "query" : {
            "match_all" : {}
        }

    }
    res = es.search(index=indexName, body=searchCount)
    dataCount = res['hits']['total']['value']

    body = {
        "size" : dataCount,
        "query": {
            "match_all": {}
        }
    }

    resData = es.search(index=indexName, body=body)

    print(resData)

    es.indices.delete(index='iaido2')

