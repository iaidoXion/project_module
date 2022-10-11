import ujson as json
from datetime import datetime, timedelta

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TSoIPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['Storage']
TSoIPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileName']
TSoIPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileType']

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")

def plug_in():
    try:
        with open(TSoIPFS + TSoIPFNM + TSoIPFT) as infile:
            readData = json.load(infile)
        return readData
    except:
        print('Asset Daily Table connection(Select) Failure')