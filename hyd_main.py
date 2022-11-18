from Core.Tanium import vul_plug_in as TPI
from Transform.Dataframe import vul_plug_in as VUL_TDFPI
from Output.DB.PS.Tanium import vul_plug_in as VUL_ODPI
from datetime import datetime
import urllib3
import json
import logging
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
waitingUse = SETTING['PROJECT']['WAITING']['USE']
waitingDate = SETTING['PROJECT']['WAITING']['DATE']
logFileDirectory = SETTING['LOG']['directory']
logFileName = SETTING['LOG']['fileName']
logFileFormat = SETTING['LOG']['fileFormat']
TU = SETTING['CORE']['Tanium']['USE']

VUL_USE = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['VUL']['USE']

def main() :
    if VUL_USE == "true" :
        VDF = VUL_TDFPI('', 'question')
        VUL_ODPI(VDF, 'question')
    else :
        TPI()

if __name__ == "__main__":
    today = datetime.today().strftime("%Y%m%d")
    logFile = logFileDirectory + logFileName + today + logFileFormat
    logFormat = '%(levelname)s, %(asctime)s, %(message)s'
    logDateFormat = '%Y%m%d%H%M%S'
    logging.basicConfig(filename=logFile, format=logFormat, datefmt=logDateFormat, level=logging.DEBUG)
    logging.info('Module Started')
    main()
    logging.info('Module Finished')