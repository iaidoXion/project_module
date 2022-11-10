from hdfs import InsecureClient

def HDFSInput():
    hdfsIP = 'http://1.223.168.93:40130'
    HIDC = InsecureClient(hdfsIP)
    with HIDC.read('/user/root/kweather_20201009.csv', encoding='utf-8') as MHIDRF:
        MHIDR = MHIDRF.read()
        print(MHIDR)
    MHIDRF.close()
HDFSInput()