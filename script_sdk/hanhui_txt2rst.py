import os
import pandas as pd
import numpy as np

def csv2dict(dictscvpath):
    df = pd.read_csv(dictscvpath)
    key =[]
    value = []
    for i in df["id"]:
        key.append(i)
    for j in df["uid"]:
        value.append(j)
    uid_dict = dict(zip(key,value))
    return uid_dict

def txt2rst(restxt,resrst,uid_dict):
    with open(resrst,'a') as rr:
        with open(restxt,'r') as rt:
            txtlines = rt.readlines()
            for txtline in txtlines:
                # print(line)
                try:
                    imgname = txtline.split('-')[0].split('/')[-1]
                    faceinfo = txtline.split('-')[-1]
                    face_id = faceinfo.split(':')[2].split(';')[0]
                    
                    face_uid = uid_dict[int(face_id)]
                    # print(face_uid)
                    face_score = float(faceinfo.rstrip().split(':')[-1])
                    face_score /= 100.0
                    # print(face_score)
                    newinfo = imgname+','+str(face_uid)+','+str(face_score)+'\n'
                    rr.write(newinfo)
                    # print(newinfo)

                except:
                    continue
                

        rt.close()
    rr.close()







dictscvpath = "D:\\datasets\\face10000002\\ku\\2021-12-13_14-05-35\\2021-12-13_14-05-35.csv"
restxt = "D:\\datasets\\face10000002\\20211016175640.txt"
resrst = "D:\\datasets\\face10000002\\20211016175640.rst"
uid_dict = csv2dict(dictscvpath)
txt2rst(restxt,resrst,uid_dict)
# print(uid_dict)
