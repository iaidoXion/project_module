from datetime import datetime, timedelta
import json
import pandas as pd
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())


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


    DC = ATC-len(TSDL.yesterdayDriveSize.compare(TSDL.twodaysagoDriveSize))
    LPCC = ATC-len(TSDL.yesterdayListenPortCount.compare(TSDL.twodaysagoListenPortCount))
    EPC = ATC-len(TSDL.yesterdayEstablishedPort.compare(TSDL.twodaysagoEstablishedPort))

    DSNM = "no_change"
    DSNC = DC

    LPCNM = "no_change"
    LPCNC = LPCC

    EPNM = "no_change"
    EPNC = EPC

    RD = {
        "AA": {"name": [ATNM], "value": [ATC]},
        "AIS" : {"name": AINM.tolist(), "value": AIC.tolist()},
        "OS" : {"name": OSNM.tolist(), "value": OSC.tolist()},
        "LS" : {"name": [LLNM], "value": [LLNC]},
        "DSS" : {"name" : [DSNM], "value": [DSNC]},
        "LPCS" : {"name" : [LPCNM], "value": [LPCNC]},
        "EPS" : {"name" : [EPNM], "value": [EPNC]},
    }

    return RD