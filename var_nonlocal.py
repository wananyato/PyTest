#测试nonlocal、global关键字的用法
a = 100

def outer():
    b = 10

    def inner():
        nonlocal b
        print("inner b:", b)
        b = 20
        global a
        print(a)
        a = 1000
    inner()
    print("outer b:", b)


outer()
print(a)