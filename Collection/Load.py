import psycopg2
import json
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
today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")


def AssetDaily(AssetData) :
    try:
        if DataLoadingType == 'DB':
            AssetInsertConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            AssetInsertCur = AssetInsertConn.cursor()
            LIQ = """ INSERT INTO """ + AssetTNM + """ (computer_id, asset_item, os_item, disk_total_space, last_seen_at, asset_collection_date) VALUES (%s, %s, %s, %s, %s, '""" + today + """');"""
            for i in AssetData :
                CID = i['computer_id']
                AI = i['asset_item']
                OI = i['os_platform']
                DTS = i['disk_total_space']
                LSA = i['last_seen_at']
                AssetInsertCur.execute(LIQ, (CID, AI, OI, DTS, LSA))
            AssetInsertConn.commit()
            AssetInsertConn.close()
        elif DataLoadingType == 'FILE':
            SB = {'data': AssetData}
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

def StatisticsDaily(TSDL) :
    try:
        if DataLoadingType == 'DB':
            StatisticsInsertConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            StatisticsInsertCur = StatisticsInsertConn.cursor()
            SQ = """ INSERT INTO """ + StatisticsTNM + """ (classification, item, item_count, statistics_collection_date) VALUES (%s, %s, %s, '""" + today + """');"""

            CFL = TSDL['classification']
            IL = TSDL['item']
            CL = TSDL['count']
            for i in range(len(CFL)) :
                CF = CFL[i]
                ITEM = IL[i]
                ICOUNT = CL[i]
                StatisticsInsertCur.execute(SQ, (CF, ITEM, ICOUNT))
            StatisticsInsertConn.commit()
            StatisticsInsertConn.close()

        elif DataLoadingType == 'FILE':
            SB = {'data': TSDL}
            AS = BS['statistics']
            Storage = AS['Storage']
            FNM = AS['FileName'] + today
            FT = AS['FileType']
            FileFullName = FNM + FT
            with open(Storage + FileFullName, 'w') as SOF:
                json.dump(SB, SOF)
            SOF.close()

    except:
        if DataLoadingType == 'DB':
            print('Statistics Daily Table connection(Insert) Failure')
        elif DataLoadingType == 'FILE':
            print('Statistics Daily File(Write) Failure')