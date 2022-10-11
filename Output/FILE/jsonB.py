import ujson as json
from datetime import datetime, timedelta

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TSoOPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['Storage']
TSoOPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['FileName']
TSoOPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['FileType']
TSoOPCS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['chunkSize']
today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")

def plug_in(readData) :
    try:
        startFormat = '{"rows":'
        endFormat = "}"
        chunkSize = TSoOPCS
        for i in range(0, len(readData['rows']), chunkSize):
            print(i)
            with open(TSoOPFS + TSoOPFNM + str(i // chunkSize) + TSoOPFT, 'w') as outfile:
                outfile.write(startFormat)
                json.dump(readData['rows'][i:i + chunkSize], outfile)
                outfile.write(endFormat)
    except :
        print('Asset Daily Table connection(Insert) Failure')
