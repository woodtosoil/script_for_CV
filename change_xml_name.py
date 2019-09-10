# coding=utf-8
import os
import os.path
import xml.dom.minidom

#获得文件夹中所有文件
FindPath = '/home/djw/Fine-grained-erro/err/annotations/'
FileNames = os.listdir(FindPath)
s = []
xml_path = '/home/djw/Fine-grained-erro/err/new/'
for file_name in FileNames:
    if not os.path.isdir(file_name):  # 判断是否是文件夹,不是文件夹才打开
        print(file_name)

    #读取xml文件
    dom = xml.dom.minidom.parse(os.path.join(FindPath,file_name))

    root = dom.documentElement

    # 获取标签对name之间的值
    name = root.getElementsByTagName('name')
    for i in range(len(name)):
        print(name[i].firstChild.data)
        if name[i] .firstChild.data== 'Electromobile':
            name[i].firstChild.data = 'Electrombile'
            print('修改后的 name')
            print(name[i].firstChild.data)
    #将修改后的xml文件保存
    with open(os.path.join(xml_path, file_name), 'w') as fh:
        dom.writexml(fh)
        print('写入name/pose OK!')

