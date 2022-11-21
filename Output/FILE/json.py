import json
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TSoOPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['Storage']
TSoOPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['FileName']
TSoOPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['FileType']

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")


def plug_in() :
    try:
        with open('data/asset/daily/input/data.json') as infile:
            data = json.load(infile)
        ddd = data['rows']*16000
        data['rows'] = ddd
        FNM = 'data/asset/daily/input/data_480000..json'
        with open(FNM, 'w', encoding="UTF-8") as ADOF:
            json.dump(data, ADOF)
        ADOF.close()

        """FNM = TSoOPFNM+today+'_test_1'+TSoOPFT

        with open(TSoOPFS + FNM, 'w') as ADOF:
            json.dump(data, ADOF)
        ADOF.close()"""

        """dataList = []
        for i in range(10000) :
            dataList.append(data['dataList'])
        SB = {'dataList': dataList}
        with open(TSoOPFS + FNM, 'w') as ADOF:
            json.dump(SB, ADOF)
        ADOF.close()"""
        """SB = {'data': data}
        AS = BS['asset']
        Storage = AS['Storage']
        FNM = AS['FileName'] + today
        FT = AS['FileType']
        FileFullName = FNM + FT
        with open(Storage + FileFullName, 'w') as ADOF:
            json.dump(SB, ADOF)
        ADOF.close()"""
    except :
        print('Asset Daily Table connection(Insert) Failure')
