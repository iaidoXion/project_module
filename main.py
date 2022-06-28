from Collection.API.Auth import SessionKey
from Collection.API.Call.Asset import Data as AssetData
from Collection.API.Call.Sensor import Data as SensorData
from Collection.Extract.Asset import Daily as EAD
from Collection.Transform.API import AssetOrgDaily as TAOD
from Collection.Transform.Asset import Daily as TAD
from Collection.Transform.Statistics import Daily as TSD
from Analysis.Statistics import DailyCount as ASDC, Association as ASA
from Collection.Load.Asset import Daily as LAD
from Collection.Load.Statistics import Daily as LSD
from datetime import datetime
import urllib3
import json
import schedule
import time
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
today = datetime.today().strftime("%Y%m%d")
logDateTime = datetime.today().strftime("%Y%m%d%H%M%S")
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']
logFileDirectory = SETTING['LOG']['directory']
logFileName = SETTING['LOG']['fileName']
logFileFormat = SETTING['LOG']['fileFormat']

class mainclass :
    def __init__(self):
        self.sk = SessionKey()

    def Asset(self) :
        BADL = AssetData(self.sk)
        BSDL = SensorData(self.sk)
        ADTL = TAOD(BADL['dataList'],BSDL['dataList'])
        #print(ADTL)
        LAD(ADTL)

    def Statistics(self):
        EDL = EAD()         # 어제 자산 데이터와 그제 자산 데이터
        TSDL = TAD(EDL)     # 어제 자산 데이터와 그제 자산 데이터 병합 및 변환
        ASDCL= ASDC(TSDL)   # count
        #ASA(ASDCL)
        TSDL = TSD(ASDCL)
        #LSD(TSDL)

def RunModule() :
    mc = mainclass()
    mc.Asset()
    mc.Statistics()

def Scheduling():
    logFile = logFileDirectory+logFileName+today+logFileFormat
    logFormat = '%(levelname)s, %(asctime)s, %(message)s'
    logDateFormat = '%Y%m%d%H%M%S'
    logging.basicConfig(filename=logFile, format=logFormat, datefmt=logDateFormat, level=logging.DEBUG)
    logging.info('Module Started')
    RunModule()
    logging.info('Module Finished')

if __name__ == "__main__":
    #schedule.every(3).seconds.do(job)
    #schedule.every().day.at("23:59:59").do(Scheduling)
    #while True:
        #schedule.run_pending()
        #    time.sleep(1)
    Scheduling()



