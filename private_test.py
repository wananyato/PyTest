# 测试私有属性

class Employee:

    __company = "wananyato"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __work(self):
        print("好好工作，努力赚钱")
        print("年龄：{0}".format(self.__age))
        print(Employee.__company)

e = Employee("左航伟", 18)
print(e.name)
# print(e.age)
print(e._Employee__age)
print(dir(e))
e._Employee__work()
e._Employee__company