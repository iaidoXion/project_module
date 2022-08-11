import requests
import json
import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

TAU = SETTING['CORE']['Tanium']['API']['apiUrl']
TAA = SETTING['CORE']['Tanium']['API']['Authorization']
TACT = SETTING['CORE']['Tanium']['API']['ContentType']
TASKP = SETTING['CORE']['Tanium']['API']['PATH']['SesstionKey']
TASP = SETTING['CORE']['Tanium']['API']['PATH']['Sensor']
TASID = SETTING['CORE']['Tanium']['API']['SensorID']

ZAU = SETTING['CORE']['Zabbix']['API']['apiUrl']
ZAJRPC = SETTING['CORE']['Zabbix']['API']['jsonrpc']
ZAMSK = SETTING['CORE']['Zabbix']['API']['method']['SesstionKey']
ZAMHO = SETTING['CORE']['Zabbix']['API']['method']['host']
ZAMI = SETTING['CORE']['Zabbix']['API']['method']['item']
ZAMHI = SETTING['CORE']['Zabbix']['API']['method']['history']
ZAUNM = SETTING['CORE']['Zabbix']['API']['UNAME']
ZAPWD = SETTING['CORE']['Zabbix']['API']['PWORD']


def plug_in(SK, core, APITYPE, data):
    try:
        logging.info(core+' '+APITYPE+' Data INPUT Plug In : API')
        logging.info(core+' '+APITYPE+' Data API Call Start')
        dataList = []
        if core == 'tanium' :
            apiUrl = TAU
        if core == 'zabbix':
            apiUrl = ZAU

        if core == 'tanium':
            if APITYPE == 'SesstionKey':
                path = TASKP
                headers = {'Authorization': TAA}
            if APITYPE == 'sensor':
                path = TASP + TASID
                headers = {'session': SK, 'Authorization': TAA, 'Content-Type': TACT}
            urls = apiUrl + path
            logging.info(core + ' ' + APITYPE + ' Data API URL : '+urls)
            response = requests.request("GET", urls, headers=headers, verify=False)
            resCode = response.status_code
            logging.info('API Session Key Call Success, ' + 'Sesponse Status Code : ' + str(resCode))
            responseText = response.text
            if APITYPE == 'SesstionKey' :
                dataList.append(responseText)
            if APITYPE == 'sensor':
                responseJson = json.loads(responseText)
                responseDataJson = responseJson['data']
                for j in range(len(responseDataJson['result_sets'][0]['rows'])):
                    DL = []
                    for k in range(len(responseDataJson['result_sets'][0]['rows'][j]['data'])):
                        DL.append(responseDataJson['result_sets'][0]['rows'][j]['data'][k][0]['text'])
                    dataList.append(DL)

        if core == 'zabbix':
            logging.info(core + ' ' + APITYPE + ' Data API URL : ' + apiUrl)
            if APITYPE == 'SesstionKey':
                r = requests.post(apiUrl, json={
                    "jsonrpc": ZAJRPC, "method": ZAMSK, "params": {"user": ZAUNM, "password": ZAPWD}, "id": 1
                })
                dataList.append(r.json()['result'])
            if APITYPE == 'assetHost':
                r = requests.post(apiUrl, json={
                    "jsonrpc": ZAJRPC, "method": ZAMHO, "params": {"output": ["hostid", "host"], "with_items": "True", "selectInterfaces": ["ip"]}, "auth": SK, "id": 1
                })
                responseJson = json.loads(r.text)
                responseDataJson = responseJson['result']
                data = responseDataJson

            if APITYPE == 'assetItem':
                items = ["System name", "System description", "System uptime", "Number of processes", "/: Space utilization", "Memory utilization", "CPU utilization", "Version of Zabbix agent running", "Zabbix agent availability"]
            for d in data:
                if APITYPE == 'assetHost':
                    hostid = d['hostid']
                    host = d['host']
                    ip = d['interfaces'][0]['ip']
                    dataList.append({'hostId': hostid, 'host': host, 'ip': ip})
                if APITYPE == 'assetItem':
                    for item in items:
                        r = requests.post(apiUrl, json={
                            "jsonrpc": ZAJRPC, "method": ZAMI, "params": {"output": ["value_type", "itemid", "name"],  "filter": {"hostid": d['hostId'], "name": item}}, "auth": SK, "id": 1
                        })
                        responseJson = json.loads(r.text)
                        responseDataJson = responseJson['result']
                        dataList.append(({'hostId' : d['hostId'], 'host' : d['host'], 'ip' : d['ip'], 'itemId' : responseDataJson[0]['itemid'], 'itemName' : responseDataJson[0]['name'], 'valueType' : responseDataJson[0]['value_type']}))
                if APITYPE == 'asset':
                    r = requests.post(apiUrl, json={
                        "jsonrpc": ZAJRPC, "method": ZAMHI,
                        "params": {"history": d['valueType'], "sortfield": "clock", "sortorder": "DESC", "limit": 1, "filter": {"itemid": d['itemId']}},
                        "auth": SK,
                        "id": 1
                    })
                    responseJson = json.loads(r.text)
                    items = responseJson['result']
                    for item in items :
                        dataList.append({'host': d['host'], 'hostid': d['hostId'], 'ip': d['ip'], 'itemid': d['itemId'], 'itemname': d['itemName'], 'value_type': d['valueType'], 'clock': item['clock'], 'value': item['value']})
            resCode = r.status_code
        returnList = {'resCode': resCode, 'dataList': dataList}
        return returnList
        logging.warning(core + ' ' + APITYPE + ' Data API Call Success')
        logging.warning(core + ' ' + APITYPE + ' Data API Response Code : '+str(resCode))
    except ConnectionError as e:
        logging.warning(core+' '+APITYPE+' Data API Call Error, Error Message : ' + str(e))