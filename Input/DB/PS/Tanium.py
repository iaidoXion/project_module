import psycopg2
import json
import logging
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

TSODBHost = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['HOST']
TSODBName = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['NAME']
TSODBUser = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['USER']
TSODBPwd = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['PWD']
TSOTNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['TNM']

TSTDBHost = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['HOST']
TSTDBName = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['NAME']
TSTDBUser = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['USER']
TSTDBPwd = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['PWD']
TSTTNM = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['TNM']

today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")

def plug_in(core, dataType) :
    try:
        logging.info(core+' '+dataType+' Data INPUT Plug In : DB')

        if core == 'tanium':
            if dataType == 'source' :
                TDBHost = TSODBHost
                TDBName = TSODBName
                TDBUser = TSODBUser
                TDBPwd = TSODBPwd
                TNM = TSOTNM
            if dataType == 'statistics':
                TDBHost = TSTDBHost
                TDBName = TSTDBName
                TDBUser = TSTDBUser
                TDBPwd = TSTDBPwd
                TNM = TSTTNM
            logging.info(core + ' ' + dataType + ' Data ' + TNM + ' Table connection(Select) Start')
            DL = []
            SelectConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(TDBHost, TDBName, TDBUser, TDBPwd))
            SelectCur = SelectConn.cursor()
            if dataType == 'source':
                SelectQ = """ 
                    select 
                        computer_id, 
                        computer_name,
                        last_reboot, 
                        disk_total_space, 
                        disk_used_space,
                        os_platform,
                        operating_system,
                        is_virtual,
                        chassis_type, 
                        ip_address, 
                        listen_port_count, 
                        established_port_count
                    from  
                    """ + TNM
            if dataType == 'statistics':
                SelectQ = """ 
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
                            """ + TNM + """
                        where 
                            to_char(asset_collection_date, 'YYYY-MM-DD') = '""" + yesterday + """' ) as y
                    LEFT JOIN 
                        (select 
                            computer_id,
                            disk_used_space, 
                            listen_port_count,
                            established_port_count,
                            asset_collection_date
                        from 
                            """ + TNM + """
                        where 
                            to_char(asset_collection_date, 'YYYY-MM-DD') = '""" + twoago + """' ) as yt
                    ON y.computer_id = yt.computer_id
                    """
            SelectCur.execute(SelectQ)
            SelectRS = SelectCur.fetchall()
            for RS in SelectRS:
                DL.append(RS)
        returnList = {'resCode': 200, 'dataList': DL}
        return returnList
    except ConnectionError as e:
        logging.warning(TNM + ' Table Select connection Failure : ' + str(e))