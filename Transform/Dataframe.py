import json
import pandas as pd
from datetime import datetime, timedelta
yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
twodaysago = (datetime.today() - timedelta(2)).strftime("%Y%m%d")
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

def plug_in(data, InputPlugin, dataType) :
    DFL = []
    if dataType == 'source' :
        DL = data['dataList']
        DFC = ['computer_id', 'computer_name', 'last_reboot', 'disk_total_space', 'disk_used_space', 'os_platform',
               'operating_system', 'is_virtual', 'chassis_type', 'ip_address', 'listen_port_count', 'established_port_count',
               'ram_use_size', 'ram_total_size']
        for d in DL:
            if InputPlugin == 'API' :
                CI = d[0]
                CN = d[1]
                LR = d[2]
                DTS = d[3]
                DUS = d[4]
                OP = d[5]
                OS = d[6]
                IV = d[7]
                CT = d[8]
                IP = d[9]
                LPC = d[10]
                EPC = d[11]
                RUS = d[12]
                RTS = d[13]
            if InputPlugin == 'DB' :
                print()
            if InputPlugin == 'ES' :
                CI = d['Computer ID']
                CN = d['Computer Name']
                LR = 'd[2]'
                DTS = 'd[3]'
                DUS = 'd[4]'
                OP = 'd[5]'
                OS = 'd[6]'
                IV = 'd[7]'
                CT = 'd[8]'
                IP = 'd[9]'
                LPC = 'd[10]'
                EPC = 'd[11]'
                RUS = 'd[12]'
                RTS = 'd[13]'
            DFL.append([CI, CN, LR, DTS, DUS, OP, OS, IV, CT, IP, LPC, EPC, RUS, RTS])
    elif dataType == 'statistics':
        DFC = ['id', 'assetItem', 'os', 'yesterdayDriveSize', 'twodaysagoDriveSize', 'ip', 'yesterdayListenPortCount','twodaysagoListenPortCount', 'yesterdayEstablishedPort', 'twodaysagoEstablishedPort', 'yesterdayRamUseSize', 'yesterdayRamTotalSize', 'lastLogin']

        if InputPlugin == 'DB' :
            for d in data:
                CID = d[0]
                AI = d[1]
                AIPer = AI.lower()
                if AIPer.startswith('macbook'):
                    AI = 'Notebook'
                if AI.startswith('imac'):
                    AI = 'Desktop'
                OI = d[2]
                TDTS = d[3]
                YDTS = d[4]
                IP = d[5]
                TLPC = d[6]
                YLPC = d[7]
                TEP = d[8]
                YEP = d[9]
                TRUS = d[10]
                TRTS = d[11]
                LSA = d[12]
                DFL.append([CID, AI, OI, TDTS, YDTS, IP, TLPC, YLPC, TEP, YEP, TRUS, TRTS, LSA])
        elif InputPlugin == 'ES' :
            data = data.dropna(axis=0)
            for i in range(len(data.id)) :
                CID = data.id[i]
                AI = data.assetItem[i]
                AIPer = AI.lower()
                if AIPer.startswith('macbook'):
                    AI = 'Notebook'
                if AI.startswith('imac'):
                    AI = 'Desktop'
                OI = data.os[i]
                TDTS = data.yesterdayDriveSize[i]
                YDTS = data.twodaysagoDriveSize[i]
                IP = data.ip[i]
                TLPC = data.yesterdayListenPortCount[i]
                YLPC = data.twodaysagoListenPortCount[i]
                TEP = data.yesterdayEstablishedPort[i]
                YEP = data.twodaysagoEstablishedPort[i]
                TRUS = data.yesterdayRamUseSize[i]
                TRTS = data.yesterdayRamTotalSize[i]
                LSA = data.lastLogin[i]
                DFL.append([CID, AI, OI, TDTS, YDTS, IP, TLPC, YLPC, TEP, YEP, TRUS, TRTS, LSA])
    DF = pd.DataFrame(DFL, columns=DFC)

    return DF

def zplug_in(data, InputPlugin, dataType):
    if dataType == 'source':
        DL = data['dataList']

        DFC = ['zabbix_name', 'zabbix_description', 'zabbix_ip',  'zabbix_up_time', 'zabbix_process_num',
               'zabbix_disk_used', 'zabbix_mem_used', 'zabbix_cpu_used', 'zabbix_agent_ver', 'zabbix_agent_run']
        DFL = []
        for d in DL:
            if InputPlugin == 'API':
                IP=d['ip']
                if d['itemname']=="System name":
                    SN= d['value']
                if d['itemname']=="System description":
                    OS= d['value'].split(' ')[0]
                if d['itemname'] == "System uptime":
                    UT= d['value']
                if d['itemname'] == "Number of processes":
                    PN= d['value']
                if d['itemname'] == "/: Space utilization":
                    DU = d['value']
                if d['itemname'] == "Memory utilization":
                    MU = d['value']
                if d['itemname'] == "CPU utilization":
                    CU = d['value']
                if d['itemname'] == "Version of Zabbix agent running":
                    AV = d['value']
                if d['itemname'] == "Zabbix agent availability":
                    AA = d['value']
                    if AA == '1':
                        AR = "사용중"
                    else:
                        AR = "사용안함"

                    DFL.append([SN, OS, IP, UT, PN, DU, MU, CU, AV, AR])
                    # print(DFL)
    DF = pd.DataFrame(DFL, columns=DFC)
    return DF






    """
        for i in range(len(DL)):
            # CI = DL[i][0]
            LPI = DL[i][10]
            if len(LPI) > 10:
                LPI = '0'
            else:
                LPI = DL[i][10]
            EPI = DL[i][11]
            if len(EPI) > 10:
                EPI = '0'
            else:
                EPI = DL[i][11]
            RUS = DL[i][12].split(' ')[0]
            if RUS.isdigit():
                RUS = int(RUS)
            else:
                RUS = 0
            RTS = DL[i][13].split(' ')[0]
            if RTS.isdigit():
                RTS = int(RTS)
            else:
                RTS = 0
            # RTS = DL[i][13].split(' ')[0]
            # if RTS.isdigit() :
            #    RTS = int(RUS)
            # else:
            #    RTS = 0
            DFL.append([CI, LPI, EPI, RUS, RTS])
            # print(DL[i])
    DF = pd.DataFrame(DFL, columns=DFC)
    # print(DF)
    return DF
    
            if dataType == 'asset' :
                DFC = ['computer_id', 'asset_item', 'os_platform', 'drive_use_size', 'last_seen_at', 'ip_address']
                for d in DL :
                    if InputPlugin == 'API' :
                        CI = d['computer_id']
                        AI = d['asset_item']
                        OI = d['os_platform']
                        DI = d['drive_use_size']
                        LI = d['last_seen_at'].split('T')[0]
                        II = d['ip_address']
                    elif InputPlugin == 'ES' :
                        CI = d['Computer ID']
                        AI = d['Chassis Type']
                        OI = d['OS Platform']
                        DI = d['Disk Used Space'].split(' ')[1]
                        dateString = d['Last Reboot'].split('+')[0]
                        dateFormatter = "%a, %d %b %Y %H:%M:%S "
                        LI = datetime.strptime(dateString, dateFormatter)
                        II = d['IPv4 Address']
                    AIPer = AI.lower()
                    if AIPer.startswith('macbook'):
                        AI = 'Notebook'
                    if AIPer.startswith('imac'):
                        AI = 'Desktop'
                    DFL.append([CI, AI, OI, DI, LI, II])



            elif dataType == 'sensor' :
            """






