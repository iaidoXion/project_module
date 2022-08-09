import requests
import json
import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

TU = SETTING['CORE']['Tanium']['USE']
taniumApiUrl = SETTING['CORE']['Tanium']['API']['apiUrl']
taniumAuthorization = SETTING['CORE']['Tanium']['API']['Authorization']
taniumContentType = SETTING['CORE']['Tanium']['API']['ContentType']
taniumSesstionKeyPath = SETTING['CORE']['Tanium']['API']['PATH']['SesstionKey']
taniumAssetPath = SETTING['CORE']['Tanium']['API']['PATH']['Asset']
taniumSensorPath = SETTING['CORE']['Tanium']['API']['PATH']['Sensor']
taniumSensorID = SETTING['CORE']['Tanium']['API']['SensorID']

ZU = SETTING['CORE']['Zabbix']['USE']
zabbixApiUrl = SETTING['CORE']['Zabbix']['API']['apiUrl']
zabbixContentType = SETTING['CORE']['Zabbix']['API']['ContentType']
UNAME = SETTING['CORE']['Zabbix']['API']['UNAME']
PWORD = SETTING['CORE']['Zabbix']['API']['PWORD']


def plug_in(SK, APITYPE):
    try:
        if TU == 'true' :
            if APITYPE == 'Auth' :
                logging.info('API Session Key Call Start')
                path = taniumSesstionKeyPath
                urls = taniumApiUrl + path
                headers = {
                    'Authorization': taniumAuthorization
                }
                response = requests.request("GET", urls, headers=headers, verify=False)
                resCode = response.status_code
                sessionKey = response.text
                returnList = sessionKey
                logging.info('API Session Key Call Success, ' + 'Status Code : ' + str(resCode))
                logging.info('API Session Key : ' + returnList)
            elif APITYPE == 'Asset' :
                path = taniumAssetPath
                urls = taniumApiUrl + path
                headers = {
                    'session': SK,
                    'Authorization': taniumAuthorization,
                    'Content-Type': taniumContentType,
                }
                response = requests.request("GET", urls, headers=headers, verify=False)
                resCode = response.status_code
                assetText = response.text
                assetJson = json.loads(assetText)
                assetsDataJson = assetJson['data']

                dataListAppend = []
                for i in range(len(assetJson['data'])):
                    data = assetsDataJson[i]
                    if data['id'] and data['computer_name'] and data['computer_id'] and data['os_platform'] and data[
                        'operating_system'] and data['ci_logical_disk'] and data['last_seen_at'] and data['chassis_type'] and data[
                        'ip_address'] and data['ram'] != None:
                        id = data['id']
                        computer_name = data['computer_name']
                        computer_id = data['computer_id']
                        os_platform = data['os_platform']
                        operating_system = data['operating_system']
                        drive_use_size = str(data['ci_logical_disk'][0]['free_space'])
                        last_seen_at = data['last_seen_at']
                        chassis_type = data['chassis_type']
                        ip_address = data['ip_address']
                        ram = data['ram']
                        data = {
                            'id': id,
                            'computer_name': computer_name,
                            'computer_id': computer_id,
                            'os_platform': os_platform,
                            'operating_system': operating_system,
                            'drive_use_size': drive_use_size,
                            'last_seen_at': last_seen_at,
                            'asset_item': chassis_type,
                            'ip_address': ip_address,
                            'ram': ram
                        }
                        dataListAppend.append(data)
                    dataList = dataListAppend
                    returnList = {'resCode': resCode, 'dataList': dataList}
                    # print(dataList)
            elif APITYPE == 'sensor':
                path = taniumSensorPath + taniumSensorID
                urls = taniumApiUrl + path
                headers = {
                    'session': SK,
                    'Authorization': taniumAuthorization,
                    'Content-Type': taniumContentType,
                }
                response = requests.request("GET", urls, headers=headers, verify=False)
                resCode = response.status_code

                assetText = response.text
                assetJson = json.loads(assetText)
                assetsDataJson = assetJson['data']
                dataList = assetsDataJson['result_sets'][0]['rows']
                columnsListAppend = []
                dataListAppend = []
                for j in range(len(dataList)):
                    DL = []
                    for k in range(len(dataList[j]['data'])):
                        DL.append(dataList[j]['data'][k][0]['text'])
                    dataListAppend.append(DL)
                returnList = {'resCode': resCode, 'dataList': dataListAppend}

            return returnList



        if ZU == 'true':
            if APITYPE == 'Auth':
                logging.info('Zabbix API Session Key Call Start')
                urls = zabbixApiUrl


                r = requests.post(zabbixApiUrl, json={
                    "jsonrpc": "2.0",
                    "method": "user.login",
                    "params": {
                        "user": UNAME,
                        "password": PWORD
                    },
                    "id": 1

                }
                                  )
                sessionKey = r.json()['result']
                resCode = r.status_code
                # print(sessionKey)
                returnList = sessionKey
                logging.info('Zabbix API Session Key Call Success, ' + 'Status Code : ' + str(resCode))
                logging.info('Zabbix API Session Key : ' + returnList)

            elif APITYPE == 'Asset':
                dataListAppend = []
                urls = zabbixApiUrl
                r = requests.post(urls, json={
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output": ["hostid", "host"],
                        "with_items": "True",
                        "selectInterfaces": [
                            "ip"
                        ]
                    },
                    "auth": SK,
                    "id": 1
                }
                                  )
                hostText = r.text
                hostJson = json.loads(hostText)
                hostCount = len(hostJson['result'])
                hostDataJson = hostJson['result']

                for i in range(0, hostCount):
                    hostid = hostDataJson[i]['hostid']
                    host = hostDataJson[i]['host']
                    ip = hostDataJson[i]['interfaces'][0]['ip']

                    r2 = requests.post(urls, json={
                        "jsonrpc": "2.0",
                        "method": "item.get",
                        "params": {
                            "output": ["value_type", "itemid", "name", "lastclock", "lastvalue"],
                            "filter": {
                                "hostid": hostid

                            }

                        },
                        "auth": SK,
                        "id": 1
                    }
                                       )

                    itemText = r2.text
                    itemJson = json.loads(itemText)
                    itemCount = len(itemJson['result'])
                    itemDataJson = itemJson['result']

                    # print(itemDataJson)
                    # print(itemCount)

                    for j in range(0, itemCount):
                        itemid = itemDataJson[j]['itemid']
                        itemname = itemDataJson[j]['name']
                        value_type = itemDataJson[j]['value_type']

                        r3 = requests.post(urls, json={
                            "jsonrpc": "2.0",
                            "method": "history.get",
                            "params": {

                                "history": value_type,
                                "sortfield": "clock",
                                "sortorder": "DESC",
                                "limit": 1,

                                "filter": {
                                    "itemid": itemid
                                }

                            },

                            "auth": SK,
                            "id": 1
                        }
                                           )

                        historyText = r3.text
                        historyJson = json.loads(historyText)
                        historyCount = len(historyJson['result'])
                        historyDataJson = historyJson['result']

                        for k in range(0, historyCount):
                            clock = historyDataJson[k]['clock']
                            value = historyDataJson[k]['value']

                            data = {
                                'host': host,
                                'hostid': hostid,
                                'ip': ip,
                                'itemid': itemid,
                                'itemname': itemname,
                                'value_type': value_type,
                                'clock': clock,
                                'value': value
                            }
                            # print(data)

                        dataListAppend.append(data)
                    returnList = {'dataList': dataListAppend}

                # print(dataList)
            return returnList






    except ConnectionError as e:
        logging.warning('API Session Key Call Error, Error Message : ' + str(e))


