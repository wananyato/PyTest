# 测试类方法：

class Student:
    company = "wananyato"   # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod        # 类方法
    def printCompany(cls):
        print(cls.company)

    @staticmethod        # 静态方法
    def add(a, b):
        print("{0}+{1}={2}".format(a, b, a+b))
        return a+b


Student.printCompany()
Student.add(8, 9)