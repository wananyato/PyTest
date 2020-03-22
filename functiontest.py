# 测试返回值的基本用法
def add(a, b):
    print("计算两个数的和：{0}，{1}，{2}".format(a, b, (a+b)))
    return a+b

def test():
    print("axt")
    print("gao")
    return          #return两个作用：1、返回值 2、结束函数的执行
    print("hello")

def test01(x, y, z):
    return [x*10, y*10, z*10]


c = add(30, 40)
print(add(30, 40)*10)
d = test()
print(d)
e = test01(3, 4, 5)
print(e)
