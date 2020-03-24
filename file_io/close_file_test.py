try:
    f = open(r"d:\ax.txt", "a")
    str = ["wananyato", "camelia", "love you more"]
    f.writelines(str)
except BaseException as e:
    print(e)
finally:
    f.close()           # 关闭文件之前会自动调用flush()将缓冲区的内容写入文件中。
