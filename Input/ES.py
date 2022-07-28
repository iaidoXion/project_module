from elasticsearch import Elasticsearch

index = 'tanium'
def ES():
    es = Elasticsearch(["http://192.168.0.15:9200"])
    es.cat.indices()
    body = {
        "query": {
            "range": {
                "@timestamp": {
                    "lt": "2022-07-26T00:00:00",
                    "gt": "2022-07-26T23:59:59"
                }
            }
        }
    }
    dataList = es.search(index=index, body = body)
    dataListAppend = []
    for  data in dataList['hits']['hits'] :
        dataListAppend.append(data['_source'])

    returnList = {'resCode': 200, 'dataList': dataListAppend}
    print(returnList)
    return returnList