print("===== Завдання 2 =====")
autos = {"audi": "ВА 9999 АК", "toyota": "ВХ 1234 ТВ", "tesla": "AB 4455 IK",
         "mini": "AI 8644 AO", "mercedes": "BA 3782 PA", "volvo": "KA 9665 AM",
         "lexus": "AA 0000 AA", "porsche": "AA 7777 BB", "renault": "AH 3637 AA",
         "mitsubishi": "AP 8448 OM"}
print("Словник: {}\nLength: {}".format(autos, len(autos)))
print("Номер машини: ", autos.get(input("Введіть шукану марку: ").lower()))

print("===== Завдання 3 =====")
print(input("Введіть номер авто: ").upper() in autos.values())

print("===== Завдання 4 =====")
autoKeys = autos.keys()
autoValues = autos.values()
print(sorted(autos))

print("===== Завдання 5 =====")
for i in autos.items():
    print(i[0].capitalize(), end=", ")

print("===== Завдання 6 =====")
del(autos[input("Введіть марку для видалення: ").lower()])
print("{}, \nРозмір: {}".format(autos, len(autos)))

print("===== Завдання 7 =====")
newAutos = {"ford": "KA 9990 KM", "chevrolet": "AE 1123 AM", "subaru": "AA 8888 AA"}
autos.update(newAutos)
print("{}\nДовжина: {}".format(autos,len(autos)))

print("===== Завдання 8 =====")
list = ("ford", "audi", "smart", "honda")
import random
print(dict.fromkeys(list, random.randint(0, 10)))