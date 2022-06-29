import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
apiUrl = SETTING['API']['apiUrl']
Authorization = SETTING['API']['Authorization']
ContentType = SETTING['API']['ContentType']
AssetPath = SETTING['API']['PATH']['Asset']

def Data(SK):
    path = '/api/v2/action_groups'
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
    assetsCount = len(assetJson['data'])
    assetsDataJson = assetJson['data']
    #print(assetsDataJson)
    """dataListAppend = []
    for i in range(0, assetsCount):
        id = assetsDataJson[i]['id']
        computer_name = assetsDataJson[i]['computer_name']
        computer_id = assetsDataJson[i]['computer_id']
        os_platform = assetsDataJson[i]['os_platform']
        operating_system = assetsDataJson[i]['operating_system']
        drive_use_size = str(assetsDataJson[i]['ci_logical_disk'][0]['free_space'])
        created_at = assetsDataJson[i]['created_at']
        updated_at = assetsDataJson[i]['updated_at']
        last_seen_at = assetsDataJson[i]['last_seen_at']
        ci_installed_application = assetsDataJson[i]['ci_installed_application']
        chassis_type = assetsDataJson[i]['chassis_type']
        ip_address = assetsDataJson[i]['ip_address']
        asset_serial_number = assetsDataJson[i]['serial_number']
        asset_manufacturer = assetsDataJson[i]['manufacturer']
        asset_model_name = assetsDataJson[i]['model']
        asset_domain_name = assetsDataJson[i]['domain_name']
        ram_total_size = assetsDataJson[i]['ram']
        disk_total_space = assetsDataJson[i]['disk_total_space']
        system_uuid = assetsDataJson[i]['system_uuid']
        cpu_name = assetsDataJson[i]['cpu_name']
        cpu_speed = assetsDataJson[i]['cpu_speed']
        cpu_processor = assetsDataJson[i]['cpu_processor']
        cpu_core = assetsDataJson[i]['cpu_core']
        user_name = assetsDataJson[i]['user_name']
        os_version = assetsDataJson[i]['os_version']
        cpu_manufacturer = assetsDataJson[i]['cpu_manufacturer']
        if assetsDataJson[i]['ci_physical_disk'] != None :
            drive_serial_number = assetsDataJson[i]['ci_physical_disk'][0]['serial_number']
            drive_manufacturer = assetsDataJson[i]['ci_physical_disk'][0]['manufacturer']
            drive_model_name = assetsDataJson[i]['ci_physical_disk'][0]['model']
        else :
            drive_serial_number = '-'
            drive_manufacturer = '-'
            drive_model_name = '-'
        mac_address = assetsDataJson[i]['ci_network_adapter'][0]['mac_address']


        data = {
            'id': id,
            'computer_name': computer_name,
            'computer_id': computer_id,
            'os_platform': os_platform,
            'operating_system': operating_system,
            'drive_use_size': drive_use_size,
            'created_at': created_at,
            'updated_at': updated_at,
            'last_seen_at': last_seen_at,
            'asset_item': chassis_type,
            'ci_installed_application': ci_installed_application,
            'ip_address' : ip_address,
            'asset_serial_number' : asset_serial_number,
            'asset_manufacturer' : asset_manufacturer,
            'asset_model_name': asset_model_name,
            'asset_domain_name': asset_domain_name,
            'ram_total_size': ram_total_size,
            'disk_total_space': disk_total_space,
            'system_uuid': system_uuid,
            'cpu_name': cpu_name,
            'cpu_speed': cpu_speed,
            'cpu_processor': cpu_processor,
            'cpu_core': cpu_core,
            'user_name': user_name,
            'os_version': os_version,
            'cpu_manufacturer': cpu_manufacturer,
            'drive_serial_number': drive_serial_number,
            'drive_manufacturer': drive_manufacturer,
            'drive_model_name': drive_model_name,
            'mac_address': mac_address,
        }

        dataListAppend.append(data)


    dataList = dataListAppend
    returnList = {'resCode': resCode, 'dataList': dataList}

    return returnList"""


