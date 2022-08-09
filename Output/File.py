import psycopg2
import json
import logging
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

BS = SETTING['FILE']
today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")


def plug_in(data, dataType) :
    try:
        SB = {'data': data}
        AS = BS['asset']
        Storage = AS['Storage']
        FNM = AS['FileName'] + today
        FT = AS['FileType']
        FileFullName = FNM + FT
        with open(Storage + FileFullName, 'w') as ADOF:
            json.dump(SB, ADOF)
        ADOF.close()
    except :
        print('Asset Daily Table connection(Insert) Failure')
