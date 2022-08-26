import json
import pandas as pd
import numpy as np

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

def plug_in(data) :
    AACL = []
    for AASC in range(len(data['AA']['name'])):
        AACL.append("asset")
    AICL = []
    for AISC in range(len(data['AIS']['name'])):
        AICL.append("asset")
    OCL = []
    for OSC in range(len(data['OS']['name'])):
        OCL.append("os")
    LCL = []
    for LSC in range(len(data['LS']['name'])):
        LCL.append("login_history")
    DSCL = []
    for DSSC in range(len(data['DSS']['name'])):
        DSCL.append("drive_size")
    LPCSL = []
    for LPCC in range(len(data['LPCS']['name'])):
        LPCSL.append("listen_port_count")
    EPSL = []
    for EPC in range(len(data['EPS']['name'])):
        EPSL.append("established_port_count")
    #RUSL = []
    #for RUSC in range(len(data['RUS']['name'])):
    #    RUSL.append("ram_use_size")

    DC = AACL + AICL + OCL + LCL + DSCL + LPCSL + EPSL #+ RUSL
    DNM = data['AA']['name'] + data['AIS']['name'] + data['OS']['name'] + data['LS']['name'] + data['DSS'][
        'name'] + data['LPCS']['name'] + data['EPS']['name'] #+ data['RUS']['name']
    DV = data['AA']['value'] + data['AIS']['value'] + data['OS']['value'] + data['LS']['value'] + data['DSS'][
        'value'] + data['LPCS']['value'] + data['EPS']['value'] #+ data['RUS']['value']
    returnData = {"classification": DC, "item": DNM, "count": DV}
    return returnData
    """
    elif DataLoadingType == 'FILE':
    AASDL = []
    for AASC in range(len(ASDCL['AA']['name'])):
        AASDL.append(
            {"classification": "asset", "item": ASDCL['AA']['name'][AASC], "count": ASDCL['AA']['value'][AASC]})
    AISDL = []
    for AISC in range(len(ASDCL['AIS']['name'])):
        AISDL.append(
            {"classification": "asset", "item": ASDCL['AIS']['name'][AISC], "count": ASDCL['AIS']['value'][AISC]})
    OSDL = []
    for OSC in range(len(ASDCL['OS']['name'])):
        OSDL.append({"classification": "os", "item": ASDCL['OS']['name'][OSC], "count": ASDCL['OS']['value'][OSC]})
    LSDL = []
    for LSC in range(len(ASDCL['LS']['name'])):
        LSDL.append({"classification": "login", "item": ASDCL['LS']['name'][LSC], "count": ASDCL['LS']['value'][LSC]})
    returnData = {"AAS": AASDL, "AIS": AISDL, "OS": OSDL, "LS": LSDL}


    """


    """
    computer_id = data.computer_id
    computer_name = data.computer_name
    last_reboot = data.last_reboot
    disk_total_space = data.disk_total_space
    disk_used_space = data.disk_used_space
    os_platform = data.os_platform
    operating_system = data.operating_system
    is_virtual = data.is_virtual
    chassis_type = data.chassis_type
    ip_address = data.ip_address
    listen_port_count = data.listen_port_count
    established_port_count = data.established_port_count
    ram_use_size = data.ram_use_size
    ram_total_size = data.ram_total_size
    DL = []
    for i in range(len(computer_id)) :
        CI = computer_id[i]
        CN = computer_name[i]
        LR = last_reboot[i]
        DTS = disk_total_space[i]
        DUS = disk_used_space[i]
        OP = os_platform[i]
        OS = operating_system[i]
        IV = is_virtual[i]
        CT = chassis_type[i]
        IP = ip_address[i]
        LPC = listen_port_count[i]
        EPC = established_port_count[i]
        RUS = ram_use_size[i]
        RTS = ram_total_size[i]
        DL.append({'computer_id':CI, 'computer_name':CN, 'last_reboot':LR, 'disk_total_space':DTS, 'disk_used_space':DUS, 'os_platform':OP, 'operating_system':OS,
               'is_virtual':IV, 'chassis_type':CT, 'ip_address':IP, 'listen_port_count':LPC, 'established_port_count':EPC, 'ram_use_size':RUS, 'ram_total_size':RTS})
    return DL
    """
    """
    assetData = data[0]
    sensorData = data[1]
    DF = pd.merge(left=assetData, right=sensorData, how="outer", on="computer_id").sort_values(by="computer_id", ascending=True).reset_index(drop=True)

    DL = []
    computer_id = DF.computer_id
    asset_item = DF.asset_item
    os_platform = DF.os_platform
    drive_use_size = DF.drive_use_size
    last_seen_at = DF.last_seen_at
    ip_address = DF.ip_address
    listen_port_count = DF.listen_port_count
    established_port_count = DF.established_port_count
    ram_use_size = DF.ram_use_size
    ram_total_size = DF.ram_total_size
    for i in range(len(computer_id)):
        CI = computer_id[i]
        AI = asset_item[i]
        OI = os_platform[i]
        DI = drive_use_size[i]
        LI = last_seen_at[i]
        II = ip_address[i]
        LPCI = listen_port_count[i]
        if LPCI:
            if type(LPCI) == float:
                LPCI = '0'
            else:
                LPCI = listen_port_count[i]
        else:
            LPCI = '0'

        EPCI = established_port_count[i]
        if EPCI:
            if type(EPCI) == float:
                EPCI = '0'
            else:
                EPCI = established_port_count[i]
        else:
            EPCI = '0'

        RUSI = ram_use_size[i]
        if pd.isnull(RUSI) :
            RUSI = '0'
        else :
            RUSI = int(ram_use_size[i])

        RTSI = ram_total_size[i]
        if pd.isnull(RTSI):
            RTSI = '0'
        else:
            RTSI = int(ram_total_size[i])

        DL.append({'computer_id': CI, 'asset_item': AI, 'os_platform': OI, 'drive_use_size': DI, 'ip_address': II, 'listen_port_count' : LPCI, 'established_port_count' : EPCI, 'last_seen_at': LI, 'ram_use_size' : RUSI, 'ram_total_size' : RTSI})
    return DL
    """



