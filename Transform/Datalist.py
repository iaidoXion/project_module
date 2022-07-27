import json
import pandas as pd
import numpy as np

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

def dataList(data) :
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



