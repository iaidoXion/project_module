from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import json
with open("setting.json", encoding="UTF-8") as sf:
    SETTING = json.loads(sf.read())
TU = SETTING['CORE']['Tanium']['USE']
TESURL = SETTING['CORE']['Tanium']['ES']['URL']
TESPORT = SETTING['CORE']['Tanium']['ES']['PORT']
TESSOI = SETTING['CORE']['Tanium']['ES']['SOURCE']['INDEX']
TESSOMF = SETTING['CORE']['Tanium']['ES']['SOURCE']['MappingFile']
TESSTI = SETTING['CORE']['Tanium']['ES']['STATISTICS']['INDEX']
TESSTMF = SETTING['CORE']['Tanium']['ES']['STATISTICS']['MappingFile']

def plug_in(data, outputType) :
    try:
        yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
        if outputType == 'source':
            indexName = TESSOI
            mappingJsonFile = TESSOMF
            dataCount = len(data)
        elif outputType == 'statistics':
            indexName = TESSTI
            mappingJsonFile = TESSTMF
            dataCount = len(data['classification'])

        es = Elasticsearch([TESURL+":"+TESPORT])
        with open(mappingJsonFile, encoding="UTF-8") as mf:
            mapping = json.load(mf)

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
    except :
        print('ES Failure')
    #es.indices.delete(index='iaido_statistics')



    #es.indices.delete(index="인덱스명")
