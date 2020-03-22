# 测试参数的类型，位置参数、默认值参数、命名参数
def test_location(a, b, c, d):
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


def test_default(a, b, c=30, d=40):     # c,d为默认参数，必须位于其他参数后面
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


def test_canchange(a, b, *c):       # 可变参数*C，*c会生成一个元组
    print(a, b, c)


def test_canchange(a, b, **c):      # 可变参数*c，**c会生成一个字典
    print(a, b, c)
    

test_location(10, 20, 30, 40)           # 位置参数
test_location(d=40, c=30, a=10, b=20)   # 命名参数
test_default(10, 20)                    # 默认值参数
test_default(10, 20, 50, 60)            # 默认值参数的修改
