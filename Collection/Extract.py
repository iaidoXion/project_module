import psycopg2
import json
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
DataLoadingType = SETTING['MODULE']['DataLoadingType']
DBHost = SETTING['DB']['DBHost']
DBName = SETTING['DB']['DBName']
DBUser = SETTING['DB']['DBUser']
DBPwd = SETTING['DB']['DBPwd']
AssetTNM = SETTING['DB']['AssetTNM']
BS = SETTING['FILE']
today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")

def AssetDaily() :
    try:
        AssetSelectL = []
        if DataLoadingType == 'DB':
            AssetSelectConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            AssetSelectCur = AssetSelectConn.cursor()
            AssetSelectQ = """ 
                select
                    t.computer_id as computer_id,
                    t.asset_item as asset_item, 
                    t.os_item as os_item, 
                    t.disk_total_space as today_disk_size, 
                    y.disk_total_space as yesterday_disk_size,
                    t.last_seen_at as last_seen_at, 
                    t.asset_collection_date as asset_collection_date
                from 
                    (select 
                        computer_id,
                        asset_item, 
                        os_item, 
                        disk_total_space, 
                        last_seen_at, 
                        asset_collection_date
                    from 
                        daily_assets
                    where 
                        to_char(asset_collection_date, 'YYYY-MM-DD HH24:MI:SS') > '"""+yesterday+""" 23:58:59' 
                    and 
                        to_char(asset_collection_date, 'YYYY-MM-DD HH24:MI:SS') <= '"""+today+""""') as t
                LEFT JOIN 
                    (select 
                        computer_id,
                        disk_total_space, 
                        asset_collection_date
                    from 
                        daily_assets
                    where 
                        to_char(asset_collection_date, 'YYYY-MM-DD HH24:MI:SS') > '"""+twoago+""" 23:58:59' 
                    and 
                        to_char(asset_collection_date, 'YYYY-MM-DD HH24:MI:SS') <= '"""+yesterday+""" 23:58:59') as y
                    
                ON t.computer_id = y.computer_id
                """

            AssetSelectCur.execute(AssetSelectQ)
            AssetSelectRS=AssetSelectCur.fetchall()
            for AssetSelectR in AssetSelectRS :
                AssetSelectL.append(AssetSelectR)
        elif DataLoadingType == 'FILE':
            AS = BS['asset']
            Storage = AS['Storage']
            FNM = AS['FileName'] + yesterday
            FT = AS['FileType']
            FileFullName = FNM + FT
            with open(Storage + FileFullName, encoding="UTF-8") as ADF:
                ADL = json.loads(ADF.read())
            AssetSelectL=ADL
        return AssetSelectL
    except :
        if DataLoadingType == 'DB':
            print('Asset Daily Table connection(Select) Failure')
        elif DataLoadingType == 'FILE':
            print('Asset Daily File(Read) Failure')




