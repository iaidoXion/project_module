from Input.API import plug_in as IAPI
from Input.DB import plug_in as IDPI
from Input.ES import plug_in as IEPI
from Transform.Dataframe import plug_in as TDFPI
from Transform.Merge import plug_in as TMPI
from Transform.Datalist import plug_in as TDLPI
from Analysis.Statistics import DailyCount as ASDC
from Output.DB import plug_in as ODPI
from Output.ES import plug_in as OEPI
from datetime import datetime, timedelta
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
TSoC = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['COLLECTION']
TSoIP = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']
TSoTP = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['Transform']
TSoOP = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']
TStC = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['COLLECTION']
TStIP = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']
TStTP = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['Transform']
TStOP = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']

def main() :
    module_install_date = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
    if TU == 'true' :
        if TSoC == 'true' :
            if TSoIP == 'API' :
                sk = IAPI('','SesstionKey')['dataList'][0]
                BDL = IAPI(sk, 'sensor')
            elif TSoIP == 'ES' :
                print()
            if TSoTP == "true" :
                TDFDL = TDFPI(BDL, TSoIP, 'source')

            if TSoOP == 'DB':
                ODPI(TDFDL, 'source')
            elif TSoOP == 'ES':
                OEPI(TDFDL, 'source')

        if TStC == 'true' :
            if waitingUse == 'true' :
                if module_install_date == waitingDate :
                    logging.info(module_install_date)
                else:
                    if TStIP == 'DB' :
                        SBDL = IDPI()
                        SDL = SBDL
                    elif TStIP == 'ES':
                        SBDL = IEPI()
                        SDL = TMPI(SBDL)

                    if TStTP == 'true':
                        TSDL = TDFPI(SDL, TStIP, 'statistics')

                    ASDCL = ASDC(TSDL)
                    TSDL = TDLPI(ASDCL)

                    if TStOP == 'DB':
                        ODPI(TSDL, 'statistics')
                    elif TStOP == 'ES':
                        OEPI(TSDL, 'statistics')

if __name__ == "__main__":
    today = datetime.today().strftime("%Y%m%d")
    logFile = logFileDirectory + logFileName + today + logFileFormat
    logFormat = '%(levelname)s, %(asctime)s, %(message)s'
    logDateFormat = '%Y%m%d%H%M%S'
    logging.basicConfig(filename=logFile, format=logFormat, datefmt=logDateFormat, level=logging.DEBUG)
    logging.info('Module Started')
    main()
    logging.info('Module Finished')