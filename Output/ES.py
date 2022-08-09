from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import json


def plug_in(data, outputType) :
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
    if outputType == 'source':
        indexName = 'iaido'
        mappingJsonFile = "source.json"
        dataCount = len(data)
    elif outputType == 'statistics':
        indexName = 'iaido_statistics'
        mappingJsonFile = "statistics.json"
        dataCount = len(data['classification'])

    es = Elasticsearch(["http://192.168.0.15:9200"])
    with open('Mapping/ES/'+mappingJsonFile, encoding="UTF-8") as f:
        mapping = json.load(f)

    if es.indices.exists(index=indexName):
        pass
    else:
        es.indices.create(index=indexName, body=mapping)
    for i in range(dataCount) :
        if outputType == 'source' :
            insertData = {
                "Computer ID": data['computer_id'][i],
                "Computer Name": data['computer_name'][i],
                "Last Reboot": data['last_reboot'][i],
                "Disk Total Space": data['disk_total_space'][i],
                'Disk Used Space': data['disk_used_space'][i],
                'OS Platform': data['os_platform'][i],
                "Operating System": data['operating_system'][i],
                "Is Virtual": data['is_virtual'][i],
                'Chassis Type': data['chassis_type'][i],
                "IPv4 Address": data['ip_address'][i],
                "Listen Port Count": data['listen_port_count'][i],
                "Established Port Count": data['established_port_count'][i],
                "Used Memory": data['ram_use_size'][i],
                "Total Memory": data['ram_total_size'][i],
                "Collection Date" : yesterday
            }
        elif outputType == 'statistics' :
            insertData = {
                "classification" : data['classification'][i],
                "item" : data['item'][i],
                "item_count" : data['count'][i],
                "statistics_collection_date" : yesterday
            }
        es.index(index=indexName, document=insertData)

    #es.indices.delete(index='iaido_statistics')



    #es.indices.delete(index="인덱스명")
