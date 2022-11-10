import psycopg2
import json
import logging
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

ZU = SETTING['CORE']['Zabbix']['USE']
ZDBHost = SETTING['CORE']['Zabbix']['DB']['HOST']
ZDBPort = SETTING['CORE']['Zabbix']['DB']['PORT']
ZDBName = SETTING['CORE']['Zabbix']['DB']['DBName']
ZDBUser = SETTING['CORE']['Zabbix']['DB']['DBUser']
ZDBPwd = SETTING['CORE']['Zabbix']['DB']['DBPwd']
ZATNM = SETTING['CORE']['Zabbix']['DB']['AssetTNM']
ZStTNM = SETTING['CORE']['Zabbix']['DB']['StatisticsTNM']

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")


def plug_in(data, dataType) :
    try:
        logging.info('Zabbix '+dataType+' Data OUTPUT Plug In : DB')
        logging.info('Zabbix ' + dataType + ' Data Table connection(Insert) Start')
        DBHost = ZDBHost
        DBPort = ZDBHost
        DBName = ZDBName
        DBUser = ZDBUser
        DBPwd = ZDBPwd
        if dataType == 'source':
            TNM = ZATNM

        logging.info('Insert Data Type : '+dataType)
        logging.info('Databases Host : ' + DBHost)
        logging.info('Databases Name : ' + DBName)
        logging.info('Databases User : ' + DBUser)
        logging.info('Databases PWD : ' + DBPwd)
        insertConn = psycopg2.connect('host={0} port={1} dbname={2} user={3} password={4}'.format(DBHost, DBPort, DBName, DBUser, DBPwd))
        insertCur = insertConn.cursor()

        if dataType == 'source':
            IQ = """ INSERT INTO """ + TNM + """ (zabbix_asset_num, zabbix_name, zabbix_description, zabbix_ip, zabbix_up_time, zabbix_process_num, zabbix_disk_used, zabbix_mem_used, zabbix_cpu_used, zabbix_agent_ver, zabbix_agent_run, zabbix_asset_date) VALUES (nextval('seq_zabbix_asset'), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '""" + yesterday + """ 23:59:59""" + """');"""
            datalen = len(data.zabbix_name)

        logging.info('Table Name : ' + TNM)
        logging.info('Insert Data Count : ' + str(datalen))
        for i in range(datalen):
            if dataType == 'source':
                HN = data.zabbix_name[i]
                OS = data.zabbix_description[i]
                IP = data.zabbix_ip[i]
                UT = data.zabbix_up_time[i]
                PN = data.zabbix_process_num[i]
                DU = data.zabbix_disk_used[i]
                MU = data.zabbix_mem_used[i]
                CU = data.zabbix_cpu_used[i]
                AV = data.zabbix_agent_ver[i]
                AR = data.zabbix_agent_run[i]
                dataList = HN, OS, IP, UT, PN, DU, MU, CU, AV, AR
            insertCur.execute(IQ, (dataList))
        insertConn.commit()
        insertConn.close()
    except ConnectionError as e:
        logging.warning('Zabbix '+ dataType + 'Data Insert Connection Failure : ' + str(e))
