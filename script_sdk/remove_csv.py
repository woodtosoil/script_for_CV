import os
import shutil
from typing import ClassVar
import pandas as pd

csv_path = r"D:\datasets\face10000002\10000002.csv"

all_path = "D:\\datasets\\face10000002\\face10000002\\"
to_path = "D:\\datasets\\face10000002\\test\\"

csv_data = pd.read_csv(csv_path)
# print(csv_data)
for i in range(len(csv_data)):
    if str(csv_data['uid'][i]) == '0':
        img_name = csv_data['image'][i]
        new_name = str(csv_data['uid'][i])+'.jpg'
        shutil.copy(all_path+img_name,to_path+img_name)
# alllist = os.listdir(all_path)
# for need in alllist:
#     need2 = need.replace('.jpg','.txt')
#     if need2 not in havelist:
#         shutil.copy(os.path.join(all_path,need),os.path.join(to_path,need))
