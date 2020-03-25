# coding=utf-8
import os

path = os.getcwd()
file_list = os.listdir(path)
for filename in file_list:
    if filename.endswith("py"):
        print(filename)

print("#########################################")

file_list2 = [filename for filename in os.listdir(path) if filename.endswith("py")]
for f in file_list2:
    print(f,end=",")