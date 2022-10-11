import ujson as json
import time
import teradata
import os
from datetime import datetime, timedelta

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TSoIPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['Storage']
TSoIPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileName']
TSoIPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileType']

TSoOPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['Storage']
TSoOPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['FileName']
TSoOPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['FileType']
TSoOPCS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['chunkSize']


#16메가로 자른 파일을 Teradata에 직접적재
#NOS를 이용하기 때문에 현재는 불필요

#테라데이터 정보
host='192.168.1.140'
username='xion11'
password='xion11'


def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + " "
    return result.strip()

def plug_in() :
    file = os.listdir(TSoOPFS)
    filecount = len(file)

    udaExec = teradata.UdaExec(appName="test", version="1.0", logConsole=False)
    with udaExec.connect(method="odbc", system=host, username=username,
                         password=password, driver="Teradata Database ODBC Driver 17.20") as connect:

        for i in range(0, filecount):
            with open(TSoOPFS + TSoOPFNM + str(i) + TSoOPFT, 'r', encoding="utf-8") as inputfile:
                data=json.load(inputfile)
                print(TSoOPFNM+"%d 파일을 열었습니다." %i)
                for x in range(0,len(data['rows'])):
                    id = str(data['rows'][x]['id'])
                    cid = str(data['rows'][x]['cid'])
                    list = []
                    for y in range(0, len(data['rows'][x]['data'])):
                        text = data['rows'][x]['data'][y][0]['text'].replace('$','/')
                        list.append(text)
                        result = listToString(list)
                    query = """INSERT INTO xion11.Teratest(id, cid, info)VALUES ("""+id+""", """+cid+""",'"""+result+"""'); """
                    connect.execute(query)