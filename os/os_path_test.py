# coding=utf-8
import os
import os.path
# from os import path

print(os.path.isabs("d:/a.txt"))    #判断是否为绝对路径
print(os.path.isdir("d:/a.txt"))    #判断是否为文件夹
print(os.path.isfile("d:/a.txt"))   #判断是否为文件
print(os.path.exists("d:/a.txt"))   #判断文件是否存在

###############获得文件基本信息####################

print(os.path.getsize("d:/a.txt"))  #获取文件大小
print(os.path.abspath("d:/a.txt"))
print(os.path.dirname("d:/a.txt"))
print(os.path.getctime("d:/a.txt"))
print(os.path.getatime("d:/a.txt"))
print(os.path.getmtime("d:/a.txt"))


################对路径的操作#########################

path = os.path.abspath("a.txt")
print(os.path.split(path))
print(os.path.splitext(path))

print(os.path.join("aa","bb","cc"))