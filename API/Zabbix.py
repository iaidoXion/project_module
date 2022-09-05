import requests
import json
import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

ZAU = SETTING['CORE']['Zabbix']['API']['apiUrl']
ZAJRPC = SETTING['CORE']['Zabbix']['API']['jsonrpc']
ZAMSK = SETTING['CORE']['Zabbix']['API']['method']['SesstionKey']
ZAMHO = SETTING['CORE']['Zabbix']['API']['method']['host']
ZAMI = SETTING['CORE']['Zabbix']['API']['method']['item']
ZAMHI = SETTING['CORE']['Zabbix']['API']['method']['history']
ZAUNM = SETTING['CORE']['Zabbix']['API']['UNAME']
ZAPWD = SETTING['CORE']['Zabbix']['API']['PWORD']


def plug_in(SK, APITYPE, data):
    try:
        logging.info('Zabbix '+APITYPE+' Data INPUT Plug In : API')
        logging.info('Zabbix '+APITYPE+' Data API Call Start')
        dataList = []
        apiUrl = ZAU
        logging.info('Zabbix ' + APITYPE + ' Data API URL : ' + apiUrl)
        if APITYPE == 'SesstionKey':
            r = requests.post(apiUrl, json={
                "jsonrpc": ZAJRPC, "method": ZAMSK, "params": {"user": ZAUNM, "password": ZAPWD}, "id": 1
            })
            dataList.append(r.json()['result'])
        if APITYPE == 'assetHost':
            r = requests.post(apiUrl, json={
                "jsonrpc": ZAJRPC, "method": ZAMHO,
                "params": {"output": ["hostid", "host"], "with_items": "True", "selectInterfaces": ["ip"]}, "auth": SK,
                "id": 1
            })
            responseJson = json.loads(r.text)
            responseDataJson = responseJson['result']
            data = responseDataJson

        if APITYPE == 'assetItem':
            items = ["System name", "System description", "System uptime", "Number of processes",
                     "/: Space utilization", "Memory utilization", "CPU utilization", "Version of Zabbix agent running",
                     "Zabbix agent availability"]
        for d in data:
            if APITYPE == 'assetHost':
                hostid = d['hostid']
                host = d['host']
                ip = d['interfaces'][0]['ip']
                dataList.append({'hostId': hostid, 'host': host, 'ip': ip})
            if APITYPE == 'assetItem':
                for item in items:
                    r = requests.post(apiUrl, json={
                        "jsonrpc": ZAJRPC, "method": ZAMI, "params": {"output": ["value_type", "itemid", "name"],
                                                                      "filter": {"hostid": d['hostId'], "name": item}},
                        "auth": SK, "id": 1
                    })
                    responseJson = json.loads(r.text)
                    responseDataJson = responseJson['result']
                    dataList.append(({'hostId': d['hostId'], 'host': d['host'], 'ip': d['ip'],
                                      'itemId': responseDataJson[0]['itemid'], 'itemName': responseDataJson[0]['name'],
                                      'valueType': responseDataJson[0]['value_type']}))
            if APITYPE == 'asset':
                r = requests.post(apiUrl, json={
                    "jsonrpc": ZAJRPC, "method": ZAMHI,
                    "params": {"history": d['valueType'], "sortfield": "clock", "sortorder": "DESC", "limit": 1,
                               "filter": {"itemid": d['itemId']}},
                    "auth": SK,
                    "id": 1
                })
                responseJson = json.loads(r.text)
                items = responseJson['result']
                for item in items:
                    dataList.append({'host': d['host'], 'hostid': d['hostId'], 'ip': d['ip'], 'itemid': d['itemId'],
                                     'itemname': d['itemName'], 'value_type': d['valueType'], 'clock': item['clock'],
                                     'value': item['value']})
        resCode = r.status_code
        returnList = {'resCode': resCode, 'dataList': dataList}
        return returnList
        logging.warning('Zabbix ' + APITYPE + ' Data API Call Success')
        logging.warning('Zabbix ' + APITYPE + ' Data API Response Code : '+str(resCode))
    except ConnectionError as e:
        logging.warning('Zabbix '+APITYPE+' Data API Call Error, Error Message : ' + str(e))