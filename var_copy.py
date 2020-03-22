# 传递不可变对象是，如果发生copy，则使用的是浅拷贝

a = 10
print("a:", id(a))


def test01(m):
    print("m:", id(m))
    m = 20
    print(m)
    print("m:", id(m))


test01(a)