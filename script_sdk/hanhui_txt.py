import os
import shutil
import re

one_txt_path = "D:\\datasets\\Face++\\20211015084732.txt"
all_txt_path = "D:\\datasets\\Face++\\hanhui_result\\"


with open(one_txt_path,'r',encoding= 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        # print(line)
        info_list = line.split('-')
        # if info_list[2][0] == 'V':
        img_path = info_list[0]
        loc_info = info_list[1]
        print(img_path)
        try:
            if info_list[2][0]=='V':
                loc_info = re.sub("[()]","", loc_info)
                # loc = re.sub("[[]]","", loc_info)
                loc = loc_info.replace('[','').replace(']','')
                loc_list = loc.split(',')
                # print(loc_list[0])
                txt_name = img_path.split('/')[-1].replace('jpg','txt')
                with open(all_txt_path+txt_name,'a') as f2:
                    f2.write('0')
                    f2.write(' ')
                    f2.write(' '.join(str(loc_list[i]) for i in range(len(loc_list))))
                    f2.write('\n')
                f2.close()
        except:
            continue
f.close()
            



