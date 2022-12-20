import requests
import json
import urllib3
import logging
from ast import literal_eval
from pprint import pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

APIURL = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['URL']
SKPATH = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['PATH']['SesstionKey']
SPATH = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['PATH']['Sensor']
SID = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['SensorID']
APIUNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['username']
APIPWD = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['password']

# VUl
VUL_SID = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['VUL']['SensorID']


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
        list_dict = {}
        dict_list = []
        dataList = []
        for_list = ['SW1', 'SW2', 'SW2_2', 'SW2-3', 'SW2_4', 'SW3', 'SW4', 'SW4_2']
        chekc_swv = [20, 42, 9, 24]
        if APITYPE == 'SWV' :
            path = SPATH + VUL_SID
            headers = {'session': SK, 'Content-Type': ContentType}
            urls = apiUrl + path
            logging.info('Tanium ' + APITYPE + ' Data API URL : ' + urls)
            headers = {'session': SK, 'Content-Type': ContentType}
            response = requests.request("GET", urls, headers=headers, verify=False)
            resCode = response.status_code
            logging.info('API Session Key Call Success, ' + 'Sesponse Status Code : ' + str(resCode))
            responseText = response.text
            jsonObj = json.loads(responseText)
            data = jsonObj['data']['result_sets'][0]['rows']
            for i in range(len(data)) :
                dict = {}
                dict_list = []
                list_dict = {}
                count = 0
                
                SWV_list = []
                for i, cdata in enumerate(chekc_swv) :
                    for j in range(cdata) :
                        SWV_list.append('SW' + str(i+1) + '-' + str(j + 1).zfill(2))
                for k in range(len(for_list)) :
                    count = count + 1
                    for j in data[i]['data'][k] :
                        if j['text'] == 'TSE-Error: No Sensor Definition for this Platform':
                            logging.info('ComputerID :  {} has {}'.format(data[i]['cid'], j['text']))
                            continue
                        if j['text'] == 'TSE-Error: Python is disabled':
                            logging.info('ComputerID :  {} has {}'.format(data[i]['cid'], j['text']))
                            continue
                        elif j['text'] == '[current result unavailable]' :
                            logging.info('ComputerID :  {} has {}'.format(data[i]['cid'], j['text']))
                            continue
                        elif j['text'] == 'TSE-Error: Python is not available on this system.':
                            logging.info('ComputerID :  {} has {}'.format(data[i]['cid'], j['text']))
                            continue
                        else :
                            if j['text'] == 'TSE-Error: Failed to send to sensor child process: broken pipe' :
                                dict['SWV'] = for_list[k]
                                dict['value'] = j['text']
                                j['text'] = dict
                            else :
                                if not j['text'].startswith('{') and not j['text'].endswith('}'):
                                    j['text'] = '{' + j['text'] + '}'
                                dict = literal_eval(j['text'])
                                SWV_list.remove(dict['SWV'])
                            dict_list.append(dict)
                    if len(for_list) == count : 
                        if not len(SWV_list) == 0 :
                            for index in SWV_list :
                                sub_dict = {}
                                sub_dict['SWV'] = index
                                sub_dict['status'] = 'None'
                                sub_dict['value'] = 'None'
                                dict_list.append(sub_dict)
                    if len(dict_list) != 0 :
                        list_dict['list'] = dict_list
                        list_dict['cid'] = data[i]['data'][8][0]['text'] #computer_id
                        list_dict['cpn'] = data[i]['data'][9][0]['text'] #computer_name
                        list_dict['os'] = data[i]['data'][10][0]['text'] #Operating System
                        list_dict['ip'] = data[i]['data'][11][0]['text'] #Tanium Client NAT IP Address
                        list_dict['ct'] = data[i]['data'][12][0]['text'] #Chassis Type
                        list_dict['lr'] = data[i]['data'][13][0]['text'] #Last Reboot
                        list_dict['online'] = data[i]['data'][14][0]['text']
                if len(list_dict) != 0 :
                    dataList.append(list_dict)
            for i in range(len(dataList)) :
                dataList[i]['list'] = sorted(dataList[i]['list'], key= lambda x: x['SWV'])
            returnList = {'resCode': resCode, 'dataList': dataList}
            logging.info('Tanium ' + APITYPE + ' Data API Call Success')
            logging.info('Tanium ' + APITYPE + ' Data API Response Code : ' + str(resCode))
        return returnList
    except ConnectionError as e:
        logging.warning('Tanium '+APITYPE+' Data API Call Error, Error Message : ' + str(e))
