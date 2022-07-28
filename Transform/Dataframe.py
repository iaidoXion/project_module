import json
import pandas as pd
from datetime import datetime
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

def dataframe(data, day, dataType, InputPlugin) :
    DFL = []
    if data['resCode'] == 200 :
        DL = data['dataList']
        if day == 'today' :
            if dataType == 'asset' :
                DFC = ['computer_id', 'asset_item', 'os_platform', 'drive_use_size', 'last_seen_at', 'ip_address']
                for d in DL :
                    if InputPlugin == 'API' :
                        CI = d['computer_id']
                        AI = d['asset_item']
                        OI = d['os_platform']
                        DI = d['drive_use_size']
                        LI = d['last_seen_at'].split('T')[0]
                        II = d['ip_address']
                    elif InputPlugin == 'ES' :
                        CI = d['Computer ID']
                        AI = d['Chassis Type']
                        OI = d['OS Platform']
                        DI = d['Disk Used Space'].split(' ')[1]
                        dateString = d['Last Reboot'].split('+')[0]
                        dateFormatter = "%a, %d %b %Y %H:%M:%S "
                        LI = datetime.strptime(dateString, dateFormatter)
                        II = d['IPv4 Address']
                    AIPer = AI.lower()
                    if AIPer.startswith('macbook'):
                        AI = 'Notebook'
                    if AIPer.startswith('imac'):
                        AI = 'Desktop'
                    DFL.append([CI, AI, OI, DI, LI, II])



            elif dataType == 'sensor' :
                DFC = ['computer_id', 'listen_port_count', 'established_port_count', 'ram_use_size', 'ram_total_size']
                for i in range(len(DL)):
                    CI = DL[i][0]
                    LPI = DL[i][10]
                    if len(LPI) > 10:
                        LPI = '0'
                    else:
                        LPI = DL[i][10]
                    EPI = DL[i][11]
                    if len(EPI) > 10:
                        EPI = '0'
                    else:
                        EPI = DL[i][11]
                    RUS = DL[i][12].split(' ')[0]
                    if RUS.isdigit() :
                        RUS = int(RUS)
                    else:
                        RUS = 0

                    RTS = DL[i][13].split(' ')[0]
                    if RTS.isdigit():
                        RTS = int(RTS)
                    else:
                        RTS = 0
                    #RTS = DL[i][13].split(' ')[0]
                    #if RTS.isdigit() :
                    #    RTS = int(RUS)
                    #else:
                    #    RTS = 0
                    DFL.append([CI, LPI, EPI, RUS, RTS])
                    #print(DL[i])
        DF = pd.DataFrame(DFL, columns=DFC)
        #print(DF)
        return DF





