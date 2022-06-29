import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
apiUrl = SETTING['API']['apiUrl']
Authorization = SETTING['API']['Authorization']
ContentType = SETTING['API']['ContentType']
SensorPath = SETTING['API']['PATH']['Sensor']
SensorID = SETTING['API']['SensorID']

def Data(SK) :
    path = SensorPath+SensorID
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
    columnsList = assetsDataJson['result_sets'][0]['columns']
    dataList = assetsDataJson['result_sets'][0]['rows']
    columnsListAppend = []
    for i in range(len(columnsList)) :
        columnsName = assetsDataJson['result_sets'][0]['columns'][i]['name']
        columnsListAppend.append(columnsName)
        #print(columnsName)
    dataListAppend = []
    for j in range(len(dataList)) :
        DL = []
        for k in range(len(dataList[j]['data'])) :
            DL.append(dataList[j]['data'][k][0]['text'])
        #print(DL)
        dataListAppend.append(DL)
    returnList = {'resCode': resCode, 'dataList': dataListAppend, 'dataColumnList': columnsListAppend}

    return returnList

