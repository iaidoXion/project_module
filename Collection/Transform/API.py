import json
import pandas as pd
import numpy as np

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']


def AssetOrgDaily(BADL, BSDL):
    PDLC = len(BADL)
    ADDFL = []
    assetDataList = []
    for i in range(PDLC):
        CI = BADL[i]['computer_id']
        AI = BADL[i]['asset_item']
        OI = BADL[i]['os_platform']
        DI = BADL[i]['disk_total_space']
        LI = BADL[i]['last_seen_at'].split('T')[0]
        II = BADL[i]['ip_address']
        AIPer = AI.lower()
        if AIPer.startswith('macbook'):
            AI = 'Notebook'
        if AIPer.startswith('imac'):
            AI = 'Desktop'
        ADDFL.append([CI, AI, OI, DI, LI, II])


    ADDFCNM = ['computer_id', 'asset_item', 'os_platform', 'disk_total_space', 'last_seen_at', 'ip_address']
    ADDF = pd.DataFrame(ADDFL, columns=ADDFCNM)
    #print(ADDF)
    SDDFL = []
    for j in range(len(BSDL)) :
        CI = BSDL[j][0]
        LPI = BSDL[j][10]
        if len(LPI) > 10 :
            LPI = '0'
        else :
            LPI = BSDL[j][10]

        EPI = BSDL[j][11]
        if len(EPI) > 10 :
            EPI = '0'
        else :
            EPI = BSDL[j][11]

        SDDFL.append([CI, LPI, EPI])
    SDDFCNM = ['computer_id', 'listen_port_count', 'established_port_count']
    SDDF = pd.DataFrame(SDDFL, columns=SDDFCNM)


    #print(ADDF.sort_values(by="computer_id", ascending=True).reset_index())
    #print(SDDF.sort_values(by="computer_id", ascending=True).reset_index())
    DFM = pd.merge(left=ADDF, right=SDDF, how="left", on="computer_id")


    computer_id = DFM.computer_id
    asset_item = DFM.asset_item
    os_platform = DFM.os_platform
    disk_total_space = DFM.disk_total_space
    last_seen_at = DFM.last_seen_at
    ip_address = DFM.ip_address
    listen_port_count = DFM.listen_port_count
    established_port_count = DFM.established_port_count
    for k in range(len(computer_id)) :
        CI = computer_id[k]
        AI = asset_item[k]
        OI = os_platform[k]
        DI = disk_total_space[k]
        LI = last_seen_at[k]
        II = ip_address[k]
        LPCI = listen_port_count[k]
        if LPCI :
            if type(LPCI) == float :
                LPCI = '0'
            else:
                LPCI = listen_port_count[k]
        else :
            LPCI = '0'

        EPCI = established_port_count[k]
        if EPCI :
            if type(EPCI) == float :
                EPCI = '0'
            else:
                EPCI = established_port_count[k]
        else :
            EPCI = '0'
        assetDataList.append({'computer_id': CI, 'asset_item': AI, 'os_platform': OI, 'disk_total_space': DI, 'ip_address': II, 'listen_port_count' : LPCI, 'established_port_count' : EPCI, 'last_seen_at': LI})

    returnDataList = assetDataList
    return returnDataList



