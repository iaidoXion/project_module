from datetime import datetime, timedelta
import json
import pandas as pd
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
AlarmRamUsage = SETTING['MODULE']['RamUsage']


def DailyCount(TSDL):

    ATNM = "all"
    ATC = len(TSDL)
    weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")

    DF = TSDL
    LLNM = "no_change"
    LLNC = len(DF[(DF['lastLogin'] < weekAgo)])

    AIDL = []
    for d in range(len(TSDL.id)) :
        AI = TSDL.assetItem[d]
        if AI == 'Desktop' or AI == 'Notebook' or AI == 'Virtual' or AI == 'Rack Mount Chassis':
            AI = AI
        else :
            AI = 'Other'
        AIDL.append([AI])
    AIDF = pd.DataFrame(AIDL, columns=['assetItem'])
    AIG = AIDF.groupby(['assetItem'])
    AIGBR = AIG.size().reset_index(name='counts')
    AINM = AIGBR.assetItem
    AIC = AIGBR.counts

    OSDL = []
    for j in range(len(TSDL.id)):
        os = TSDL.os[j]
        if os == 'Linux' or os == 'Mac' or os == 'Windows' :
            os = os
        else:
            os = 'Other'
        OSDL.append([os])
    OSDF = pd.DataFrame(OSDL, columns=['os'])
    OSG = OSDF.groupby(['os'])
    OSGBR = OSG.size().reset_index(name='counts')
    OSNM = OSGBR.os
    OSC = OSGBR.counts


    RUSC = 0
    DC = ATC-len(TSDL.todayDriveSize.compare(TSDL.yesterdayDriveSize))
    LPCC = ATC-len(TSDL.todayListenPortCount.compare(TSDL.yesterdayListenPortCount))
    EPC = ATC-len(TSDL.todayEstablishedPort.compare(TSDL.yesterdayEstablishedPort))

    for i in range(len(TSDL.id)) :
        todayRamTotalSize = TSDL.todayRamTotalSize[i].split(' ')[0]
        todayRamUseSize = TSDL.todayRamUseSize[i].split(' ')[0]
        if todayRamTotalSize.isdigit() :
            todayRamTotalSize = int(todayRamTotalSize)
        else :
            todayRamTotalSize = 0
        if todayRamUseSize.isdigit() :
            todayRamUseSize = int(todayRamUseSize)
        else :
            todayRamUseSize = 0

        if todayRamTotalSize != 0 and todayRamUseSize != 0 :
            usage = (todayRamUseSize / todayRamTotalSize) * 100
            if usage < AlarmRamUsage:
                RUSC = RUSC+1
    RUSC = ATC - RUSC

    DSNM = "no_change"
    DSNC = DC

    LPCNM = "no_change"
    LPCNC = LPCC

    EPNM = "no_change"
    EPNC = EPC

    RUSNM = "no_change"
    RUSNC = RUSC



    RD = {
        "AA": {"name": [ATNM], "value": [ATC]},
        "AIS" : {"name": AINM.tolist(), "value": AIC.tolist()},
        "OS" : {"name": OSNM.tolist(), "value": OSC.tolist()},
        "LS" : {"name": [LLNM], "value": [LLNC]},
        "DSS" : {"name" : [DSNM], "value": [DSNC]},
        "LPCS" : {"name" : [LPCNM], "value": [LPCNC]},
        "EPS" : {"name" : [EPNM], "value": [EPNC]},
        "RUS" : {"name" : [RUSNM], "value": [RUSNC]},
    }

    return RD







