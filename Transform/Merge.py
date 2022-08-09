import json
import pandas as pd
from datetime import datetime, timedelta
yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
twodaysago = (datetime.today() - timedelta(2)).strftime("%Y%m%d")
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())


def plug_in(data) :
    yDFL = []
    yDFC = ['id', 'lastLogin', 'yesterdayDriveSize', 'os', 'assetItem', 'ip', 'yesterdayListenPortCount', 'yesterdayEstablishedPort','yesterdayRamUseSize', 'yesterdayRamTotalSize']
    twDFL= []
    twDFC = ['id', 'twodaysagoDriveSize', 'twodaysagoListenPortCount',  'twodaysagoEstablishedPort']
    for ydata in data['yesterday'] :
        yDFL.append(
            [ydata['Computer ID'],
             ydata['Last Reboot'],
             ydata['Disk Used Space'],
             ydata['OS Platform'],
             ydata['Chassis Type'],
             ydata['IPv4 Address'],
             ydata['Listen Port Count'],
             ydata['Established Port Count'],
             ydata['Used Memory'],
             ydata['Total Memory']]
        )
    for twodata in data['twodaysago']:
        twDFL.append([twodata['Computer ID'], twodata['Disk Used Space'], twodata['Listen Port Count'],twodata['Established Port Count']])
    twDF = pd.DataFrame(twDFL, columns=twDFC)
    yDF = pd.DataFrame(yDFL, columns=yDFC)

    mdf = pd.merge(left=yDF, right=twDF, how="outer",on=['id'])
    return mdf
