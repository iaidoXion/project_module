from Input.API.Tanium import plug_in as IAPI
from Input.API.Tanium import vul_plug_in as HYAPI
from Input.DB.PS.Tanium import plug_in as IDPI
from Input.ES.Tanium import plug_in as IEPI
from Input.FILE.json import plug_in as IFJPI
from Transform.Dataframe import plug_in as TDFPI
from Transform.Dataframe import vul_plug_in as VUL_TDFPI
from Transform.Merge import plug_in as TMPI
from Transform.Datalist import plug_in as TDLPI
from Analysis.Statistics.GroupByCount import plug_in as ASDC
from Output.DB.PS.Tanium import plug_in as ODPI
from Output.DB.PS.Tanium import vul_plug_in as VUL_ODPI
from Output.ES.Tanium import plug_in as OEPI
from Output.FILE.json import plug_in as OFJPI
from Output.Report import plug_in as RP
from Analysis.Statistics.AlarmDetection import plug_in as AADP
from datetime import datetime, timedelta
import urllib3
import json
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
waitingUse = SETTING['PROJECT']['WAITING']['USE']
waitingDate = SETTING['PROJECT']['WAITING']['DATE']
# Source Data
TSoC = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['COLLECTION']
## Input Plug In
TSoIPAU = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['API']['USE']
TSoIPDBPSU = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['USE']
TSoIPESU = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['ES']['USE']
TSoIPFU = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['USE']
## Transform Plug In
TSoTP = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['Transform']
## Output Plug In
TSoOPDBPSU = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['DB']['PS']['USE']
TSoOPESU = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['ES']['USE']
TSoOPFU = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['USE']

# Statistics Data
TStC = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['COLLECTION']
## Input Plug In
# = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['API']['USE']
TStIPDBPSU = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['USE']
TStIPESU = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['ES']['USE']
## Transform Plug In
TStTP = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['Transform']
## Output Plug In
TStOPDBPSU = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['DB']['PS']['USE']
TStOPESU = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['ES']['USE']

# Report
RU = SETTING['REPORT']['USE']
RDU = SETTING['REPORT']['DAILY']['USE']


def plug_in():
    module_install_date = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
    if TSoC == 'true':
        if TSoIPAU == 'true':
            sk = IAPI('', 'SesstionKey')['dataList'][0]
            BDL = IAPI(sk, 'sensor')
            TSoIP = 'API'
        if TSoIPDBPSU == 'true':
            BDL = IDPI('tanium', 'source')
            TSoIP = 'DB'
        if TSoIPESU == 'true':
            BDL = IEPI('source')
            TSoIP = 'ES'
        if TSoIPFU == 'true':
            BDL = IFJPI()
            TSoIP = 'FILE'
        if TSoTP == "true":
            TDFDL = TDFPI(BDL, TSoIP, 'source')
        else:
            TDFDL = BDL
        if TSoOPDBPSU == 'true':
            ODPI(TDFDL, 'source')
        if TSoOPESU == 'true':
            OEPI(TDFDL, 'tanium', 'source')
        if TSoOPFU == 'true':
            OFJPI(TDFDL)

    if waitingUse == 'true':
        if module_install_date == waitingDate:
            logging.info(module_install_date)
        else:
            if TStC == 'true':
                if TStIPDBPSU == 'true':
                    SBDL = IDPI('tanium', 'statistics')
                    SDL = SBDL['dataList']
                    TStIP = 'DB'
                if TStIPESU == 'true':
                    SBDL = IEPI('statistics')
                    SDL = TMPI(SBDL)
                    TStIP = 'ES'
                if TStTP == 'true':
                    STDL = TDFPI(SDL, TStIP, 'statistics')

                ASDCL = ASDC(STDL)
                TSDL = TDLPI(ASDCL)
                if TStOPDBPSU == 'true':
                    ODPI(TSDL, 'statistics')
                if TStOPESU == 'ES':
                    OEPI(TSDL, 'statistics')

            if RU == 'true' :
                AADP(STDL)
                if RDU == 'true' :
                    RP('daily')


def vul_plug_in():
    sk = IAPI('', 'SesstionKey')['dataList'][0]
    SWV = HYAPI(sk, 'SWV')
    DF = VUL_TDFPI(SWV, 'SW')
    DB = VUL_ODPI(DF, 'vulnerability')


def report_plug_in(type):
    RP(type)
