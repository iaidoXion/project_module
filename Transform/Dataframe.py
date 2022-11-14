
import pandas as pd
import logging
from datetime import datetime, timedelta
from pprint import pprint

yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
twodaysago = (datetime.today() - timedelta(2)).strftime("%Y%m%d")

def plug_in(data, InputPlugin, dataType):
    try:
        logging.info('Tanium ' + dataType + ' Data Transform(Dataframe) Plug In Start')
        logging.info('Input Plugin : ' + InputPlugin)
        DFL = []
        if dataType == 'source':
            DL = data['dataList']
            DFC = [
                'computer_id', 'computer_name', 'last_reboot', 'disk_total_space', 'disk_used_space', 'os_platform',
                'operating_system', 'is_virtual', 'chassis_type', 'ipv_address', 'listen_port_count',
                'established_port_count', 'ram_use_size', 'ram_total_size', 'installed_applications_name',
                'installed_applications_version', 'installed_applications_silent_uninstall_string',
                'installed_applications_uninstallable', 'running_processes', 'running_service', 'cup_consumption',
                'cup_details_system_type', 'cup_details_cup', 'cup_details_cup_speed',
                'cup_details_total_physical_processors', 'cup_details_total_cores', 'cup_details_total_logical_processors',
                'disk_free_space', 'high_cup_processes', 'high_memory_processes', 'high_uptime', 'ip_address',
                'tanium_client_nat_ip_address', 'last_logged_in_user', 'listen_ports_process', 'listen_ports_name',
                'listen_ports_local_port', 'last_system_crash', 'mac_address', 'memory_consumption', 'open_port',
                'open_share_details_name', 'open_share_details_path', 'open_share_details_status',
                'open_share_details_type', 'open_share_details_permissions', 'primary_owner_name', 'uptime',
                'usb_write_protected', 'user_accounts', 'ad_query_last_logged_in_user_date',
                'ad_query_last_logged_in_user_name', 'ad_query_last_logged_in_user_time'
            ]
            for d in DL:
                if InputPlugin == 'API':
                    CI = d[0][0]['text']
                    CN = d[1][0]['text']
                    LR = d[2][0]['text']
                    DTS = []
                    for DTSD in d[3]:
                        DTS.append(DTSD['text'])
                    DUS = []
                    for DUSD in d[4]:
                        DUS.append(DUSD['text'])
                    OP = d[5][0]['text']
                    OS = d[6][0]['text']
                    IV = d[7][0]['text']
                    CT = d[8][0]['text']
                    IP = d[9][0]['text']
                    LPC = d[10][0]['text']
                    EPC = d[11][0]['text']
                    RUS = d[12][0]['text']
                    RTS = d[13][0]['text']
                    IA = []
                    for IAD in d[14]:
                        IA.append(IAD['text'])
                    IAV = []
                    for IAVD in d[15]:
                        IAV.append(IAVD['text'])
                    IASUS = []
                    for IASUSD in d[16]:
                        IASUS.append(IASUSD['text'])
                    IAU = []
                    for IAUD in d[17]:
                        IAU.append(IAUD['text'])
                    RP = []
                    for RPD in d[18]:
                        RP.append(RPD['text'])
                    RS = []
                    for RSD in d[19]:
                        RS.append(RSD['text'])
                    CPUC = d[20][0]['text']
                    CPUDST = d[21][0]['text']
                    CPUDCPU = d[22][0]['text']
                    CPUDCPUS = d[23][0]['text']
                    CPUDTPP = d[24][0]['text']
                    CPUDTC = d[25][0]['text']
                    CPUDTLP = d[26][0]['text']
                    DFS = []
                    for DFSD in d[27]:
                        DFS.append(DFSD['text'])
                    HCPUP = []
                    for HCPUPD in d[28]:
                        HCPUP.append(HCPUPD['text'])
                    HMP = []
                    for HMPD in d[29]:
                        HMP.append(HMPD['text'])
                    HU = []
                    for HUD in d[30]:
                        HU.append(HUD['text'])
                    IPA = []
                    for IPAD in d[31]:
                        IPA.append(IPAD['text'])
                    TCNATIPA = d[32][0]['text']
                    LLIU = d[33][0]['text']
                    LPP = []
                    for LPPD in d[34]:
                        LPP.append(LPPD['text'])
                    LPN = []
                    for LPND in d[35]:
                        LPN.append(LPND['text'])
                    LPLP = []
                    for LPLPD in d[36]:
                        LPLP.append(LPLPD['text'])
                    LSC = d[37][0]['text']
                    MACA = []
                    for MACAD in d[38]:
                        MACA.append(MACAD['text'])
                    MC = d[39][0]['text']
                    openPort = []
                    for op in d[40]:
                        openPort.append(op['text'])
                    OSDN = []
                    for OSDND in d[41]:
                        OSDN.append(OSDND['text'])
                    OSDPath = []
                    for OSDPathD in d[42]:
                        OSDPath.append(OSDPathD['text'])
                    OSDS = []
                    for OSDSD in d[43]:
                        OSDS.append(OSDSD['text'])
                    OSDT = []
                    for OSDTD in d[44]:
                        OSDT.append(OSDTD['text'])
                    OSDP = []
                    for OSDPD in d[45]:
                        OSDP.append(OSDPD['text'])
                    PON = d[46][0]['text']
                    Uptime = d[47][0]['text']
                    USBWP = d[48][0]['text']
                    UA = []
                    for UAD in d[49]:
                        UA.append(UAD['text'])
                    ADQLLIUD = d[50][0]['text']
                    ADQLLIUN = d[51][0]['text']
                    ADQLLIUT = d[52][0]['text']

                if InputPlugin == 'DB':
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
                    IA = d[14]
                    IAV = d[15]
                    IASUS = d[16]
                    IAU = d[17]
                    RP = d[18]
                    RS = d[19]
                    CPUC = d[20]
                    CPUDST = d[21]
                    CPUDCPU = d[22]
                    CPUDCPUS = d[23]
                    CPUDTPP = d[24]
                    CPUDTC = d[25]
                    CPUDTLP = d[26]
                    DFS = d[27]
                    HCPUP = d[28]
                    HMP = d[29]
                    HU = d[30]
                    IPA = d[31]
                    TCNATIPA = d[32]
                    LLIU = d[33]
                    LPP = d[34]
                    LPN = d[35]
                    LPLP = d[36]
                    LSC = d[37]
                    MACA = d[38]
                    MC = d[39]
                    openPort = d[40]
                    OSDN = d[41]
                    OSDPath = d[42]
                    OSDS = d[43]
                    OSDT = d[44]
                    OSDP = d[45]
                    PON = d[46]
                    Uptime = d[47]
                    USBWP = d[48]
                    UA = d[49]
                    ADQLLIUD = d[50]
                    ADQLLIUN = d[51]
                    ADQLLIUT = d[52]
                if InputPlugin == 'ES' :
                    CI = d['Computer ID']
                    CN = d['Computer Name']
                    LR = d['Last Reboot']
                    DTS = d['Disk Total Space']
                    DUS = d['Disk Used Space']
                    OP = d['OS Platform']
                    OS = d['Operating System']
                    IV = d['Is Virtual']
                    CT = d['Chassis Type']
                    IP = d['IPv4 Address']
                    LPC = d['Listen Port Count']
                    EPC = d['Established Port Count']
                    RUS = d['Used Memory']
                    RTS = d['Total Memory']
                    """
                                    IA
                                    IAV
                                    IASUS
                                    IAU
                                    RP
                                    RS
                                    CPUC
                                    CPUDST
                                    CPUDCPU
                                    CPUDCPUS
                                    CPUDTPP
                                    CPUDTC
                                    CPUDTLP
                                    DFS
                                    HCPUP
                                    HMP
                                    HU
                                    IPA
                                    TCNATIPA
                                    LLIU
                                    LPP
                                    LPN
                                    LPLP
                                    LSC
                                    MACA
                                    MC
                                    openPort
                                    OSDN
                                    OSDPath
                                    OSDS
                                    OSDT
                                    OSDP
                                    PON
                                    Uptime
                                    USBWP
                                    UA
                                    ADQLLIUD
                                    ADQLLIUN
                                    ADQLLIUT
                                    """
                if InputPlugin == 'FILE':
                    CI = d['data'][0][0]['text']
                    CN = d['data'][1][0]['text']
                    LR = d['data'][2][0]['text']
                    DTS = []
                    for DTSD in d['data'][3]:
                        DTS.append(DTSD['text'])
                    DUS = []
                    for DUSD in d['data'][4]:
                        DUS.append(DUSD['text'])
                    OP = "d[5]"
                    OS = "d[6]"
                    IV = "d[7]"
                    CT = "d[8]"
                    IP = "d[9]"
                    LPC = "d[10]"
                    EPC = "d[11]"
                    RUS = "d[12]"
                    RTS = "d[13]"
                    IA = "d[14]"
                    IAV = "d[15]"
                    IASUS = "d[16]"
                    IAU = "d[17]"
                    RP = "d[18]"
                    RS = "d[19]"
                    CPUC = "d[20]"
                    CPUDST = "d[21]"
                    CPUDCPU = "d[22]"
                    CPUDCPUS = "d[23]"
                    CPUDTPP = "d[24]"
                    CPUDTC = "d[25]"
                    CPUDTLP = "d[26]"
                    DFS = "d[27]"
                    HCPUP = "d[28]"
                    HMP = "d[29]"
                    HU = "d[30]"
                    IPA = "d[31]"
                    TCNATIPA = "d[32]"
                    LLIU = "d[33]"
                    LPP = "d[34]"
                    LPN = "d[35]"
                    LPLP = "d[36]"
                    LSC = "d[37]"
                    MACA = "d[38]"
                    MC = "d[39]"
                    openPort = "d[40]"
                    OSDN = "d[41]"
                    OSDPath = "d[42]"
                    OSDS = "d[43]"
                    OSDT = "d[44]"
                    OSDP = "d[45]"
                    PON = "d[46]"
                    Uptime = "d[47]"
                    USBWP = "d[48]"
                    UA = "d[49]"
                    ADQLLIUD = "d[50]"
                    ADQLLIUN = "d[51]"
                    ADQLLIUT = "d[52]"
                DFL.append([CI, CN, LR, DTS, DUS, OP, OS, IV, CT, IP, LPC, EPC, RUS, RTS, IA, IAV, IASUS, IAU, RP, RS, CPUC,
                            CPUDST, CPUDCPU, CPUDCPUS, CPUDTPP, CPUDTC, CPUDTLP, DFS, HCPUP, HMP, HU, IPA, TCNATIPA, LLIU,
                            LPP, LPN, LPLP, LSC, MACA, MC, openPort, OSDN, OSDPath, OSDS, OSDT, OSDP, PON, Uptime, USBWP,
                            UA, ADQLLIUD, ADQLLIUN, ADQLLIUT])

        if dataType == 'statistics':
            DFC = ['id', 'assetItem', 'os', 'yesterdayDriveSize', 'twodaysagoDriveSize', 'ip', 'yesterdayListenPortCount',
                   'twodaysagoListenPortCount', 'yesterdayEstablishedPort', 'twodaysagoEstablishedPort', 'lastLogin']
            if InputPlugin == 'DB':
                for d in data:
                    CID = d[0]
                    AI = d[1]
                    AIPer = AI.lower()
                    if AIPer.startswith('macbook'):
                        AI = 'Notebook'
                    if AI.startswith('imac'):
                        AI = 'Desktop'
                    OI = d[2]

                    # TDTS = d[3]
                    TDTS = []
                    YDTS = []
                    DTS_item = []
                    DUS_item = []
                    DTS_sum = 0
                    DUS_sum = 0
                    DTS_result = 0
                    DUS_result = 0
                    ##############################Drive Total Size####################################
                    list = str(d[3]).split(',')
                    if "current result unavailable" in list[0]:
                        DTS_item.append(list[0])
                    else:
                        if len(list) == 1:
                            a = list[0].split(' ')
                            DTS_item.append(a)
                        elif len(list) > 1:
                            for i in list:
                                a = i.split(' ')
                                DTS_item.append(a)
                        for x in DTS_item:
                            if len(x) == 3:
                                if ('KB' in x[2]):
                                    DTS_result = int(x[1])
                                elif ('MB' in x[2]):
                                    DTS_result = int(x[1]) * 1024
                                elif ('GB' in x[2]):  # 기준
                                    DTS_result = int(x[1]) * 1024 * 1024
                                elif ('TB' in x[2]):
                                    DTS_result = int(x[1]) * 1024 * 1024 * 1024
                                elif ('PB' in x[2]):
                                    DTS_result = int(x[1]) * 1024 * 1024 * 1024 * 1024
                            elif len(x) == 2:
                                if ("K" in x[1].upper()):
                                    a = x[1].upper().find("K")
                                    DTS_result = float(x[1][:a])
                                elif ("M" in x[1].upper()):
                                    a = x[1].upper().find("M")
                                    DTS_result = float(x[1][:a]) * 1024
                                elif ("G" in x[1].upper()):
                                    a = x[1].upper().find("G")
                                    DTS_result = float(x[1][:a]) * 1024 * 1024
                            DTS_sum += DTS_result

                    items = round(DTS_sum / 1024 / 1024)
                    TDTS.append(str(items) + "KB")

                    # YDTS = d[4]
                    list = str(d[4]).split(',')
                    if "current result unavailable" in list[0]:
                        DUS_item.append(list[0])
                    else:
                        if len(list) == 1:
                            a = list[0].split(' ')
                            DUS_item.append(a)
                        elif len(list) > 1:
                            for i in list:
                                a = i.split(' ')
                                DUS_item.append(a)
                        for x in DUS_item:
                            if len(x) == 3:
                                if ('KB' in x[2]):
                                    DUS_result = int(x[1])
                                elif ('MB' in x[2]):
                                    DUS_result = int(x[1]) * 1024
                                elif ('GB' in x[2]):  # 기준
                                    DUS_result = int(x[1]) * 1024 * 1024
                                elif ('TB' in x[2]):
                                    DUS_result = int(x[1]) * 1024 * 1024 * 1024
                                elif ('PB' in x[2]):
                                    DUS_result = int(x[1]) * 1024 * 1024 * 1024 * 1024
                            elif len(x) == 2:
                                if ("K" in x[1].upper()):
                                    a = x[1].upper().find("K")
                                    DUS_result = float(x[1][:a])
                                elif ("M" in x[1].upper()):
                                    a = x[1].upper().find("M")
                                    DUS_result = float(x[1][:a]) * 1024
                                elif ("G" in x[1].upper()):
                                    a = x[1].upper().find("G")
                                    DUS_result = float(x[1][:a]) * 1024 * 1024
                            DUS_sum += DUS_result
                    items = round(DUS_sum / 1024 / 1024)
                    YDTS.append(str(items) + "KB")

                    IP = d[5]
                    TLPC = d[6]
                    YLPC = d[7]
                    TEP = d[8]
                    YEP = d[9]
                    # TRUS = d[10]
                    # TRTS = d[11]
                    if type(d[10]) != float and d[10] != '[current result unavailable]':
                        LSA = datetime.strptime(d[10].replace('-', '+').split(' +')[0], "%a, %d %b %Y %H:%M:%S")
                    DFL.append([CID, AI, OI, TDTS, YDTS, IP, TLPC, YLPC, TEP, YEP, LSA])
            if InputPlugin == 'ES':
                data = data.dropna(axis=0)
                for i in range(len(data.id)):
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
    except :
        logging.warning('Error running Tanium '+dataType+' Data Transform (Data Frame) plugin')

def zplug_in(data, InputPlugin, dataType):
    if dataType == 'source':
        DL = data['dataList']

        DFC = ['zabbix_name', 'zabbix_description', 'zabbix_ip', 'zabbix_up_time', 'zabbix_process_num',
               'zabbix_disk_used', 'zabbix_mem_used', 'zabbix_cpu_used', 'zabbix_agent_ver', 'zabbix_agent_run']
        DFL = []
        for d in DL:
            if InputPlugin == 'API':
                IP = d['ip']
                if d['itemname'] == "System name":
                    SN = d['value']
                if d['itemname'] == "System description":
                    OS = d['value'].split(' ')[0]
                if d['itemname'] == "System uptime":
                    UT = d['value']
                if d['itemname'] == "Number of processes":
                    PN = d['value']
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
def vul_plug_in(data, dataType):
    try:
        cpu_dict = {}
        weak_dict = {}
        status_list = []
        value_list = []
        cid_list = []
        cpn_list = []
        ct_list = []
        ip_list = []
        lr_list = []
        os_list = []
        swv_list = []
        date_list = []
        logging.info('Tanium ' + dataType + ' Data Transform(Dataframe) Plug In Start')
        for i in data['dataList'] :
            for j in i['list'] :
                if 'cid' in i :
                    cid_list.append(i['cid'])
                if 'cpn' in i :
                    cpn_list.append(i['cpn'])
                if 'ct' in i :
                    ct_list.append(i['ct'])
                if 'ip' in i :
                    ip_list.append(i['ip'])
                if 'lr' in i :
                    lr_list.append(i['lr'])
                if 'os' in i :
                    os_list.append(i['os'])
                if 'status' in j :
                    status_list.append(j['status'])
                else :
                    status_list.append('TSE-Error')
                if 'value' in j :
                    value_list.append(j['value'])
                else :
                    value_list.append('TSE-Error')
                if 'SWV' in j :
                    swv_list.append(j['SWV'])
                else :
                    swv_list.append('TSE-Error')
                date_list.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logging.info('Completing list operations for putting into a data frame')
        
        weak_dict['computer_id'] = cid_list
        weak_dict['vulnerability_code'] = swv_list
        weak_dict['vulnerability_judge_result'] = status_list
        weak_dict['vulnerability_judge_update_time'] = date_list
        weak_dict['vulnerability_judge_reason'] = value_list
        weak_dict['computer_name'] = cpn_list
        weak_dict['chassis_type'] = ct_list
        weak_dict['tanium_client_nat_ip_address'] = ip_list
        weak_dict['last_reboot'] = lr_list
        weak_dict['operating_system'] = os_list
        
        DF = pd.DataFrame(weak_dict)
        DF = DF.astype({'computer_id': 'object'})
        DF = DF.astype({'vulnerability_judge_update_time': 'datetime64'})
        logging.info('Tanium ' + dataType + ' Data Transform(Dataframe) Plug In Finish')

        return DF
    except:
        logging.warning('Error running Tanium '+dataType+' Data Transform (Data Frame) plugin')