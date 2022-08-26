import psycopg2
import json
import logging
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

TSODBHost = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['DB']['PS']['HOST']
TSODBName = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['DB']['PS']['NAME']
TSODBUser = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['DB']['PS']['USER']
TSODBPwd = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['DB']['PS']['PWD']
TSOTNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['DB']['PS']['TNM']

TSTDBHost = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['DB']['PS']['HOST']
TSTDBName = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['DB']['PS']['NAME']
TSTDBUser = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['DB']['PS']['USER']
TSTDBPwd = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['DB']['PS']['PWD']
TSTTNM = SETTING['CORE']['Tanium']['MODULE']['STATISTICS']['PLUGIN']['OUTPUT']['DB']['PS']['TNM']

ZU = SETTING['CORE']['Zabbix']['USE']
ZDBHost = SETTING['CORE']['Zabbix']['DB']['DBHost']
ZDBName = SETTING['CORE']['Zabbix']['DB']['DBName']
ZDBUser = SETTING['CORE']['Zabbix']['DB']['DBUser']
ZDBPwd = SETTING['CORE']['Zabbix']['DB']['DBPwd']
ZATNM = SETTING['CORE']['Zabbix']['DB']['AssetTNM']
ZStTNM = SETTING['CORE']['Zabbix']['DB']['StatisticsTNM']

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")


def plug_in(data, core, dataType) :
    try:
        logging.info(core+' '+dataType+' Data OUTPUT Plug In : DB')
        logging.info(core + ' ' + dataType + ' Data Table connection(Insert) Start')
        if core == 'tanium':
            DBHost = TSODBHost
            DBName = TSODBName
            DBUser = TSODBUser
            DBPwd = TSODBPwd
            if dataType == 'source':
                TNM = TSOTNM
            if dataType == 'statistics':
                TNM = TSTTNM
        if core == 'zabbix':
            DBHost = ZDBHost
            DBName = ZDBName
            DBUser = ZDBUser
            DBPwd = ZDBPwd
            if dataType == 'source':
                TNM = ZATNM

        logging.info('Insert Data Type : '+dataType)
        logging.info('Databases Host : ' + DBHost)
        logging.info('Databases Name : ' + DBName)
        logging.info('Databases User : ' + DBUser)
        logging.info('Databases PWD : ' + DBPwd)
        insertConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
        insertCur = insertConn.cursor()

        if core == 'tanium':
            if dataType == 'source':
                IQ = """ INSERT INTO 
                    """+TNM+""" (
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
                        ad_query_last_logged_in_user_time, asset_collection_date
                        ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, '""" + yesterday +""" 23:59:59"""+"""'
                        );"""
                datalen = len(data.computer_id)
            if dataType == 'statistics':
                IQ = """ INSERT INTO 
                    """ + TNM + """ (
                        classification, item, item_count, statistics_collection_date
                        ) VALUES (
                        %s, %s, %s, '""" + yesterday + """ 23:59:59""" + """');"""
                datalen = len(data['classification'])
        if core == 'zabbix':
            if dataType == 'source':
                IQ = """ INSERT INTO """ + TNM + """ (zabbix_asset_num, zabbix_name, zabbix_description, zabbix_ip, zabbix_up_time, zabbix_process_num, zabbix_disk_used, zabbix_mem_used, zabbix_cpu_used, zabbix_agent_ver, zabbix_agent_run, zabbix_asset_date) VALUES (nextval('seq_zabbix_asset'), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '""" + yesterday + """ 23:59:59""" + """');"""
                datalen = len(data.zabbix_name)

        logging.info('Table Name : ' + TNM)
        logging.info('Insert Data Count : ' + str(datalen))
        for i in range(datalen):
            if core == 'tanium':
                if dataType == 'source':
                    CI = data.computer_id[i]
                    CN = data.computer_name[i]
                    LR = data.last_reboot[i]
                    DTS = data.disk_total_space[i]
                    DUS = data.disk_used_space[i]
                    OP = data.os_platform[i]
                    OS = data.operating_system[i]
                    IV = data.is_virtual[i]
                    CT = data.chassis_type[i]
                    IP = data.ipv_address[i]
                    LPC = data.listen_port_count[i]
                    EPC = data.established_port_count[i]
                    RUS = data.ram_use_size[i]
                    RTS = data.ram_total_size[i]
                    IA = data.installed_applications_name[i]
                    IAV = data.installed_applications_version[i]
                    IASUS = data.installed_applications_silent_uninstall_string[i]
                    IAU = data.installed_applications_uninstallable[i]
                    RP = data.running_processes[i]
                    RS = data.running_service[i]
                    CPUC = data.cup_consumption[i]
                    CPUDST = data.cup_details_system_type[i]
                    CPUDCPU = data.cup_details_cup[i]
                    CPUDCPUS = data.cup_details_cup_speed[i]
                    CPUDTPP = data.cup_details_total_physical_processors[i]
                    CPUDTC = data.cup_details_total_cores[i]
                    CPUDTLP = data.cup_details_total_logical_processors[i]
                    DFS = data.disk_free_space[i]
                    HCPUP = data.high_cup_processes[i]
                    HMP = data.high_memory_processes[i]
                    HU = data.high_uptime[i]
                    IPA = data.ip_address[i]
                    TCNATIPA = data.tanium_client_nat_ip_address[i]
                    LLIU = data.last_logged_in_user[i]
                    LPP = data.listen_ports_process[i]
                    LPN = data.listen_ports_name[i]
                    LPLP = data.listen_ports_local_port[i]
                    LSC = data.last_system_crash[i]
                    MACA = data.mac_address[i]
                    MC = data.memory_consumption[i]
                    openPort = data.open_port[i]
                    OSDN = data.open_share_details_name[i]
                    OSDPath = data.open_share_details_path[i]
                    OSDS = data.open_share_details_status[i]
                    OSDT = data.open_share_details_type[i]
                    OSDP = data.open_share_details_permissions[i]
                    PON = data.primary_owner_name[i]
                    Uptime = data.uptime[i]
                    USBWP = data.usb_write_protected[i]
                    UA = data.user_accounts[i]
                    ADQLLIUD = data.ad_query_last_logged_in_user_date[i]
                    ADQLLIUN = data.ad_query_last_logged_in_user_name[i]
                    ADQLLIUT = data.ad_query_last_logged_in_user_time[i]
                    dataList = CI, CN, LR, DTS, DUS, OP, OS, IV, CT, IP, LPC, EPC, RUS, RTS, IA, IAV, IASUS, IAU, RP, RS, CPUC, CPUDST, CPUDCPU, CPUDCPUS, CPUDTPP, CPUDTC, CPUDTLP, DFS, HCPUP, HMP, HU, IPA, TCNATIPA, LLIU, LPP, LPN, LPLP, LSC, MACA, MC, openPort, OSDN, OSDPath, OSDS, OSDT, OSDP, PON, Uptime, USBWP, UA, ADQLLIUD, ADQLLIUN, ADQLLIUT
                if dataType == 'statistics':
                    CF = data['classification'][i]
                    ITEM = data['item'][i]
                    ICOUNT = data['count'][i]
                    dataList = CF, ITEM, ICOUNT
            if core == 'zabbix':
                if dataType == 'source':
                    HN = data.zabbix_name[i]
                    OS = data.zabbix_description[i]
                    IP = data.zabbix_ip[i]
                    UT = data.zabbix_up_time[i]
                    PN = data.zabbix_process_num[i]
                    DU = data.zabbix_disk_used[i]
                    MU = data.zabbix_mem_used[i]
                    CU = data.zabbix_cpu_used[i]
                    AV = data.zabbix_agent_ver[i]
                    AR = data.zabbix_agent_run[i]
                    dataList = HN, OS, IP, UT, PN, DU, MU, CU, AV, AR
            insertCur.execute(IQ, (dataList))
        insertConn.commit()
        insertConn.close()
    except ConnectionError as e:
        logging.warning(dataType + 'Data Insert Connection Failure : ' + str(e))
