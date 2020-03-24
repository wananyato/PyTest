# coding = utf-8
# 示例：循环输入数字，如果输入不是数字则处理异常，直到输入88，则结束循环

while True:
    try:
        x = int(input("please input number:"))
        print("The number is:", x)
        if x == 88:
            print("end the program!")
            break
    except BaseException as e:
        print(e)
        print("Input Error! Please Input a number!")
print("exiting...")