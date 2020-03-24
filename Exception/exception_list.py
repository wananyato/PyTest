# 列举常见异常

# SyntaxError 语法错误


# Name Error: 尝试访问一个没有申明的变量
print(a)

# ZeroDivisionError:division by zero
b = 3/0

# Value Error:数值错误
float("wananyato")

# Type Error: 类型错误
123+"abc"

# AttributeError:访问对象的不存在的属性
c = 100
c.sayhi()

# IndexError:索引越界异常
d = [4, 5, 6]
d[10]

# Key Error:字典的关键字不存在
e = {"name": "phil", "age": 18}
e['salary']


