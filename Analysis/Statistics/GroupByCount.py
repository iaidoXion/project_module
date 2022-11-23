from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import pandas as pd
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())


def plug_in(data):
    now = datetime.now()
    ATNM = "all"
    ATC = len(data)
    six_month_str = (now - relativedelta(months=6)).strftime("%Y-%m-%d %H:%M:%S")
    six_month = datetime.strptime(six_month_str, '%Y-%m-%d %H:%M:%S')
    LLNM = "no_change"
    LLNC = 0
    #LLNC = len(DF[(DF['lastLogin'] < six_month)])
    for d in data['lastLogin'] :
        if type(d) != str :
            if d < six_month:
                LLNC = LLNC + 1
    AIDL = []
    for d in range(len(data.id)) :
        AI = data.assetItem[d]
        AIDL.append([AI])
    AIDF = pd.DataFrame(AIDL, columns=['assetItem'])
    AIG = AIDF.groupby(['assetItem'])
    AIGBR = AIG.size().reset_index(name='counts')
    AINM = AIGBR.assetItem
    AIC = AIGBR.counts
    #AIG = AIDF.groupby(['assetItem']).size().reset_index(name='counts')
    #AIGS = AIG.sort_values(by="counts", ascending=False).head(3)
    #AINM = AIGS.assetItem
    #AIC = AIGS.counts

    OSDL = []
    for j in range(len(data.id)):
        os = data.os[j]
        OSDL.append([os])
    OSDF = pd.DataFrame(OSDL, columns=['os'])
    OSG = OSDF.groupby(['os'])
    OSGBR = OSG.size().reset_index(name='counts')
    OSNM = OSGBR.os
    OSC = OSGBR.counts


    DC = ATC-len(data.yesterdayDriveSize.compare(data.twodaysagoDriveSize))
    LPCC = ATC-len(data.yesterdayListenPortCount.compare(data.twodaysagoListenPortCount))
    EPC = ATC-len(data.yesterdayEstablishedPort.compare(data.twodaysagoEstablishedPort))

    DSNM = "no_change"
    DSNC = DC

    LPCNM = "no_change"
    LPCNC = LPCC

    EPNM = "no_change"
    EPNC = EPC

    IANDL = []
    for k in range(len(data.id)):
        for i in data.installed_applications_name[k] :
            if i != '0' :
                IANDL.append(i)
    IANDF = pd.DataFrame(IANDL, columns=['IANM'])
    IANDFG = IANDF.groupby(['IANM']).size().reset_index(name='counts')
    IANDFGS = IANDFG.sort_values(by="counts", ascending=False).head(5)
    IANMD = IANDFGS.IANM
    IANMC = IANDFGS.counts
    RD = {
        "AA": {"name": [ATNM], "value": [ATC]},
        "AIS" : {"name": AINM.tolist(), "value": AIC.tolist()},
        "OS" : {"name": OSNM.tolist(), "value": OSC.tolist()},
        "LS" : {"name": [LLNM], "value": [LLNC]},
        "DSS" : {"name" : [DSNM], "value": [DSNC]},
        "LPCS" : {"name" : [LPCNM], "value": [LPCNC]},
        "EPS" : {"name" : [EPNM], "value": [EPNC]},
        "IANM" : {"name" : IANMD.tolist(), "value" : IANMC.tolist()}
    }
    #print(RD)
    return RD