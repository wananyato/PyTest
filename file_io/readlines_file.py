a = ["左航伟\n", "王宇\n", "love you more\n"]
b = enumerate(a)
print(a)
print(b)
print(list(b))

c = [temp.rstrip()+" #"+str(index) for index, temp in enumerate(a)]
with open(r"d:\aini.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
print(c)