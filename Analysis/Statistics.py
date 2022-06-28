from datetime import datetime, timedelta

def DailyCount(TSDL):
    ATNM = "all"
    ATC = len(TSDL)

    weekAgo = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")

    DF = TSDL
    LLNM = "N"
    LLNC = len(DF[(DF['lastLogin'] < weekAgo)])

    AIG = DF.groupby(['assetItem'])
    AIGBR = AIG.size().reset_index(name='counts')
    AINM = AIGBR.assetItem
    AIC = AIGBR.counts

    OSG = DF.groupby(['os'])
    OSGBR = OSG.size().reset_index(name='counts')
    OSNM = OSGBR.os
    OSC = OSGBR.counts

    DC = 0
    LPCC = 0
    EPC = 0
    for i in range(len(TSDL.id)) :
        if TSDL.todayDriveSize[i] == TSDL.yesterdayDriveSize[i] :
            DC = DC+1

        if str(TSDL.todayListenPortCount[i]) == str(TSDL.yesterdayListenPortCount[i]) :
           LPCC = LPCC+1
        #print(type(TSDL.todayEstablishedPort[i]))
        if TSDL.todayEstablishedPort[i] == 0 :
            EPC = EPC+1



    DSNM = "no_change"
    DSNC = DC

    LPCNM = "no_change"
    LPCNC = LPCC

    EPNM = "N"
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


def Association(TSDL) :
    print(TSDL)





