

def plug_in(data) :
    alarmDetectionList = []
    for i in range(len(data)) :
        if data.yesterdayDriveSize[i] == data.twodaysagoDriveSize[i] :
            driveSize = '변화없음'
            alarmDetectionList.append([data.id, driveSize])
        else :
            driveSize = '변화있음'
            alarmDetectionList.append([data.id, driveSize])

    print(alarmDetectionList)
            #print(data.yesterdayDriveSize[i])
            #print(data.twodaysagoDriveSize[i])
            #print(data.id[i])
