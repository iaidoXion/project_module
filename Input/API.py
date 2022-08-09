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
    except ConnectionError as e:
        logging.warning(APITYPE+' API Call Error, Error Message : ' + str(e))