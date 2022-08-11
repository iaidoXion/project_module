import psycopg2
import json
import logging
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TU = SETTING['CORE']['Tanium']['USE']
TDBHost = SETTING['CORE']['Tanium']['DB']['DBHost']
TDBName = SETTING['CORE']['Tanium']['DB']['DBName']
TDBUser = SETTING['CORE']['Tanium']['DB']['DBUser']
TDBPwd = SETTING['CORE']['Tanium']['DB']['DBPwd']
TATNM = SETTING['CORE']['Tanium']['DB']['AssetTNM']
TStTNM = SETTING['CORE']['Tanium']['DB']['StatisticsTNM']

ZU = SETTING['CORE']['Zabbix']['USE']
ZDBHost = SETTING['CORE']['Zabbix']['DB']['DBHost']
ZDBName = SETTING['CORE']['Zabbix']['DB']['DBName']
ZDBUser = SETTING['CORE']['Zabbix']['DB']['DBUser']
ZDBPwd = SETTING['CORE']['Zabbix']['DB']['DBPwd']
ZATNM = SETTING['CORE']['Zabbix']['DB']['AssetTNM']
ZStTNM = SETTING['CORE']['Zabbix']['DB']['StatisticsTNM']

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")


def plug_in(data, core, dataType) :
    try:
        logging.info(core+' '+dataType+' Data OUTPUT Plug In : DB')
        logging.info(core + ' ' + dataType + ' Data Table connection(Insert) Start')
        if core == 'tanium':
            DBHost = TDBHost
            DBName = TDBName
            DBUser = TDBUser
            DBPwd = TDBPwd
            if dataType == 'source':
                TNM = TATNM
            if dataType == 'statistics':
                TNM = TStTNM
        if core == 'zabbix':
            DBHost = ZDBHost
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
        insertConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
        insertCur = insertConn.cursor()

        if core == 'tanium':
            if dataType == 'source':
                IQ = """ INSERT INTO """+TNM+""" (computer_id, computer_name, last_reboot, disk_total_space, disk_used_space, os_platform, operating_system, is_virtual, chassis_type, ip_address, listen_port_count, established_port_count, ram_use_size, ram_total_size, asset_collection_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '""" + yesterday +""" 23:59:59"""+"""');"""
                datalen = len(data.computer_id)
            if dataType == 'statistics':
                IQ = """ INSERT INTO """ + TNM + """ (classification, item, item_count, statistics_collection_date) VALUES (%s, %s, %s, '""" + yesterday + """ 23:59:59""" + """');"""
                datalen = len(data['classification'])
        if core == 'zabbix':
            if dataType == 'source':
                IQ = """ INSERT INTO """ + TNM + """ (zabbix_asset_num, zabbix_name, zabbix_description, zabbix_ip, zabbix_up_time, zabbix_process_num, zabbix_disk_used, zabbix_mem_used, zabbix_cpu_used, zabbix_agent_ver, zabbix_agent_run, zabbix_asset_date) VALUES (nextval('seq_zabbix_asset'), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '""" + yesterday + """ 23:59:59""" + """');"""
                datalen = len(data.zabbix_name)

        logging.info('Table Name : ' + TNM)
        logging.info('Insert Query : ' + IQ)
        print(datalen)
        for i in range(datalen):
            if core == 'tanium':
                if dataType == 'source':
                    CI = data.computer_id[i]
                    CN = data.computer_name[i]
                    LR = data.last_reboot[i]
                    DTS = data.disk_total_space[i]
                    DUS = data.disk_used_space[i]
                    OP = data.os_platform[i]
                    OS = data.operating_system[i]
                    IV = data.is_virtual[i]
                    CT = data.chassis_type[i]
                    IP = data.ip_address[i]
                    LPC = data.listen_port_count[i]
                    EPC = data.established_port_count[i]
                    RUS = data.ram_use_size[i]
                    RTS = data.ram_total_size[i]
                    dataList = CI, CN, LR, DTS, DUS, OP, OS, IV, CT, IP, LPC, EPC, RUS, RTS
                if dataType == 'statistics':
                    CF = data['classification'][i]
                    ITEM = data['item'][i]
                    ICOUNT = data['count'][i]
                    dataList = CF, ITEM, ICOUNT
            if core == 'zabbix':
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
        logging.warning(dataType + 'Data Insert Connection Failure : ' + str(e))
