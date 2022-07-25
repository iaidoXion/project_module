import pandas as pd

from Collection.API.Auth import SessionKey
from Collection.API.Call.Asset import data as AssetData
from Collection.API.Call.Sensor import data as SensorData
from Collection.API.Call.Group import Data as GroupData
from Collection.Extract.Asset import Daily as EAD
from Collection.Extract.Zabbix import Daily as EZD
from Collection.Transform.API import dataframe as TDF, dataList as TDL
from Collection.Transform.Asset import Daily as TAD
from Collection.Transform.Statistics import Daily as TSD
from Analysis.Statistics import DailyCount as ASDC
from Collection.Load.Asset import Daily as LAD
from Collection.Load.Statistics import Daily as LSD
from datetime import datetime
import urllib3
import json
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']
logFileDirectory = SETTING['LOG']['directory']
logFileName = SETTING['LOG']['fileName']
logFileFormat = SETTING['LOG']['fileFormat']
core = SETTING['PROJECT']['CORE']
moduleInstallDate = SETTING['MODULE']['InstallDate']

class mainclass :
    def __init__(self):
        self.sk = SessionKey()

    def Asset(self) :
        BADL = AssetData(self.sk)                                       # Asset API Call
        BSDL = SensorData(self.sk)                                      # Sensor API Call
        ADL = TDF(BADL, 'today', 'asset')
        SDL = TDF(BSDL, 'today', 'sensor')
        DL = [ADL,SDL]
        DTL = TDL(DL)
        LAD(DTL)


    def Statistics(self):
        today = datetime.today().strftime("%Y-%m-%d")
        if today == moduleInstallDate:
            logging.info(today)
        else:
            if core == 'Tanium':
                EDL = EAD()         # 어제 자산 데이터와 그제 자산 데이터
                TSDL = TAD(EDL)     # 어제 자산 데이터와 그제 자산 데이터 병합 및 변환
                ASDCL= ASDC(TSDL)   # count
                TSDL = TSD(ASDCL)
                LSD(TSDL)
            elif core == 'Zabbix':
                EDL = EZD()

def RunModule() :
    mc = mainclass()
    if core == 'Tanium' :
        mc.Asset()
        mc.Statistics()
    elif core == 'Zabbix' :
        mc.Statistics()

def Scheduling():
    today = datetime.today().strftime("%Y%m%d%H%M%S")
    logFile = logFileDirectory+logFileName+today+logFileFormat
    logFormat = '%(levelname)s, %(asctime)s, %(message)s'
    logDateFormat = '%Y%m%d%H%M%S'
    logging.basicConfig(filename=logFile, format=logFormat, datefmt=logDateFormat, level=logging.DEBUG)
    logging.info('Module Started')
    RunModule()
    logging.info('Module Finished')

if __name__ == "__main__":
    """
    schedule.every(3).seconds.do(Scheduling)
    schedule.every().day.at("00:00:00").do(Scheduling)
    while True:
        schedule.run_pending()
        time.sleep(1)"""
    Scheduling()



