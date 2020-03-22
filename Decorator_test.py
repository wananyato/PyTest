# 测试@property最简单的使用
class Employee:

    @property
    def salary(self):
        print("salary run...")
        return 10000


emp = Employee()
# emp.salary
print(emp.salary)