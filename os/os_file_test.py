# coding:utf-8
# 测试os模块中操作文件或目录的方法
import os

###########################获取文件和文件夹相关信息###################################
print(os.name)      #win : nt       linux或unix : posix  系统名称
print(os.sep)       #win : \        linux或unix : /      路径分隔符
print(repr(os.linesep))     #win : \r\n     linux-->\n\  换行符
print(os.stat("os_file_test.py"))    #获得文件信息

###########################关于工作目录的操作########################################
print(os.getcwd())      #打印当前的工作目录
os.chdir("H:\PyLab\PyTest")     #改变当前的工作目录

###########################创建目录、创建多级目录、删除###############################
#os.mkdir("os_test")        #相对路径都是相对于当前的工作目录
os.rmdir("os_test")
os.makedirs("d:\电影\港台\周星驰")     #创建多级目录
os.removedirs("d:\电影\港台\周星驰")   #只能删除空目录
os.makedirs("../音乐/香港/刘德华")     #../指的是上一级目录
os.rename("电影","movie")             #重命名

dirs= os.listdir("movie")            #列出movie的子目录
print(dirs)