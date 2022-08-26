from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import json
import logging
yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
twodaysago = (datetime.today() - timedelta(2)).strftime("%Y%m%d")
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TSOESURL = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['ES']['URL']
TSOESPORT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['ES']['PORT']
TSOESSOURCEINDEX = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['ES']['INDEX']

TSTESURL = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['ES']['URL']
TSTESPORT = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['ES']['PORT']
TSTESSOURCEINDEX = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['ES']['INDEX']
def plug_in(dataType):
    try:
        logging.info(dataType+' INPUT Plug In : ES')
        if dataType == 'source' :
            TESURL = TSOESURL
            TESPORT = TSOESPORT
            indexName = TSOESSOURCEINDEX
        if dataType == 'statistics' :
            TESURL = TSTESURL
            TESPORT = TSTESPORT
            indexName = TSTESSOURCEINDEX
        es = Elasticsearch([TESURL + ":" + TESPORT])
        searchCount = {
            "query": {
                "match_all": {}
            }

        }
        res = es.search(index=indexName, body=searchCount)
        dataCount = res['hits']['total']['value']
        if dataType == 'source' :
            body = {
                "size": dataCount,
                "query": {
                    "match_all": {}
                }

            }
        if dataType == 'statistics' :
            body = {
                "size": dataCount,
                "query": {
                    "bool": {
                        "must": {
                            "bool": {
                                "should": [
                                    {
                                        "match": {
                                            "Collection Date": yesterday
                                        }
                                    },
                                    {
                                        "match": {
                                            "Collection Date": twodaysago
                                        }
                                    }
                                ]
                            }
                        }
                    }
                }
            }

        resData = es.search(index=indexName, body=body)
        yesterdayDL = []
        twodaysagoDL = []
        dataListAppend = []
        for data in resData['hits']['hits']:
            if dataType == 'source':
                dataListAppend.append(data['_source'])
            if dataType == 'statistics':
                if data['_source']['Collection Date'] == yesterday:
                    yesterdayDL.append(data['_source'])
                elif data['_source']['Collection Date'] == twodaysago:
                    twodaysagoDL.append(data['_source'])
        if dataType == 'source':
            returnData = {'dataList': dataListAppend}
        if dataType == 'statistics':
            returnData = {'yesterday': yesterdayDL, 'twodaysago': twodaysagoDL}
        return returnData
    except :
        print('ES Failure')


    """
    searchKword = [twodaysago,yesterday]
    dataListAppend = []
    for i in range(len(searchKword)) :
        body = {
            "size": dataCount,
            "query": {
                "match": {"Collection Date": searchKword[i]}
            }
        }
        resData = es.search(index=indexName, body=body)
        for data in resData['hits']['hits']:
            dataListAppend.append(data['_source'])
    return dataListAppend
    """
    """
    dataList = es.search(index='iaido', body=body)
    dataListAppend = []
    for data in resData['hits']['hits']:
        dataListAppend.append(data['_source'])
    

    returnList = dataListAppend
    print(returnList)
    return returnList

    
    t2 = es.search(index=index, body=body2)
    print(t1['hits']['hits']['_source'])
    print(t2['hits']['hits']['_source'])
    """
    """
    dataList = es.get(index=index)
    """

    #print(dataList)

