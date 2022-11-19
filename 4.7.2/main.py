var=float(input("Введіть задану точність:"))
suma=0
n=1
while (1/((3**n)+3*n)) >= var:
    suma = suma + (1/(3**n)+3*n)
    n = n + 1
print("Задана точність: {}, сума компонентів: {}".format(var, suma))
