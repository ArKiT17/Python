#завдання 1
print("--- Створення кортежу ---")
cort1 = ("мм", "мм", "ярд", "см", "ярд", "м", "дм", "км", "ярд", "миля", "дюйм", "фут")
print("Кортеж: {}".format(cort1))
print("Довжина кортежа: {}".format(len(cort1)))

#завдання 2
print("\n\n--- Виведення на єкран k-го елемента ---")
k = int(input("Введіть номер елемента, який хочете вивести: "))
print("{}й елемент кортежа - {}".format(k, cort1[k - 1]))

#завдання 3
print("\n\n--- Додавання іншого кортежу ---")
cort2 = ("один", "два", "три")
cort1 += cort2
print("Кортеж: {}\nМаксимальний елемент - {}\nМінімальний елемент - {}".format(cort1, max(cort1), min(cort1)))

#завдання 4
print("\n\n--- Пошук елемента ---")
tmp = input("Введіть значення: ")
if tmp in cort1:
    print("Значення знайдено. Індекс його першого входження - {}, загальна їх кількість - {}".format(cort1.index(tmp), cort1.count(tmp)))
else:
    print("Заданого значення в кортежі немає")

#завдання 5
print("\n\n--- Перетворення на список ---")
list1 = list(cort1)
print("Cписок: {}".format(list1))
