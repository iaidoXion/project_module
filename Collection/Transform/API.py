import json

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']


def AssetOrgDaily(BADL):
    PDLC = len(BADL)
    DFL = []
    assetDataList = []
    for i in range(PDLC):
        CI = BADL[i]['computer_id']
        AI = BADL[i]['asset_item']
        OI = BADL[i]['os_platform']
        DI = BADL[i]['disk_total_space']
        LI = BADL[i]['last_seen_at'].split('T')[0]
        AIPer = AI.lower()
        if AIPer.startswith('macbook'):
            AI = 'Notebook'
        if AIPer.startswith('imac'):
            AI = 'Desktop'
        DFL.append([CI, AI, OI, DI, LI])

        assetDataList.append({'computer_id': CI, 'asset_item': AI, 'os_platform': OI, 'disk_total_space': DI, 'last_seen_at': LI})
    returnDataList = assetDataList
    return returnDataList









