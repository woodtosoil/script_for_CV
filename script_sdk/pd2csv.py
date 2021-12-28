from os import write
import sqlite3 as db
import csv
import filecmp

dbpath = "D:\\datasets\\face10000002\\ku\\2021-12-13_14-05-35\\2021-12-13_14-05-35.db"
csvpath = "D:\\datasets\\face10000002\\ku\\2021-12-13_14-05-35\\2021-12-13_14-05-35.csv"

def db2csv(dbpath,csvpath):
    conn = db.connect(dbpath)
    cursor = conn.cursor()
    # sql = """select name from sqlite_master where type='table' order by name"""
    sql = """select * from faceinfo """
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(type(result))
    with open(csvpath,'w',newline='') as fp:
        writer=csv.writer(fp)
        writer.writerows(result)
    conn.close()

db2csv(dbpath,csvpath)