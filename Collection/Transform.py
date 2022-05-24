import pandas as pd
import json

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']


def AssetOrgDaily(parserData):
    PDLC = len(parserData)
    DFL = []
    assetDataList = []
    for i in range(PDLC):
        CI = parserData[i]['computer_id']
        AI = parserData[i]['asset_item']
        OI = parserData[i]['os_platform']
        DI = parserData[i]['disk_total_space']
        LI = parserData[i]['last_seen_at'].split('T')[0]
        AIPer = AI.lower()
        if AIPer.startswith('macbook'):
            AI = 'Notebook'
        if AIPer.startswith('imac'):
            AI = 'Desktop'
        DFL.append([CI, AI, OI, DI, LI])

        assetDataList.append({'computer_id': CI, 'asset_item': AI, 'os_platform': OI, 'disk_total_space': DI, 'last_seen_at': LI})
    returnDataList = assetDataList
    return returnDataList

def AssetDaily(TEDL):
    DL=[]
    if DataLoadingType == 'DB':
        ADL = TEDL
    elif DataLoadingType == 'FILE':
        ADL = TEDL['data']
    for AssetData in ADL:
        if DataLoadingType == 'DB':
            CID = AssetData[0]
            AI = AssetData[1]
            OI = AssetData[2]
            TDTS = AssetData[3]
            YDTS = AssetData[4]
            LSA = AssetData[5]
        elif DataLoadingType == 'FILE':
            CID = AssetData['computer_id']
            AI = AssetData['asset_item']
            OI = AssetData['os_platform']
            TDTS = AssetData['disk_total_space']
            LSA = AssetData['last_seen_at']
        DL.append([CID, AI, OI, TDTS, YDTS, LSA])

    DFCNM = ['id', 'assetItem', 'os', 'todayDriveSize', 'yesterdayDriveSize', 'lastLogin']
    DF = pd.DataFrame(DL, columns=DFCNM)
    #print(DF)
    return DF

def StatisticsDaily(ASDCL) :

    if DataLoadingType == 'DB':
        AACL = []
        for AASC in range(len(ASDCL['AA']['name'])):
            AACL.append("asset")
        AICL = []
        for AISC in range(len(ASDCL['AIS']['name'])):
            AICL.append("asset")
        OCL = []
        for OSC in range(len(ASDCL['OS']['name'])):
            OCL.append("os")
        LCL = []
        for LSC in range(len(ASDCL['LS']['name'])):
            LCL.append("login")
        DSCL = []
        for DSSC in range(len(ASDCL['DSS']['name'])):
            DSCL.append("drive")
        DC = AACL+AICL+OCL+LCL+DSCL
        DNM = ASDCL['AA']['name']+ASDCL['AIS']['name']+ASDCL['OS']['name']+ASDCL['LS']['name']+ASDCL['DSS']['name']
        DV = ASDCL['AA']['value']+ASDCL['AIS']['value']+ASDCL['OS']['value']+ASDCL['LS']['value']+ASDCL['DSS']['value']
        returnData = {"classification" : DC, "item" : DNM, "count" : DV}

    elif DataLoadingType == 'FILE':
        AASDL = []
        for AASC in range(len(ASDCL['AA']['name'])) :
            AASDL.append({"classification": "asset", "item": ASDCL['AA']['name'][AASC], "count": ASDCL['AA']['value'][AASC]})
        AISDL = []
        for AISC in range(len(ASDCL['AIS']['name'])) :
            AISDL.append({"classification": "asset", "item": ASDCL['AIS']['name'][AISC], "count": ASDCL['AIS']['value'][AISC]})
        OSDL = []
        for OSC in range(len(ASDCL['OS']['name'])) :
            OSDL.append({"classification": "os", "item": ASDCL['OS']['name'][OSC], "count": ASDCL['OS']['value'][OSC]})
        LSDL =[]
        for LSC in range(len(ASDCL['LS']['name'])):
            LSDL.append({"classification": "login", "item": ASDCL['LS']['name'][LSC], "count": ASDCL['LS']['value'][LSC]})
        returnData = {"AAS" : AASDL, "AIS" : AISDL, "OS" : OSDL, "LS" : LSDL}

    return returnData













