import psycopg2
import json
import logging
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

SODBHOST = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['HOST']
SODBPORT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['PORT']
SODBNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['NAME']
SODBUNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['USER']
SODBPWD = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['PWD']
SOTNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['DB']['PS']['TNM']

STDBHOST = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['HOST']
STDBPORT = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['PORT']
STDBNM = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['NAME']
STDBUNM = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['USER']
STDBPWD = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['PWD']
STTNM = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['INPUT']['DB']['PS']['TNM']

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")

def plug_in(core, dataType) :
    try:
        logging.info(core+' '+dataType+' Data INPUT Plug In : DB')

        if core == 'tanium':
            if dataType == 'source' :
                TDBHost = SODBHOST
                TDBPort = SODBPORT
                TDBName = SODBNM
                TDBUser = SODBUNM
                TDBPwd = SODBPWD
                TNM = SOTNM
            if dataType == 'statistics':
                TDBHost = STDBHOST
                TDBPort = STDBPORT
                TDBName = STDBNM
                TDBUser = STDBUNM
                TDBPwd = STDBPWD
                TNM = STTNM
            logging.info(core + ' ' + dataType + ' Data ' + TNM + ' Table connection(Select) Start')
            DL = []
            SelectConn = psycopg2.connect('host={0} port={1} dbname={2} user={3} password={4}'.format(TDBHost, TDBPort, TDBName, TDBUser, TDBPwd))
            SelectCur = SelectConn.cursor()
            if dataType == 'source':
                SelectQ = """ 
                    select 
                        computer_id, computer_name, last_reboot, disk_total_space, disk_used_space, os_platform, 
                        operating_system, is_virtual, chassis_type, ipv_address, listen_port_count, 
                        established_port_count, ram_use_size, ram_total_size, installed_applications_name, 
                        installed_applications_version, installed_applications_silent_uninstall_string, 
                        installed_applications_uninstallable, running_processes, running_service, cup_consumption, 
                        cup_details_system_type, cup_details_cup, cup_details_cup_speed, 
                        cup_details_total_physical_processors, cup_details_total_cores, 
                        cup_details_total_logical_processors, 
                        disk_free_space, high_cup_processes, 
                        high_memory_processes, high_uptime, ip_address, tanium_client_nat_ip_address, 
                        last_logged_in_user, listen_ports_process, listen_ports_name, listen_ports_local_port, 
                        last_system_crash, mac_address, memory_consumption, open_port, open_share_details_name, 
                        open_share_details_path, open_share_details_status, open_share_details_type, 
                        open_share_details_permissions, primary_owner_name, uptime, usb_write_protected, user_accounts, 
                        ad_query_last_logged_in_user_date, ad_query_last_logged_in_user_name, 
                        ad_query_last_logged_in_user_time
                    from  
                    """ + TNM + """
                        where 
                            to_char(asset_collection_date, 'YYYY-MM-DD') = '""" + yesterday + """' """
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