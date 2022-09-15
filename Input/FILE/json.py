import json
import time
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TSoIPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['Storage']
TSoIPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileName']
TSoIPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileType']


today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")

def plug_in() :
    try:
        FileFullName = TSoIPFS+TSoIPFNM+'2022-09-14_900'+TSoIPFT
        with open(FileFullName, encoding="UTF-8") as ADF:
            ADL = json.loads(ADF.read())
        df = ADL[0]['rows']
        return df
        """with open('data.json', encoding="UTF-8") as ADF:
            ADL = json.loads(ADF.read())
        df = ADL
        return df"""
        #print("time :", time.time() - start)
        #return df
        #with open(TSoIPFS + FileFullName, encoding="UTF-8") as ADF:
        #    ADL = json.loads(ADF.read())
        #AssetSelectL = ADL
        #print(len(AssetSelectL['dataList']))

        """AS = BS['asset']
        Storage = AS['Storage']
        FNM = AS['FileName'] + yesterday
        FT = AS['FileType']
        FileFullName = FNM + FT
        with open(Storage + FileFullName, encoding="UTF-8") as ADF:
            ADL = json.loads(ADF.read())
        AssetSelectL = ADL
        return AssetSelectL"""
    except :
        print('Asset Daily Table connection(Select) Failure')




