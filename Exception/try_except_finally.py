# coding = utf-8
# 测试finally语句
try:
    a = input("Please input a number:")
    b = input("Please input a number:")
    c = float(a)/float(b)
except BaseException as e:
    print(e)
else:
    print("{0}除以{1}的结果是{2}".format(a, b, c))
    print("运算成功")
finally:
    print("无论程序是否执行成功，结束程序")