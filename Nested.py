# 测试嵌套函数（内部函数）的定义
def outer():
    print("outer running")

    def inner():
        print("inner running")

    inner()


def printChinesename(name, familyname):
    print("{0}{1}".format(familyname, name))


def printForginername(name, familyname):
    print("{0}{1}".format(name, familyname))


def printName(isChinese, name, familyname):
    def inner_print(a, b):
        print("{0}{1}".format(a,b))
    if isChinese:
        inner_print(familyname, name)
    else:
        inner_print(name, familyname)


printName(True, "航伟", "左")

outer()