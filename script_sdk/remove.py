import os
import shutil

have_path = "D:\\datasets\\Face++\\res_txt2"
all_path = "D:\\datasets\\Face++\\plate_data"
to_path = "D:\\datasets\\Face++\\error2"
havelist = os.listdir(have_path)
alllist = os.listdir(all_path)
for need in alllist:
    need2 = need.replace('.jpg','.txt')
    if need2 not in havelist:
        shutil.copy(os.path.join(all_path,need),os.path.join(to_path,need))
