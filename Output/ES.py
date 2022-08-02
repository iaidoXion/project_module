from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
#today = datetime.today().strftime("%Y-%m-%d")
indexName = 'iaido'
def write(data, outputType) :
    es = Elasticsearch(["http://192.168.0.15:9200"])
    indexList = es.cat.indices(format='json')
    indexArray = []
    for ID in indexList:
        indexArray.append(ID['index'])
    if indexName not in indexArray:
        es.indices.create(index=indexName)
    for i in range(len(data)) :
        if outputType == 'asset' :
            insertData = {
                "Num" : i,
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
                "Collection Date" : yesterday+ " 23:59:59"
            }
        #print(insertData)
        es.index(index=indexName, document=insertData)
    """
    es.indices.delete(index=indexName)
    """

    #es.indices.delete(index="인덱스명")
