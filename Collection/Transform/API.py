import json
import pandas as pd
import numpy as np

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']


def dataframe(data, day, dataType) :
    DFL = []
    if data['resCode'] == 200 :
        DL = data['dataList']
        if day == 'today' :
            if dataType == 'asset' :
                DFC = ['computer_id', 'asset_item', 'os_platform', 'drive_use_size', 'last_seen_at', 'ip_address']
                for i in range(len(DL)) :
                    CI = DL[i]['computer_id']
                    AI = DL[i]['asset_item']
                    OI = DL[i]['os_platform']
                    DI = DL[i]['drive_use_size']
                    LI = DL[i]['last_seen_at'].split('T')[0]
                    II = DL[i]['ip_address']
                    AIPer = AI.lower()
                    if AIPer.startswith('macbook'):
                        AI = 'Notebook'
                    if AIPer.startswith('imac'):
                        AI = 'Desktop'
                    DFL.append([CI, AI, OI, DI, LI, II])
            elif dataType == 'sensor' :
                DFC = ['computer_id', 'listen_port_count', 'established_port_count', 'ram_use_size', 'ram_total_size']
                for i in range(len(DL)):
                    CI = DL[i][0]
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
                    if RUS.isdigit() :
                        RUS = int(RUS)
                    else:
                        RUS = 0

                    RTS = DL[i][13].split(' ')[0]
                    if RTS.isdigit():
                        RTS = int(RTS)
                    else:
                        RTS = 0
                    #RTS = DL[i][13].split(' ')[0]
                    #if RTS.isdigit() :
                    #    RTS = int(RUS)
                    #else:
                    #    RTS = 0
                    DFL.append([CI, LPI, EPI, RUS, RTS])
                    #print(DL[i])
        DF = pd.DataFrame(DFL, columns=DFC)
        #print(DF)
        return DF

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



