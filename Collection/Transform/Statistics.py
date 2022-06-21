import json

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())

DataLoadingType = SETTING['MODULE']['DataLoadingType']

def Daily(ASDCL) :

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
            LCL.append("login_history")
        DSCL = []
        for DSSC in range(len(ASDCL['DSS']['name'])):
            DSCL.append("drive_size")
        LPCSL = []
        for LPCC in range(len(ASDCL['LPCS']['name'])):
            LPCSL.append("listen_port_count")
        EPSL = []
        for EPC in range(len(ASDCL['EPS']['name'])):
            EPSL.append("established_port")

        DC = AACL+AICL+OCL+LCL+DSCL+LPCSL+EPSL
        DNM = ASDCL['AA']['name']+ASDCL['AIS']['name']+ASDCL['OS']['name']+ASDCL['LS']['name']+ASDCL['DSS']['name']+ASDCL['LPCS']['name']+ASDCL['EPS']['name']
        DV = ASDCL['AA']['value']+ASDCL['AIS']['value']+ASDCL['OS']['value']+ASDCL['LS']['value']+ASDCL['DSS']['value']+ASDCL['LPCS']['value']+ASDCL['EPS']['value']
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













