import requests
import json
import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
apiUrl = SETTING['API']['apiUrl']
Authorization = SETTING['API']['Authorization']
ContentType = SETTING['API']['ContentType']
SesstionKeyPath = SETTING['API']['PATH']['SesstionKey']
AssetPath = SETTING['API']['PATH']['Asset']
SensorPath = SETTING['API']['PATH']['Sensor']
SensorID = SETTING['API']['SensorID']

def read(SK, APITYPE):
    try:
        if APITYPE == 'Auth' :
                logging.info('API Session Key Call Start')
                path = SesstionKeyPath
                urls = apiUrl + path
                headers = {
                    'Authorization': Authorization
                }
                response = requests.request("GET", urls, headers=headers, verify=False)
                resCode = response.status_code
                sessionKey = response.text
                returnList = sessionKey
                logging.info('API Session Key Call Success, ' + 'Status Code : ' + str(resCode))
                logging.info('API Session Key : ' + returnList)
        elif APITYPE == 'Asset' :
            path = AssetPath
            urls = apiUrl + path
            headers = {
                'session': SK,
                'Authorization': Authorization,
                'Content-Type': ContentType,
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
            path = SensorPath + SensorID
            urls = apiUrl + path
            headers = {
                'session': SK,
                'Authorization': Authorization,
                'Content-Type': ContentType,
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
    except ConnectionError as e:
        logging.warning('API Session Key Call Error, Error Message : ' + str(e))


