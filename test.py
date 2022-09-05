# If requests module is missing type this in the python console:
# pip install requests
import requests
import json
import time
import getpass
import urllib

class dataClass:
    def __init__(self):
        self.username = ""
        self.domain = ""
        self.password = ""

    def SetUserNamePassword(self):
        self.username = 'administrator'
        self.password = 'xion123!'


class demoClass:
    def __init__(self):
        self.sessionID=""
        self.sessionHeader={"session":""}
        self.TaniumServer="https://192.168.5.100"


    def setSessionId(self):
        url = self.TaniumServer + "/api/v2/session/login"
        dc = dataClass()
        dc.SetUserNamePassword()
        authJSON = '{"username": "administrator", "domain": "", "password": "xion123!"}'
        response = requests.post(url, data=authJSON, verify=False)
        jsonOut = response.content.decode('utf-8') #Convert from byte array to string
        jsonObj = json.loads(jsonOut)   # Convert to dict from json
        self.sessionID = jsonObj['data']['session']
        self.sessionHeader = {"session":self.sessionID}
        print(self.sessionHeader )
        print("*** Session Header is:", self.sessionHeader)

    def sessionKey(self):
        url = self.TaniumServer + "/auth"
        headers = {'Authorization': 'Basic QWRtaW5pc3RyYXRvcjp4aW9uMTIzIQ=='}
        response = requests.request("GET", url, headers=headers, verify=False)
        self.responseText = response.content.decode('utf-8')
        self.sessionHeader = {"session": self.responseText}

    def issueQuestionAndGetID(self,questionText):
        url = self.TaniumServer + "/api/v2/questions?json_pretty_print=1"

        # Caution sensor hash should match actual sensor else you wildl get Error
        jsonText = '{ "question_text" :"' + questionText +'",' + \
                    '"selects" : [' + \
              '{"group" : {"and_flag" : false,"deleted_flag" : false, "filters" : [],"not_flag" : false, "sub_groups" : []},' + \
              '"sensor" : {"hash" : 3409330187, "name" : "Computer Name"}}],' + \
            '"sensor_references" : [{"name" : "computer name","start_char" : "4"}]}"'
        response = requests.post(url, data=jsonText, headers=self.sessionHeader,verify=False)
        jsonOut = response.content.decode('utf-8')  # Convert from byte array to string
        jsonObj = json.loads(jsonOut)  # Convert to dict from json
        questionID = jsonObj['data']['id']
        return questionID

    def getResultForQuestionId(self, questionID):
        url = self.TaniumServer + "/api/v2/result_data/question/" + str(questionID)
        response = requests.post(url, headers=self.sessionHeader,verify=False)
        questionResults = response.content.decode('utf-8')  # Convert from byte array to string
        return questionResults


    def getSensorHash(self,sensorName):
        # Convert to http encoding
        sensorName = urllib.parse.quote(sensorName)
        url = self.TaniumServer + "/api/v2/sensors/by-name/" + sensorName
        response = requests.get(url, headers=self.sessionHeader, verify=False)
        jsonOut = response.content.decode('utf-8')  # Convert from byte array to string
        jsonObj = json.loads(jsonOut)  # Convert to dict from json
        sensorHash = jsonObj['data']['hash']
        return sensorHash

    def logOut(self):
        url = self.TaniumServer + "/api/v2/session/logout"
        sessionJSON = json.dumps(self.sessionHeader)
        response = requests.post(url, data=sessionJSON , verify=False)
        jsonOut = response.content.decode('utf-8')
        if response.status_code == 200:
            return True
        else:
            return False

# main() function which contain the high level routines
def main():
    dc = demoClass()
    dc.setSessionId()
    #sensorHash = dc.getSensorHash("IP Address")
    #print('Sensor hash', sensorHash)

    questionId  = dc.issueQuestionAndGetID("Get computer name from all machines")
    #Wait for some time while question results become available
    print('Waiting for the Tanium server to pull results for question id:', str(questionId), '...') #This can be in Async call
    time.sleep(20)  # 15-25 seconds is generally sufficient to pull data from most endpoints
    results = dc.getResultForQuestionId(questionId)
    # let us log out of the session
    if dc.logOut() == True:
        print("logout successful")
    else:
        print("logout failed")

    #print("Question results in JSON:", results)
    jsonObj = json.loads(results)
    noOfItems = int(jsonObj['data']['result_sets'][0]['item_count'])
    print('Number of items',noOfItems)
    print('List of Computer name(s) returned from Tanium Server:')
    for idx in range(0, noOfItems):
        computerNames = jsonObj['data']['result_sets'][0]['rows'][idx]['data'][0][0]['text']
        print(computerNames)

# Call the main() function
main()
