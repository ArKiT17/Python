print("===== Завдання 1 =====")
print(
    """
    - Hi! What are you doing?
    - Hi, I`m working about python`s homework
    - Oh, what result do you want to have?
    - Um... Hope at least 100.. 😅 
    """
)

print("===== Завдання 2 =====")
print("the early bird gets the worm"[4:-3])

print("===== Завдання 3 =====")
a = input("Введіть рядок: ")
b = input("Введіть підрядок: ")
print("Перше входження починається з індекса {}, а останнє - {}".format(a.find(b), a.rfind(b)))

print("===== Завдання 4 =====")
a = input("Введіть рядок: ")
b = input("Введіть підрядок: ")
print("Індекси всіх входжень підрядка: ", end='')
k = -1
while True:
    k = a.find(b, k + 1)
    if k != -1:
        print(k, end=" ")
    else:
        break

print("\n===== Завдання 5 =====")
a = input("Введіть рядок: ")
b = input("Введіть підрядок: ")
print("Вся частина:", a.count(b))
print("Від {} до {}:".format(input("Введіть початок пошуку: "), input("Введіть кінець пошуку: ")), a.count(b))

print("===== Завдання 6 =====")
a = input("Введіть рядок: ")
b = list(a)
c = ''.join(reversed(b))
print((c.replace('.', '!')).replace('№', ''))

#print((''.join(reversed(list(input("Введіть рядок: ")))).replace('.', '!')).replace('№', ''))