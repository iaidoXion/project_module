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
taniumSensorPath = SETTING['CORE']['Tanium']['API']['PATH']['Sensor']
taniumSensorID = SETTING['CORE']['Tanium']['API']['SensorID']

ZU = SETTING['CORE']['Zabbix']['USE']
zabbixApiUrl = SETTING['CORE']['Zabbix']['API']['apiUrl']
zabbixContentType = SETTING['CORE']['Zabbix']['API']['ContentType']
UNAME = SETTING['CORE']['Zabbix']['API']['UNAME']
PWORD = SETTING['CORE']['Zabbix']['API']['PWORD']


def plug_in(SK, APITYPE):
    try:
        logging.info('INPUT Plug In : API')
        if TU == 'true' :
            logging.info(APITYPE+' API Call Start')
            if APITYPE == 'SesstionKey':
                path = taniumSesstionKeyPath
                headers = {
                    'Authorization': taniumAuthorization
                }
            if APITYPE == 'sensor':
                path = taniumSensorPath + taniumSensorID
                headers = {
                    'session': SK,
                    'Authorization': taniumAuthorization,
                    'Content-Type': taniumContentType,
                }
            urls = taniumApiUrl + path
            logging.info('API URL : ' +urls)
            response = requests.request("GET", urls, headers=headers, verify=False)
            resCode = response.status_code
            logging.info('API Session Key Call Success, ' + 'Sesponse Status Code : ' + str(resCode))
            responseText = response.text
            if APITYPE == 'SesstionKey' :
                dataList = [responseText]
                logging.info('API Session Key : ' + dataList[0])
            if APITYPE == 'sensor':
                responseJson = json.loads(responseText)
                responseDataJson = responseJson['data']
                dataList = []
                for j in range(len(responseDataJson['result_sets'][0]['rows'])):
                    DL = []
                    for k in range(len(responseDataJson['result_sets'][0]['rows'][j]['data'])):
                        DL.append(responseDataJson['result_sets'][0]['rows'][j]['data'][k][0]['text'])
                    dataList.append(DL)
            returnList = {'resCode': resCode, 'dataList': dataList}
            return returnList



        if ZU == 'true':
            if APITYPE == 'SesstionKey':
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

                    items = ["System name", "System description", "System uptime", "Number of processes", "/: Space utilization",
                                "Memory utilization", "CPU utilization", "Version of Zabbix agent running", "Zabbix agent availability"]

                    for item in items:
                        r2 = requests.post(urls, json={
                            "jsonrpc": "2.0",
                            "method": "item.get",
                            "params": {
                                "output": ["value_type", "itemid", "name", "lastclock", "lastvalue"],
                                "filter": {
                                    "hostid": hostid,
                                    "name": item

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
                                print(data)

                            dataListAppend.append(data)
                        returnList = {'dataList': dataListAppend}

                # print(dataList)
            return returnList






    except ConnectionError as e:
        logging.warning(APITYPE+' API Call Error, Error Message : ' + str(e))