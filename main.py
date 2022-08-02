from Input.API import read as IAT
from Input.DB import read as IDT
from Input.ES import read as IEE
from Transform.Dataframe import dataframe as TDF
from Transform.Datalist import dataList as TDL
from Transform.Asset import Daily as TAD
from Transform.Statistics import Daily as TSD
from Analysis.Statistics import DailyCount as ASDC
from Output.DB import write as ODL
from Output.ES import write as OEL


from datetime import datetime, timedelta
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
    module_install_date = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
    #today = datetime.today().strftime("%Y-%m-%d")
    if sourceCollection == 'true' :
        if sourceInputPlugin == 'API' :
            sk = IAT('','Auth')
            BDL = IAT(sk, 'sensor')                                      # API Call
        elif sourceInputPlugin == 'ES' :
            print()
        if sourceTransformPlugin == "true" :
            TDFL = TDF(BDL, sourceInputPlugin, 'source')
        if sourceOutputPlugin == 'DB':
            print()
            #ODL(TDFL, 'asset')
        elif sourceOutputPlugin == 'ES':
            OEL(TDFL, 'asset')
            print()

    if statisticsCollection == 'true' :
        if statisticsWaitingUse == 'true' :
            if module_install_date == statisticsWaitingDate :
                logging.info(module_install_date)
            else:
                if statisticsInputPlugin == 'DB' :
                    EDL = IDT()
                elif statisticsInputPlugin == 'ES':
                    EDL = IEE()
                if statisticsTransformPlugin == 'true':
                    TSDL = TDF(EDL, statisticsInputPlugin, 'statistics')
                ASDCL = ASDC(TSDL)
                if statisticsOutputPlugin == 'DB':
                    TSDL = TSD(ASDCL)
                    ODL(TSDL, 'statistics')
                    """if statisticsTransformPlugin == 'true':
                        a = TDF(DL, 'today', 'asset', statisticsInputPlugin)
                        #print(a)"""



def RunModule() :
    #today = datetime.today().strftime("%Y%m%d%H%M%S")
    today = datetime.today().strftime("%Y%m%d")
    logFile = logFileDirectory + logFileName + today + logFileFormat
    logFormat = '%(levelname)s, %(asctime)s, %(message)s'
    logDateFormat = '%Y%m%d%H%M%S'
    logging.basicConfig(filename=logFile, format=logFormat, datefmt=logDateFormat, level=logging.DEBUG)
    logging.info('Module Started')
    main()
    logging.info('Module Finished')




if __name__ == "__main__":
    RunModule()



