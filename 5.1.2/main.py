def f(x, y):
    return ((x**2+x*y-y**2)/(1+x+y))+((x-y)/(x**2+y**2+2))
a=float(input("Введіть А: "))
b=float(input("Введіть B: "))
print("u = {:0.4f}".format(f(0.5, a)+f(a+b, a-b)))
