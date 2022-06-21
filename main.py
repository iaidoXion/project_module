from Collection.API.Auth import SessionKey
from Collection.API.Call.Asset import Data as AssetData
from Collection.API.Call.Sensor import Data as SensorData
from Collection.Extract.Asset import Daily as EAD
from Collection.Transform.API import AssetOrgDaily as TAOD
from Collection.Transform.Asset import Daily as TAD
from Collection.Transform.Statistics import Daily as TSD
from Analysis.Statistics import DailyCount as ASDC
from Collection.Load.Asset import Daily as LAD
from Collection.Load.Statistics import Daily as LSD


import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']

class mainclass :
    def __init__(self):
        self.sk = SessionKey()

    def Asset(self) :
        BADL = AssetData(self.sk)
        BSDL = SensorData(self.sk)
        ADTL = TAOD(BADL['dataList'],BSDL['dataList'])
        LAD(ADTL)


    def Statistics(self):
        EDL = EAD()
        TSDL = TAD(EDL)
        ASDCL = ASDC(TSDL)
        TSDL = TSD(ASDCL)
        LSD(TSDL)



def RunModule() :
    mc = mainclass()
    mc.Asset()
    mc.Statistics()

if __name__ == "__main__":
    #schedule.every().day.at("23:59").do(RunModule)
    RunModule()



