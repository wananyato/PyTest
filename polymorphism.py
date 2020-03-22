# 测试多态


class Man:

    def eat(self):
        print("饿了，吃饭了")


class Chinese(Man):

    def eat(self):
        print("中国人用筷子吃饭")


class English(Man):

    def eat(self):
        print("英国人用刀叉吃饭")


class Indian(Man):

    def eat(self):
        print("印度人用右手吃饭")


def maneat(m):
    if isinstance(m, Man):
        m.eat()             # 多态，一个方法调用，根据传入的对象类型不同调用不同的方法。
    else:
        print("不能吃饭")


maneat(Chinese())
maneat(Indian())
maneat(English())
