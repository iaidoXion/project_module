from Collection.API.Auth import SessionKey
from Collection.API.Extract import Asset as AssetAPI
from Collection.Transform import AssetOrgDaily as TAOD
from Collection.Load import AssetDaily as LAD
from Collection.Extract import AssetDaily as EAD
from Collection.Transform import AssetDaily as TAD
from Analysis.Statistics import DailyCount as ASDC
from Collection.Transform import StatisticsDaily as TSD
from Collection.Load import StatisticsDaily as LSD

import urllib3
import json
import schedule

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']

class mainclass :
    def __init__(self):
        self.sk = SessionKey()

    def Asset(self) :
        baseAssetData = AssetAPI(self.sk)
        AssetData = TAOD(baseAssetData['dataList'])
        LAD(AssetData)


    def Statistics(self):
        EDL = EAD()
        TSDL = TAD(EDL)
        ASDCL = ASDC(TSDL)
        TSDL = TSD(ASDCL)
        LSD(TSDL)

    #def DriveUse(self):


def RunModule() :
    mc = mainclass()
    mc.Asset()
    mc.Statistics()

if __name__ == "__main__":
    #schedule.every().day.at("23:59").do(RunModule)
    RunModule()



