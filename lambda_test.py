
f = lambda a, b, c, d: a+b+c+d
print(f)
print(f(1, 2, 3, 4))

g = [lambda a:a*2, lambda b:b*3]
print(g[0](6))
print(g[1](7))