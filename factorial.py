# 阶乘
def factorial_test(n):
    if n == 1:
        return 1
    else:
        return n*factorial_test(n-1)


n = int(input('please input a number:'))
result = factorial_test(n)
print(result)