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
                select * from web_menusetting;
                """
            #print(AssetSelectQ)
            AssetSelectCur.execute(AssetSelectQ)
            AssetSelectRS=AssetSelectCur.fetchall()
            for AssetSelectR in AssetSelectRS :
                AssetSelectL.append(AssetSelectR)
                print(AssetSelectR)
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




