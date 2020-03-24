try:
    f = open(r"d:\ax.txt", "a")
    str = ["wananyato", "camelia", "love you more"]
    f.writelines(str)
except BaseException as e:
    print(e)
finally:
    f.close()
