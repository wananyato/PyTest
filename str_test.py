# 测试重写object的__str__();
class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "名字是：{0}".format(self.name)


p = Person("左航伟")
print(p)