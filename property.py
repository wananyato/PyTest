# @property装饰器的用法


class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 2000 < salary < 50000:
            self.__salary = salary
        else:
            print("输入有误，请重新输入（2000-50000）：")
"""
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 2000< salary <50000:
            self.__salary = salary
        else:
            print("输入有误，请重新输入（2000-50000）：")
"""

emp = Employee("左航伟", "20000")
print(emp.salary)
emp.salary = 3000
print(emp.salary)
# print(emp.get_salary())
# emp.set_salary(3000)
# print(emp.get_salary())