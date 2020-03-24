try:
    a = input("please input a number:")
    b = input("please input a number:")
    c = float(a)/float(b)
except BaseException as e:
    print(e)
else:
    print("{0}除{1}的结果是：{2}".format(a, b, c))
    print("程序结束！")