from elasticsearch import Elasticsearch

index = 'iaido'
def read():
    es = Elasticsearch(["http://192.168.0.15:9200"])
    es.cat.indices()
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match":
                            {
                                "Collection Date": "2022-07-31 23:59:59"
                            }
                    },
                    {
                        "match":
                            {
                                "Collection Date": "2022-08-01 23:59:59"
                            }
                    }
                ]
            }
        }
    }


    dataList = es.search(index=index, body=body)
    print(dataList)
    """
    dataList = es.get(index=index)
    dataListAppend = []
    for data in dataList['hits']['hits'] :
        dataListAppend.append(data['_source'])

    returnList = {'resCode': 200, 'dataList': dataListAppend}
    print(returnList)
    return returnList"""