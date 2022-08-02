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

def read() :
    try:
        AssetSelectL = []
        if DataLoadingType == 'DB':
            AssetSelectConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            AssetSelectCur = AssetSelectConn.cursor()
            AssetSelectQ = """ 
                select
                    y.computer_id as computer_id,
                    y.chassis_type as asset_item, 
                    y.os_platform as os_item, 
                    y.disk_used_space as today_disk_size, 
                    yt.disk_used_space as yesterday_disk_size,
                    y.ip_address,
                    y.listen_port_count,
                    yt.listen_port_count,
                    y.established_port_count,
                    yt.established_port_count,
                    y.ram_use_size,
                    y.ram_total_size,
                    y.last_reboot as last_seen_at, 
                    y.asset_collection_date as asset_collection_date
                from 
                    (select 
                        computer_id,
                        chassis_type, 
                        os_platform, 
                        disk_used_space, 
                        ip_address,
                        listen_port_count,
                        established_port_count,
                        ram_use_size,
                        ram_total_size,
                        last_reboot, 
                        asset_collection_date
                    from 
                        """+AssetTNM+"""
                    where 
                        to_char(asset_collection_date, 'YYYY-MM-DD') = '"""+yesterday+"""' ) as y
                LEFT JOIN 
                    (select 
                        computer_id,
                        disk_used_space, 
                        listen_port_count,
                        established_port_count,
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




