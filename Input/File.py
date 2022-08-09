import psycopg2
import json
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
BS = SETTING['FILE']
today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")

def plug_in() :
    try:
        AS = BS['asset']
        Storage = AS['Storage']
        FNM = AS['FileName'] + yesterday
        FT = AS['FileType']
        FileFullName = FNM + FT
        with open(Storage + FileFullName, encoding="UTF-8") as ADF:
            ADL = json.loads(ADF.read())
        AssetSelectL = ADL
        return AssetSelectL
    except :
        print('Asset Daily Table connection(Select) Failure')




