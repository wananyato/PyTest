#!coding:utf-8
"""输入员工的薪资，如输入薪资小于0则重新输入，最后输出员工数量，薪资列表，薪资总额，平均薪资"""
em_num = 0
sala_sum = 0
sala_mumbers = []
while True:
    salary = input("请输入员工薪资(按q或Q结束)")
    if salary.upper() == "Q":
        print("输入完毕，退出程序！")
        break
    if int(salary) < 0:
        continue
    sala_mumbers.append(salary)
    sala_sum += int(salary)
    em_num += 1

print("员工数{0}:".format(em_num))
print("薪资列表{0}:".format(sala_mumbers))
print("薪资总和{0}:".format(sala_sum))
print("平均薪资:{0}".format(float(sala_sum/em_num)))