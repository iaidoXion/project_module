from API.Zabbix import plug_in as IAPI
from Transform.Dataframe import zplug_in as ZDFPI
from Output.DB.PS.Tanium import plug_in as ODPI
from datetime import datetime, timedelta
import urllib3
import json
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
waitingUse = SETTING['PROJECT']['WAITING']['USE']
waitingDate = SETTING['PROJECT']['WAITING']['DATE']
ZSoC = SETTING['CORE']['Zabbix']['MODULE']['SOURCE']['COLLECTION']
ZSoIP = SETTING['CORE']['Zabbix']['MODULE']['SOURCE']['PLUGIN']['INPUT']
ZSoTP = SETTING['CORE']['Zabbix']['MODULE']['SOURCE']['PLUGIN']['Transform']
ZSoOP = SETTING['CORE']['Zabbix']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']
ZStC = SETTING['CORE']['Zabbix']['MODULE']['STATISTICS']['COLLECTION']
ZStIP = SETTING['CORE']['Zabbix']['MODULE']['STATISTICS']['PLUGIN']['INPUT']
ZStTP = SETTING['CORE']['Zabbix']['MODULE']['STATISTICS']['PLUGIN']['Transform']
ZStOP = SETTING['CORE']['Zabbix']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']

def plug_in() :
    module_install_date = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
    if ZSoC == 'true':
        if ZSoIP == 'API':
            sk = IAPI('', 'SesstionKey', '')['dataList'][0]
            ZHDL = IAPI(sk, 'assetHost', '')
            ZIDL = IAPI(sk, 'assetItem', ZHDL['dataList'])
            ZBDL = IAPI(sk, 'asset', ZIDL['dataList'])

        if ZSoTP == "true":
            ZDFDL = ZDFPI(ZBDL, ZSoIP, 'source')

        if ZSoOP == 'DB':
            ODPI(ZDFDL, 'zabbix', 'source')
    """
    # 일단은 사용안함
    if ZStC == 'true':
        if waitingUse == 'true':
            if module_install_date == waitingDate:
                logging.info(module_install_date)
            else:
                if ZStIP == 'DB':
                    SBDL = IDPI()
                    SDL = SBDL
                elif ZStIP == 'ES':
                    SBDL = IEPI()
                    SDL = TMPI(SBDL)

                if ZStTP == 'true':
                    TSDL = TDFPI(SDL, TStIP, 'statistics')

                ASDCL = ASDC(TSDL)
                TSDL = TDLPI(ASDCL)

                if ZStOP == 'DB':
                    ODPI(TSDL, 'zabbix', 'statistics')
                elif ZStOP == 'ES':
                    OEPI(TSDL, 'statistics')
    """


