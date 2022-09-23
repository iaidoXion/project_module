from ctypes import sizeof
from os.path import getsize

import pandas as pd

import json
import sys
import os
import time
from filesplit.split import Split

from datetime import datetime, timedelta

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TSoIPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['Storage']
TSoIPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileName']
TSoIPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileType']

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")


def plug_in():
    try:
        """
        FileFullName = TSoIPFS+TSoIPFNM+'2022-09-14_900'+TSoIPFT
        with open(FileFullName, encoding="UTF-8") as ADF:
            ADL = json.loads(ADF.read())
        df = ADL[0]['rows']
        return {'dataList': df}
        """

        start = time.process_time()
        a = '{"rows":'
        b = "}"
        with open(TSoIPFS + 'Sample.json') as infile:
            o = json.load(infile)
            print(len(o['rows']))
            chunkSize = 620
            for i in range(0, len(o['rows']), chunkSize):
                print(i)
                with open('./data/asset/daily/hh/devi' + str(i // chunkSize) + '.json', 'w') as outfile:
                    outfile.write(a)
                    json.dump(o['rows'][i:i + chunkSize], outfile)
                    outfile.write(b)

        end = time.process_time()

        print("Time elapsed :", end - start)
        print("Time elapsed :", timedelta(seconds=end - start))

        # #
        # with open(TSoIPFS + 'data.json', 'r', encoding="UTF-8") as ADF:
        #
        #     F=json.load(ADF)
        #
        #     x = 0
        #     for line in F['rows']:
        #         x+=1
        #         o = open('./data/asset/daily/hh/devi' + str(x) + '.json', 'w', encoding='utf-8')
        #
        #         json.dump(line , o)
        #         print(sys.getsizeof(line))
        #         o.close()

        # f=open(TSoIPFS + 'data.json', 'r', encoding="UTF-8")
        #
        # while True:
        #     c=[]
        #     line = f.readline()
        #     print(line)
        #     c= line
        #     if not line:
        #         break
        # with open(TSoIPFS + 'data3.json', 'w', encoding='utf-8') as ADL:
        #     json.dump(c, ADL)
        #

        # 2 . id로 일단 나눔
        # start =time.process_time()
        # with open(TSoIPFS + 'sample.json', 'r', encoding="UTF-8") as ADF:
        #     #a = ADF.read()
        #     #json_data=json.loads(a)
        #     F=json.load(ADF)
        #     #print(F)
        #     #data = ADF.readlines()
        #
        #     #print(data)
        #     # lines= data.readlines()
        #     #print(type(F))
        #     x = 0
        #     for line in F['rows']:
        #
        #         c = []
        #         # #print(line['id'])
        #         #print(line)
        #         # for x in range(0,len(data)) :
        #         #c.appned(line)
        #         # print(F['rows'])
        #
        #         if "id" in line:
        #             x+=1
        #             #print("cddd")
        #             o = open('./data/asset/daily/hh/devi' + str(x) + '.json', 'w', encoding='utf-8')
        #             #print("fgf")
        #             json.dump(line , o)
        #             #print("??")
        #             o.close()
        #
        #
        #         else:
        #             c = c.append(line)
        #             #print("z")
        # end= time.process_time()
        #
        # print("Time elapsed :", end - start )
        # print("Time elapsed :", timedelta(seconds=end-start))
        #

        # if "id" in a :
        #     for x in range(0,len(data)) :
        #
        #         with open(TSoIPFS + 'data'+x+'.json', 'w', encoding='utf-8') as ADL:
        #             #print(json.loads(data))
        #             json.dump(x, ADL)
        #             print(x)
        # else:
        #     print("tq")
        # if "id" in x:
        #     print("hd")
        # else:
        #     print("no")

        # if  json_data['id'] in json_data:
        #     print("1")
        # else:
        #     print(":g")
        # print(json_data)
        # if json_data["rows"][0]["id"]in json_data:
        #     print("1")
        # i =0
        # while i< len(range(0,ADF.readlines())):
        #     print("hg")
        #     i += 1
        #

        # json형태유지 자르기
        # 1.실패.

        # N = 30
        # with open(TSoIPFS+'data.json', encoding="UTF-8") as ADF:
        #     a=ADF.read()
        #     json_data=json.loads(a)
        #     for i in range(0,N):
        #         print(json_data["rows"][i]["id"])
        #         # if a[3] in a :
        #         #     print("gd")
        #         # else:
        #         #     print("gg")
        #     head = [next(ADF) for x in range(N)]
        # print(len(head))
        # for l in head:
        #     print(l)

        # 3. size로 나누기 성공
        # file_name = TSoIPFS + 'sample.json'
        # file_out = "./data/"
        # Split(inputfile=file_name, outputdir=file_out).bysize(size=12800000)

        # 2. 분할이 되는거같은데 1기가가 안나눠짐
        # file_name = TSoIPFS + 'sample.json'
        # file_out = "outputfile"
        #
        #
        # f = open(file_name, 'r', encoding='utf-8')
        # numbits = 128000000
        # loop_num = round(os.stat(file_name).st_size / numbits + 1)
        #
        # print(os.stat(file_name).st_size / numbits + 1)
        # print(os.stat(file_name))
        # print(loop_num)
        #
        # for i in range(0, loop_num):
        #     o = open('./data/' + file_out + str(i) + '.json', 'w', encoding='utf-8')
        #     segment = f.readlines(numbits)
        #     print(len(segment))
        #     for c in range(0, len(segment)):
        #         print(c)
        #         o.write(segment[c] + "\n")
        #         o.close()

        # 1. 연습
        # 용량 체크
        # import os
        #
        # dir_path = "./"
        # f_list = os.listdir(dir_path)
        #
        # for f in f_list:
        #     print("%s file_name : %s / file_size : %s" % (os.path.isdir(f), f, os.path.getsize(f))

        # 줄수로 저장
        # N = 30
        # with open(TSoIPFS+'data.json', encoding="UTF-8") as ADF:
        #     head = [next(ADF) for x in range(N)]
        # print(len(head))
        # for l in head:
        #     print(l)
        #
        # with open(TSoIPFS, 'w', encoding='utf-8') as make_file:
        #     json.dump(l, make_file, indent="\t")
        # ADL = json.loads(ADF.read())
        # print()

        # if "id" in line:
        #     break
        # else:
        #     print()
        # if line in "id":
        #     print("--------------------------------------------------")
        #     print(line)
        #     if
        # while "id" not in line:
        #     print(line)
        # print(line['id'])

        # ADL = json.loads(ADF.read())

        # N = 30
        # with open('input.txt', encoding='utf-8') as myfile:
        #     head = [next(myfile) for x in range(N)]
        # print(len(head))
        # for l in head:
        #     print(l)

        # df = ADL
        #
        #
        # print(df)

        # return df
        # print("time :", time.time() - start)
        # return df
        # with open(TSoIPFS + FileFullName, encoding="UTF-8") as ADF:
        #    ADL = json.loads(ADF.read())
        # AssetSelectL = ADL
        # print(len(AssetSelectL['dataList']))

        """AS = BS['asset']
        Storage = AS['Storage']
        FNM = AS['FileName'] + yesterday
        FT = AS['FileType']
        FileFullName = FNM + FT
        with open(Storage + FileFullName, encoding="UTF-8") as ADF:
            ADL = json.loads(ADF.read())
        AssetSelectL = ADL
        return AssetSelectL"""
    except:
        print('Asset Daily Table connection(Select) Failure')