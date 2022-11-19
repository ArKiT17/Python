
#завдання 6
print("--- Створення списку ---")
list1 = ["яблуня", "ялинка", "ромашка", "ялинка", "дуб", "дуб", "тюльпан", "дуб"]
print("Список: {}".format(list1))

#завдання 7
print("\n\n--- Додавання 3 елементів методом append() ---")
list1.append("пальма")
list1.append("баобаб")
list1.append("кипарис")
print("Список: {}\nДовжина - {}".format(list1, len(list1)))

#завдання 8
print("\n\n--- Вставка одного елемента методом insert() ---")
tmp_i = int(input("Введіть місце вставки нового елемента: "))
tmp_s = input("Введіть новий елемент: ")
list1.insert(tmp_i - 1, tmp_s)
print("Список: {}\nДовжина - {}".format(list1, len(list1)))

#завдання 9
print("\n\n--- Створення нового списка та його допис до загального ---")
list2 = ["календула", "тополя", "каштан"]
list1.extend(list2)
print("Список: {}\nДовжина - {}".format(list1, len(list1)))
print("Максимальний елемент: {}\nМінімальний елемент {}".format(max(list1), min(list1)))

#завдання 10
print("\n\n--- Пошук елемента count() index() ---")
tmp = input("Введіть значення: ")
if tmp in list1:
    print("Перший елемент знайдено під індексом {}, їх кількість - {}".format(list1.index(tmp), list1.count(tmp)))
else:
    print("Елемент не знайдено")

#завдання 11
print("\n\n--- sort() reverse() ---")
list1.sort()
print("Відсортований список за зростанням: {}".format(list1))
list1.reverse()
print("Відсортований список за спаданням: {}".format(list1))

#завдання 12
print("\n\n--- remove() ---")
tmp = input("Введіть значення: ")
if tmp in list1:
    list1.remove(tmp)
    print("Список: {}\nДовжина - {}".format(list1, len(list1)))
else:
    print("Такого значення у списку немає")

#завдання 13
print("\n\n--- del() ---")
del list1[:2]
print("Список: {}\nДовжина - {}".format(list1, len(list1)))
del list1[-2:]
print("Список: {}\nДовжина - {}".format(list1, len(list1)))
del list1[0::2]
print("Список: {}\nДовжина - {}".format(list1, len(list1)))

#завдання 14
print("\n\n--- Новий список виведений for ---")
list1 = ["яблуня", "ялинка", "ромашка", "ялинка", "дуб", "дуб", "тюльпан", "дуб"]
for i in range(len(list1)):
    print(list1[i], end=", ")

#завдання 15
print("\n\n--- Видалення усіх дублів ---")
#list1.sort()
for i in list1:
    if list1.count(i) > 1:
        for j in range(list1.count(i) - 1):
            list1.remove(i)
print(tuple(list1))
