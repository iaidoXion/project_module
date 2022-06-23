import requests
import json
import logging

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
SesstionKeyPath = APISETTING['API']['PATH']['SesstionKey']

def SessionKey():
    try :
        logging.info('API Session Key Call Start')
        path = SesstionKeyPath
        urls = apiUrl+path
        headers = {
          'Authorization': Authorization
        }
        response = requests.request("GET", urls, headers=headers, verify=False)
        resCode = response.status_code
        sessionKey = response.text
        returnList = sessionKey
        logging.info('API Session Key Call Success, ' + 'Status Code : '+str(resCode))
        logging.info('API Session Key : '+returnList)
        return returnList
    except ConnectionError as e:
        logging.warning('API Session Key Call Error, Error Message : ' + str(e))

