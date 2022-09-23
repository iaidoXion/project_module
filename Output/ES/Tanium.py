from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import json
import logging
with open("setting.json", encoding="UTF-8") as sf:
    SETTING = json.loads(sf.read())

TSOESURL = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['ES']['URL']
TSOESP = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['ES']['PORT']
TSOESI = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['ES']['INDEX']
TSOESMF = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['ES']['MappingFile']

TSTESURL = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['ES']['URL']
TSTESP = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['ES']['PORT']
TSTESI = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['ES']['INDEX']
TSTESMF = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['ES']['MappingFile']




def plug_in(data, core, outputType) :
    try:
        logging.info(core + ' ' + outputType + ' Data OUTPUT Plug In : ES')
        logging.info(core + ' ' + outputType + ' Data ES connection(Insert) Start')
        yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
        today = datetime.today().strftime("%Y-%m-%d")
        if outputType == 'source':
            TESURL = TSOESURL
            TESPORT = TSOESP
            indexName = TSOESI
            mappingJsonFile = TSOESMF
            dataCount = len(data)
        elif outputType == 'statistics':
            TESURL = ''
            TESPORT = ''
            indexName = TSTESI
            mappingJsonFile = TSTESMF
            dataCount = len(data['classification'])
        logging.info('Insert Data Type : ' + outputType)
        logging.info('ES URL : ' + TESURL+':'+TESPORT)
        logging.info('ES Index Name : ' + indexName)
        logging.info('Mapping File : ' + mappingJsonFile)
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
            logging.info('Insert Data Count : ' + str(dataCount))
            es.index(index=indexName, document=insertData)
    except ConnectionError as e:
        logging.warning(outputType + ' ES Data Insert Failure : ' + str(e))
    #es.indices.delete(index='iaido_statistics')



    #es.indices.delete(index="인덱스명")
