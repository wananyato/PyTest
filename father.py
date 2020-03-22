# 测试继承的基本使用

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # 私有属性

    def say_age(self):
        print(self.name, "的年龄是", self.age)


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score


# student-Person-object类
print(Student.mro())

a = Student("左航伟", 18, 80)
# a.say_age()
# print(a.name)
# print(a.age)
print(a._Person__age)
print(dir(a))