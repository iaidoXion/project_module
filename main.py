from Input.API import tanium as IAT
from Input.DB import tanium as IDT
from Transform.Dataframe import dataframe as TDF
from Transform.Datalist import dataList as TDL
from Transform.Asset import Daily as TAD
from Transform.Statistics import Daily as TSD
from Analysis.Statistics import DailyCount as ASDC
from Output.Asset import Daily as LAD
from Output.Statistics import Daily as LSD

from datetime import datetime
import urllib3
import json
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

sourceCollection = SETTING['MODULE']['SOURCE']['COLLECTION']
sourceInputPlugin = SETTING['MODULE']['SOURCE']['PLUGIN']['INPUT']
sourceTransformPlugin = SETTING['MODULE']['SOURCE']['PLUGIN']['Transform']
sourceOutputPlugin = SETTING['MODULE']['SOURCE']['PLUGIN']['OUTPUT']

statisticsCollection = SETTING['MODULE']['STATISTICS']['COLLECTION']
statisticsWaitingUse = SETTING['MODULE']['STATISTICS']['WAITING']['USE']
statisticsWaitingDate = SETTING['MODULE']['STATISTICS']['WAITING']['DATE']
statisticsInputPlugin = SETTING['MODULE']['STATISTICS']['PLUGIN']['INPUT']
statisticsTransformPlugin = SETTING['MODULE']['STATISTICS']['PLUGIN']['Transform']
statisticsOutputPlugin = SETTING['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']


DataLoadingType = SETTING['MODULE']['DataLoadingType']
logFileDirectory = SETTING['LOG']['directory']
logFileName = SETTING['LOG']['fileName']
logFileFormat = SETTING['LOG']['fileFormat']
core = SETTING['PROJECT']['CORE']


def main() :
    today = datetime.today().strftime("%Y-%m-%d")
    if sourceCollection == 'true' :
        if sourceInputPlugin == 'API' :
            sk = IAT('','Auth')
            BADL = IAT(sk, 'Asset')                                       # Asset API Call
            BSDL = IAT(sk, 'sensor')                                      # Sensor API Call
        if sourceTransformPlugin == "true" :
            ADL = TDF(BADL, 'today', 'asset')
            SDL = TDF(BSDL, 'today', 'sensor')
            DL = [ADL,SDL]
            DTL = TDL(DL)
        #if sourceOutputPlugin == 'DB' :
            #LAD(DTL)

    if statisticsCollection == 'true' :
        if statisticsWaitingUse == 'true' :
            if today == statisticsWaitingDate :
                logging.info(today)
            else:
                if statisticsInputPlugin == 'DB' :
                    EDL = IDT()                                         # 어제 자산 데이터와 그제 자산 데이터
                elif statisticsInputPlugin == 'ES' :
                    print()

                if statisticsTransformPlugin == 'true' :
                    TSDL = TAD(EDL)                                     # 어제 자산 데이터와 그제 자산 데이터 병합 및 변환
                ASDCL = ASDC(TSDL)                                      # count
                #if statisticsTransformPlugin == 'true':
                if statisticsOutputPlugin == 'DB':
                    TSDL = TSD(ASDCL)
                    #LSD(TSDL)






def RunModule() :
    today = datetime.today().strftime("%Y%m%d%H%M%S")
    logFile = logFileDirectory + logFileName + today + logFileFormat
    logFormat = '%(levelname)s, %(asctime)s, %(message)s'
    logDateFormat = '%Y%m%d%H%M%S'
    logging.basicConfig(filename=logFile, format=logFormat, datefmt=logDateFormat, level=logging.DEBUG)
    logging.info('Module Started')
    main()
    logging.info('Module Finished')




if __name__ == "__main__":
    RunModule()



