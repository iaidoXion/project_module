import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
apiUrl = SETTING['API']['apiUrl']
Authorization = SETTING['API']['Authorization']
ContentType = SETTING['API']['ContentType']

def Data(SK) :
    path = "/api/v2/result_data/saved_question/797"
    #path = "/api/v2/saved_questions"
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
    dataListAppend = []
    for j in range(len(dataList)) :
        DL = []
        for k in range(len(dataList[j]['data'])) :
            #print(len(dataList[j]['data']))
            DL.append(dataList[j]['data'][k][0]['text'])
        dataListAppend.append(DL)
    returnDataList = []
    #for m in range(len(dataListAppend)) :
    #    DTL = []
    #    for l in  range(len(columnsListAppend)) :
    #        DTL.append({columnsListAppend[l] : dataListAppend[m][l]})
    #    returnDataList.append(DTL)
    #print(returnDataList)
    #print(columnsListAppend)
    #print(columnsListAppend)
    returnList = {'resCode': resCode, 'dataList': dataListAppend, 'dataColumnList': columnsListAppend}

    return returnList

