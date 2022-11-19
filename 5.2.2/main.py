def f(x):
    n = 0
    suma = 0
    while (abs(((-2)**n)*(x**(2*n))) >= 0.0001):
        suma += ((-2)**n)*(x**(2*n))
        n += 1
    return suma
x = float(input("Введіть Х:"))
if (abs(x)<(1/(2**0.5))):
    print(f(x))
else:
    print("Неправильне введення Х")
