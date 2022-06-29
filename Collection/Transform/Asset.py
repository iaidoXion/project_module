import pandas as pd
import json

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']


def Daily(EDL):
    #print(EDL)
    DL=[]
    if DataLoadingType == 'DB':
        ADL = EDL
    elif DataLoadingType == 'FILE':
        ADL = EDL['data']
    for AssetData in ADL:
        if DataLoadingType == 'DB':
            CID = AssetData[0]
            AI = AssetData[1]
            OI = AssetData[2]
            TDTS = AssetData[3]
            YDTS = AssetData[4]
            IP = AssetData[5]
            TLPC = AssetData[6]
            YLPC = AssetData[7]
            TEP = AssetData[8]
            YEP = AssetData[9]
            TRUS = AssetData[10]
            YRUS = AssetData[11]
            LSA = AssetData[12]
        elif DataLoadingType == 'FILE':
            CID = AssetData['computer_id']
            AI = AssetData['asset_item']
            OI = AssetData['os_platform']
            TDTS = AssetData['drive_use_size']
            LSA = AssetData['last_seen_at']
        DL.append([CID, AI, OI, TDTS, YDTS, IP, TLPC, YLPC, TEP, YEP, TRUS, YRUS, LSA])

    DFCNM = ['id', 'assetItem', 'os', 'todayDriveSize', 'yesterdayDriveSize', 'ip', 'todayListenPortCount','yesterdayListenPortCount', 'todayEstablishedPort', 'yesterdayEstablishedPort', 'todayRamUseSize', 'yesterdayRamUseSize', 'lastLogin']
    DF = pd.DataFrame(DL, columns=DFCNM)
    #print(DF)
    return DF










