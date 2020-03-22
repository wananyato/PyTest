# 测试LEGB，遵循local-->Enclosed-->Global-->Build in的顺序

print(type(str))                # BuildIN：指的是Python为自己保留的特殊名称
# str = "global"                 # Global：指的是模块中的全局变量


def outer():

    # str= "outer"       # Enclosed：值得是嵌套函数（一个函数内部包含的另一个函数，闭包）
    def inner():
        # str = "inner"          # Local：函数或者类的方法内部
        print(str)

    inner()


outer()

