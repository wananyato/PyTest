# s_str = ["左航伟", "love", "Camelia\n", "我的媳妇儿！"]
# with open(r"d:\aini.txt", "a", encoding="utf-8") as f:
#     f.writelines(s_str)
with open(r"d:\aini.txt", "r", encoding="utf-8") as f1:
    for a in f1:
        print(a, end="")
    # str1 = f1.read(1)
    # print(str1)
    # str2 = f1.readline()
    # print(str2)
    # str3 = f1.readlines()
    # print(str3)
print("ending!")