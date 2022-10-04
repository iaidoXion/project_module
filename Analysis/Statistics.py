from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json
import pandas as pd
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())


def DailyCount(TSDL):
    now = datetime.now()
    ATNM = "all"
    ATC = len(TSDL)
    six_month_str = (now - relativedelta(months=6)).strftime("%Y-%m-%d %H:%M:%S")
    six_month = datetime.strptime(six_month_str, '%Y-%m-%d %H:%M:%S')

    DF = TSDL
    LLNM = "no_change"

    LLNC = len(DF[(DF['lastLogin'] < six_month)])
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
    #print(RD)
    return RD