from datetime import datetime
import urllib3
import json
import logging
from Core.Tanium import report_plug_in as RPI
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
logFileDirectory = SETTING['LOG']['directory']
logFileName = SETTING['LOG']['fileName']
logFileFormat = SETTING['LOG']['fileFormat']
RU = SETTING['REPORT']['USE']
RDU = SETTING['REPORT']['DAILY']['USE']

def main() :
    if RU == 'true' :
        if RDU == 'true' :
            RPI('daily')

if __name__ == "__main__":
    today = datetime.today().strftime("%Y%m%d")
    logFile = logFileDirectory + logFileName + today + logFileFormat
    logFormat = '%(levelname)s, %(asctime)s, %(message)s'
    logDateFormat = '%Y%m%d%H%M%S'
    logging.basicConfig(filename=logFile, format=logFormat, datefmt=logDateFormat, level=logging.DEBUG)
    logging.info('Daily Report Module Started')
    main()
    logging.info('Daily Report Module Finished')