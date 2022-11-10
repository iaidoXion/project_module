import requests
import json
import urllib3
import logging
import time
from pprint import pprint
from ast import literal_eval

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

APIURL = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['URL']
SKPATH = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['PATH']['SesstionKey']
SPATH = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['PATH']['Sensor']
SID = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['SensorID']
APIUNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['username']
APIPWD = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['password']


def plug_in(SK, APITYPE):
    try:
        logging.info('Tanium '+APITYPE+' Data INPUT Plug In : API')
        logging.info('Tanium '+APITYPE+' Data API Call Start')
        dataList = []
        apiUrl = APIURL
        if APITYPE == 'SesstionKey':
            path = SKPATH
            headers = '{"username": "' + APIUNM + '", "domain": "", "password": "' + APIPWD + '"}'
        if APITYPE == 'sensor':
            path = SPATH + SID
            headers = {'session': SK}
        urls = apiUrl + path
        logging.info('Tanium ' + APITYPE + ' Data API URL : ' + urls)
        if APITYPE == 'SesstionKey':
            response = requests.post(urls, data=headers, verify=False)
        if APITYPE == 'sensor':
            response = requests.post(urls, headers=headers, verify=False)
        resCode = response.status_code
        logging.info('API Session Key Call Success, ' + 'Sesponse Status Code : ' + str(resCode))
        responseText = response.content.decode('utf-8')
        if APITYPE == 'SesstionKey':
            jsonObj = json.loads(responseText)  # Convert to dict from json
            sessionID = jsonObj['data']['session']
            dataList.append(sessionID)
        if APITYPE == 'sensor':
            responseJson = json.loads(responseText)
            responseDataJson = responseJson['data']
            for j in range(len(responseDataJson['result_sets'][0]['rows'])):
                DL = []
                for k in range(len(responseDataJson['result_sets'][0]['rows'][j]['data'])):
                    DL.append(responseDataJson['result_sets'][0]['rows'][j]['data'][k])
                dataList.append(DL)
        returnList = {'resCode': resCode, 'dataList': dataList}
        logging.info('Tanium ' + APITYPE + ' Data API Call Success')
        logging.info('Tanium ' + APITYPE + ' Data API Response Code : ' + str(resCode))
        return returnList
    except ConnectionError as e:
        logging.warning('Tanium '+APITYPE+' Data API Call Error, Error Message : ' + str(e))
        

def vul_plug_in(SK, APITYPE) :
    try:
        logging.info('Tanium '+APITYPE+' Data INPUT Plug In : API')
        logging.info('Tanium '+APITYPE+' Data API Call Start')
        apiUrl = APIURL
        ContentType = "application/json"
        dict = {}
        dataList = [] 
        if APITYPE == 'SWV' :
            path = '/api/v2/result_data/saved_question/3626'
            urls = apiUrl + path
            logging.info('Tanium ' + APITYPE + ' Data API URL : ' + urls)
            headers = {'session': SK, 'Content-Type': ContentType}
            response = requests.request("GET", urls, headers=headers, verify=False)
            resCode = response.status_code
            logging.info('API Session Key Call Success, ' + 'Sesponse Status Code : ' + str(resCode))
            responseText = response.text
            jsonObj = json.loads(responseText)
            for i in jsonObj['data']['result_sets'][0]['rows'] :
                dict = {}
                for j in i['data'][0] :
                    if j['text'] == 'TSE-Error: No Sensor Definition for this Platform':
                        logging.info('ComputerID :  {} has {}'.format(i['cid'], j['text']))
                        continue
                    elif j['text'] == '[current result unavailable]' :
                        logging.info('ComputerID :  {} has {}'.format(i['cid'], j['text']))
                        continue
                    elif j['text'] == 'TSE-Error: Python is not available on this system.':
                        logging.info('ComputerID :  {} has {}'.format(i['cid'], j['text']))
                        continue
                    else :
                        dict = literal_eval(j['text'])
                    dict['cid'] = i['cid']
                    dataList.append(dict)
            returnList = {'resCode': resCode, 'dataList': dataList}
            logging.info('Tanium ' + APITYPE + ' Data API Call Success')
            logging.info('Tanium ' + APITYPE + ' Data API Response Code : ' + str(resCode))
        return returnList
    except ConnectionError as e:
        logging.warning('Tanium '+APITYPE+' Data API Call Error, Error Message : ' + str(e))
