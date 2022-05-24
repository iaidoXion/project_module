import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
apiUrl = SETTING['API']['apiUrl']
Authorization = SETTING['API']['Authorization']
ContentType = SETTING['API']['ContentType']


def Asset(sessionKey):
    sessionKey = sessionKey
    path = "/plugin/products/asset/v1/assets"
    urls = apiUrl + path
    headers = {
        'session': sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code

    assetText = response.text
    assetJson = json.loads(assetText)
    assetsCount = len(assetJson['data'])
    assetsDataJson = assetJson['data']

    dataListAppend = []
    for i in range(0, assetsCount):
        id = assetsDataJson[i]['id']
        computer_name = assetsDataJson[i]['computer_name']
        computer_id = assetsDataJson[i]['computer_id']
        os_platform = assetsDataJson[i]['os_platform']
        operating_system = assetsDataJson[i]['operating_system']
        disk_total_space = assetsDataJson[i]['disk_total_space']
        created_at = assetsDataJson[i]['created_at']
        updated_at = assetsDataJson[i]['updated_at']
        last_seen_at = assetsDataJson[i]['last_seen_at']
        ci_installed_application = assetsDataJson[i]['ci_installed_application']
        ram = assetsDataJson[i]['ram']
        city = assetsDataJson[i]['city']
        chassis_type = assetsDataJson[i]['chassis_type']

        data = {
            'id': id,
            'computer_name': computer_name,
            'computer_id': computer_id,
            'os_platform': os_platform,
            'operating_system': operating_system,
            'disk_total_space': disk_total_space,
            'created_at': created_at,
            'updated_at': updated_at,
            'last_seen_at': last_seen_at,
            'asset_item': chassis_type,
            'ci_installed_application': ci_installed_application
        }

        dataListAppend.append(data)


    dataList = dataListAppend
    returnList = {'resCode': resCode, 'dataList': dataList}

    return returnList
