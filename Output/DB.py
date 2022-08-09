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
today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")


def plug_in(data, dataType) :
    try:
        logging.info('OUTPUT Plug In : DB')
        if TU == 'true':
            logging.info('Table connection(Insert) Start')
            logging.info('Insert Data Type : '+dataType)
            logging.info('Databases Host : ' + TDBHost)
            logging.info('Databases Name : ' + TDBName)
            logging.info('Databases User : ' + TDBUser)
            logging.info('Databases PWD : ' + TDBPwd)
            insertConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(TDBHost, TDBName, TDBUser, TDBPwd))
            insertCur = insertConn.cursor()
            if dataType == 'source':
                TNM = TATNM
                IQ = """ INSERT INTO """+TNM+""" (computer_id, computer_name, last_reboot, disk_total_space, disk_used_space, os_platform, operating_system, is_virtual, chassis_type, ip_address, listen_port_count, established_port_count, ram_use_size, ram_total_size, asset_collection_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '""" + yesterday +""" 23:59:59"""+"""');"""
                datalen = len(data.computer_id)
            elif dataType == 'statistics':
                TNM = TStTNM
                IQ = """ INSERT INTO """ + TNM + """ (classification, item, item_count, statistics_collection_date) VALUES (%s, %s, %s, '""" + yesterday + """ 23:59:59""" + """');"""
                datalen = len(data['classification'])
            logging.info('Table Name : ' + TNM)
            logging.info('Insert Query : ' + IQ)
            for i in range(datalen):
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
                elif dataType == 'statistics':
                    CF = data['classification'][i]
                    ITEM = data['item'][i]
                    ICOUNT = data['count'][i]
                    dataList = CF, ITEM, ICOUNT
                insertCur.execute(IQ, (dataList))
            insertConn.commit()
            insertConn.close()
    except ConnectionError as e:
        logging.warning(dataType + 'Data Insert Connection Failure : ' + str(e))
