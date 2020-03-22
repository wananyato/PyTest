# _测试可调用方法__call___()

class SalaryAccount:
    """工资计算类"""

    def __call__(self, salary):
        print("算工资啦")
        yearsalary = salary*12
        daysalary = salary//22.5
        hoursalary = daysalary//8

        return dict(yearsalary=yearsalary, daysalary=daysalary, hoursalary=hoursalary)


s = SalaryAccount()
print(s(30000))
