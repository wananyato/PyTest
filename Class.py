class Student:        # 类名一般首字母大写，采用驼峰式命名

    def __init__(self, name, score):    # self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是：{1}".format(self.name,self.score))


s1 = Student("左航伟", 18)
s1.say_score()

s1.age = 32
s1.salary  = 3000
print(s1.age)

s2 = Student("王宇", 100)
print(s2.name)
Student.say_score(s2)

print(dir(s1))
print(s2.__dict__)
print(isinstance(s2, Student))