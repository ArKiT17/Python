#4.2. Вивести цілі числа з проміжку [a,b] в зворотному порядку та знайти їх суму.
a=int(input("Enter a: "))
b=int(input("Enter b: "))
s=0
for i in range(b, a-1, -1):
    print(i, end=", ")
    s += i;
print("\nSum = {}".format(s))
