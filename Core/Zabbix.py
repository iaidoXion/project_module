from API.Zabbix import plug_in as IAPI
from Transform.Dataframe import zplug_in as ZDFPI
from Output.DB.PS.Zabbix import plug_in as ODPI
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
    if ZSoC == 'true':
        if ZSoIP == 'API':
            sk = IAPI('', 'SesstionKey', '')['dataList'][0]
            ZHDL = IAPI(sk, 'assetHost', '')
            ZIDL = IAPI(sk, 'assetItem', ZHDL['dataList'])
            ZBDL = IAPI(sk, 'asset', ZIDL['dataList'])

        if ZSoTP == "true":
            ZDFDL = ZDFPI(ZBDL, ZSoIP, 'source')

        if ZSoOP == 'DB':
            ODPI(ZDFDL, 'source')
