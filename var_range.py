# 全局变量的作用域测试
a = 100


def var_range():
    a = 10
    print(a)
    a = 200

    b = 4
    print(b*a)

    print(locals())
    print(globals())

var_range()
print(a)
