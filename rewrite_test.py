# 测试方法的重写
# 测试继承的基本使用

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # 私有属性

    def say_age(self):
        print(self.name, "的年龄是", self.__age)

    def say_introduce(self):
        print("我的名字是{0}".format(self.name))


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    def say_introduce(self):
        """重写了父类的方法"""
        print("报告老师，我的名字是：{0}".format(self.name))

# student-Person-object类
print(Student.mro())

a = Student("左航伟", 18, 80)
a.say_age()
a.say_introduce()
# a.say_age()
# print(a.name)
# print(a.age)
print(a._Person__age)
print(dir(a))