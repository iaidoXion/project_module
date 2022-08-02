import psycopg2
import json
import logging
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DBHost = SETTING['DB']['DBHost']
DBName = SETTING['DB']['DBName']
DBUser = SETTING['DB']['DBUser']
DBPwd = SETTING['DB']['DBPwd']
AssetTNM = SETTING['DB']['AssetTNM']
StatisticsTNM = SETTING['DB']['StatisticsTNM']
DataLoadingType = SETTING['MODULE']['DataLoadingType']
BS = SETTING['FILE']
today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")


def write(data, dataType) :
    try:
        if dataType == 'asset':
            logging.info('assetToday : '+today)
            logging.info('assetYesterday : '+yesterday)
            AssetInsertConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            AssetInsertCur = AssetInsertConn.cursor()
            LIQ = """ INSERT INTO daily_asset (computer_id, computer_name, last_reboot, disk_total_space, disk_used_space, os_platform, operating_system, is_virtual, chassis_type, ip_address, listen_port_count, established_port_count, ram_use_size, ram_total_size, asset_collection_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '""" + yesterday +""" 23:59:59"""+"""');"""
            computer_id = data.computer_id
            computer_name = data.computer_name
            last_reboot = data.last_reboot
            disk_total_space = data.disk_total_space
            disk_used_space = data.disk_used_space
            os_platform = data.os_platform
            operating_system = data.operating_system
            is_virtual = data.is_virtual
            chassis_type = data.chassis_type
            ip_address = data.ip_address
            listen_port_count = data.listen_port_count
            established_port_count = data.established_port_count
            ram_use_size = data.ram_use_size
            ram_total_size = data.ram_total_size
            for i in range(len(computer_id)):
                CI = computer_id[i]
                CN = computer_name[i]
                LR = last_reboot[i]
                DTS = disk_total_space[i]
                DUS = disk_used_space[i]
                OP = os_platform[i]
                OS = operating_system[i]
                IV = is_virtual[i]
                CT = chassis_type[i]
                IP = ip_address[i]
                LPC = listen_port_count[i]
                EPC = established_port_count[i]
                RUS = ram_use_size[i]
                RTS = ram_total_size[i]
                AssetInsertCur.execute(LIQ, (CI, CN, LR, DTS, DUS, OP, OS, IV, CT, IP, LPC, EPC, RUS, RTS))
            AssetInsertConn.commit()
            AssetInsertConn.close()
        elif dataType == 'statistics' :
            logging.info('StatisticsToday : ' + today)
            logging.info('StatisticsYesterday : ' + yesterday)
            StatisticsInsertConn = psycopg2.connect(
                'host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            StatisticsInsertCur = StatisticsInsertConn.cursor()
            SQ = """ INSERT INTO """ + StatisticsTNM + """ (classification, item, item_count, statistics_collection_date) VALUES (%s, %s, %s, '""" + yesterday + """ 23:59:59""" + """');"""

            CFL = data['classification']
            IL = data['item']
            CL = data['count']
            for i in range(len(CFL)):
                CF = CFL[i]
                ITEM = IL[i]
                ICOUNT = CL[i]
                StatisticsInsertCur.execute(SQ, (CF, ITEM, ICOUNT))
            StatisticsInsertConn.commit()
            StatisticsInsertConn.close()
        """elif DataLoadingType == 'FILE':
            SB = {'data': ADTL}
            AS = BS['asset']
            Storage = AS['Storage']
            FNM = AS['FileName'] + today
            FT = AS['FileType']
            FileFullName = FNM + FT
            with open(Storage + FileFullName, 'w') as ADOF:
                json.dump(SB, ADOF)
            ADOF.close()"""
    except :
        if DataLoadingType == 'DB':
            print('Asset Daily Table connection(Insert) Failure')
        elif DataLoadingType == 'FILE':
            print('Asset Daily File(Write) Failure')
