# 测试函数也是对象
def test(a, b):
    print("两个数字：{0},{1}".format(a, b))


test(1, 2)
c = test
c(1, 2)