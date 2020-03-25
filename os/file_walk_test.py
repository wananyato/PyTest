# coding=utf-8
# 测试os.walk()递归遍历所有子目录和子文件

import os

path = os.getcwd()
print(path)
list_file =  os.walk(path)

for dirpath,dirnames,filenames in list_file:
    for dir in dirnames:
        print(dir)
    for file in filenames:
        print(file)
