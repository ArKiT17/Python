#3.2 Вибрати задачу відповідно до номера прізвища у журналі.
#Розробити програму, що виводить на екран таблицю значень функції на
#проміжку [1..10] з кроком 1, використовуючи цикл for та цикл із
#передумовою. Порівняти створені програми.

print("  X        Y")
for i in range(1, 11):
    print(" {}       {:.3f}". format(i, 1/(1+i**2)**0.5))