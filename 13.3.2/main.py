def sort(stat):
    for i in range(len(stat)):
        for j in range(len(stat) - 1, i, -1):
            if (stat[j] > stat[j-1]):
                stat[j], stat[j-1] = stat[j-1], stat[j]
    return stat

stations = ["Кропивницький - Київ", "Київ - Харків", "Дніпро - Одеса", "Жмеринка - Знам'янка", "Хмельницький - Луцьк",
            "Львів - Вінниця", "Дніпро - Тернопіль", "Луцьк - Суми", "Луцьк - Чернівці", "Івано-Франківськ - Кропивницький"]
for i in range(len(stations)):
    print(stations[i])
stations = sort(stations)
print()
for i in range(len(stations)):
    print(stations[i])

count = 0
word = input("Введіть станцію: ")
for i in range(len(stations)):
    x = stations[i].split()
    if (x[0] == word):
        count += 1
print("Кількість відправлень зі станції {} - {}".format(word, count))