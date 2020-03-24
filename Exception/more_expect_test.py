# coding = utf-8
"""
测试try：
    except exception1：
    except exception2:
"""
while True:
    try:
        a = input("please input a number:")
        b = input("please input a number:")
        c = float(a)/float(b)
        print(c)
    except ZeroDivisionError:
        print("异常，0不能做除数！")
    except ValueError:
        print("异常，不能将字符串转化为数字")
    except NameError:
        print("异常，变量不存在")
    except BaseException as e:
        print("异常，其他异常")
        print(e)