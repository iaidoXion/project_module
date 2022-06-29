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

def Daily() :
    try:
        AssetSelectL = []
        if DataLoadingType == 'DB':
            AssetSelectConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            AssetSelectCur = AssetSelectConn.cursor()
            AssetSelectQ = """ 
                select
                    y.computer_id as computer_id,
                    y.asset_item as asset_item, 
                    y.os_item as os_item, 
                    y.drive_use_size as today_disk_size, 
                    yt.drive_use_size as yesterday_disk_size,
                    y.ip_address,
                    y.listen_port_count,
                    yt.listen_port_count,
                    y.established_port_count,
                    yt.established_port_count,
                    y.ram_use_size,
                    yt.ram_use_size,
                    y.last_seen_at as last_seen_at, 
                    y.asset_collection_date as asset_collection_date
                from 
                    (select 
                        computer_id,
                        asset_item, 
                        os_item, 
                        drive_use_size, 
                        ip_address,
                        listen_port_count,
                        established_port_count,
                        ram_use_size,
                        last_seen_at, 
                        asset_collection_date
                    from 
                        """+AssetTNM+"""
                    where 
                        to_char(asset_collection_date, 'YYYY-MM-DD') = '"""+yesterday+"""' ) as y
                LEFT JOIN 
                    (select 
                        computer_id,
                        drive_use_size, 
                        listen_port_count,
                        established_port_count,
                        ram_use_size,
                        asset_collection_date
                    from 
                        """+AssetTNM+"""
                    where 
                        to_char(asset_collection_date, 'YYYY-MM-DD') = '"""+twoago+"""' ) as yt
                ON y.computer_id = yt.computer_id
                """
            #print(AssetSelectQ)
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




