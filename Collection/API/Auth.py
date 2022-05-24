import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
def SessionKey():
    path = "/auth"
    urls = apiUrl+path
    headers = {
      'Authorization': Authorization
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    sessionKey = response.text


    #dataList = sessionKey
    returnList = sessionKey

    return returnList

