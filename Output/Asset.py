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


def Daily(ADTL) :
    try:
        if DataLoadingType == 'DB':
            logging.info('assetToday : '+today)
            logging.info('assetYesterday : '+yesterday)
            AssetInsertConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            AssetInsertCur = AssetInsertConn.cursor()
            LIQ = """ INSERT INTO daily_asset (computer_id, asset_item, os_item, drive_use_size, ip_address, listen_port_count, established_port_count, ram_use_size, ram_total_size, last_seen_at, asset_collection_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '""" + yesterday +""" 23:59:59"""+"""');"""
            for i in range(len(ADTL)) :
                CID = ADTL[i]['computer_id']
                AI = ADTL[i]['asset_item']
                OI = ADTL[i]['os_platform']
                DTS = str(ADTL[i]['drive_use_size'])
                II = ADTL[i]['ip_address']
                LPC = str(ADTL[i]['listen_port_count'])
                EPC = str(ADTL[i]['established_port_count'])
                RUS = ADTL[i]['ram_use_size']
                RTS = ADTL[i]['ram_total_size']
                LSA = ADTL[i]['last_seen_at']
                #print(type(CID), type(AI), type(OI), type(DTS), type(II), type(LPC), type(EPC), type(LSA))
                AssetInsertCur.execute(LIQ, (CID, AI, OI, DTS, II, LPC, EPC,  RUS, RTS, LSA))
            AssetInsertConn.commit()
            AssetInsertConn.close()
        elif DataLoadingType == 'FILE':
            SB = {'data': ADTL}
            AS = BS['asset']
            Storage = AS['Storage']
            FNM = AS['FileName'] + today
            FT = AS['FileType']
            FileFullName = FNM + FT
            with open(Storage + FileFullName, 'w') as ADOF:
                json.dump(SB, ADOF)
            ADOF.close()
    except :
        if DataLoadingType == 'DB':
            print('Asset Daily Table connection(Insert) Failure')
        elif DataLoadingType == 'FILE':
            print('Asset Daily File(Write) Failure')
