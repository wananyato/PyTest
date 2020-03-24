# coding:utf-8
# Traceback追溯，most recent call last  最后一次调用。
#a = 3/0


def a():
    num = 1/0


def b():
    a()


def c():
    b()


c()