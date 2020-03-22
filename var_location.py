# 测试局部变量和全局变量应用时的效率,局部变量引用的效率大于全局变量引用的效率
import time
import math


def test01():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时：{0}".format((end-start)))


def test02():
    b = math.sqrt
    start = time.time()
    for i in range(10000000):
        b(30)
    end = time.time()
    print("耗时：{0}".format((end-start)))


test01()
test02()
