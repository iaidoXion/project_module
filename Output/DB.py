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


def load(data, dataType) :
    try:
        if dataType == 'asset':
            logging.info('assetToday : '+today)
            logging.info('assetYesterday : '+yesterday)
            AssetInsertConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            AssetInsertCur = AssetInsertConn.cursor()
            LIQ = """ INSERT INTO daily_asset (computer_id, asset_item, os_item, drive_use_size, ip_address, listen_port_count, established_port_count, ram_use_size, ram_total_size, last_seen_at, asset_collection_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '""" + yesterday +""" 23:59:59"""+"""');"""
            for i in range(len(data)) :
                CID = data[i]['computer_id']
                AI = data[i]['asset_item']
                OI = data[i]['os_platform']
                DTS = str(data[i]['drive_use_size'])
                II = data[i]['ip_address']
                LPC = str(data[i]['listen_port_count'])
                EPC = str(data[i]['established_port_count'])
                RUS = data[i]['ram_use_size']
                RTS = data[i]['ram_total_size']
                LSA = data[i]['last_seen_at']
                #print(type(CID), type(AI), type(OI), type(DTS), type(II), type(LPC), type(EPC), type(LSA))
                AssetInsertCur.execute(LIQ, (CID, AI, OI, DTS, II, LPC, EPC,  RUS, RTS, LSA))
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
