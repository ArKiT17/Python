# Номер по списку - 2
# Завдання 1
import random
def fun(lenght, from_, to_):
    list = []
    for index in range(lenght):
        list.append(random.randint(from_, to_))
    return list

# Завдання 2
list_lenght = int(input("Enter leght of list: "))
list_main = fun(list_lenght, -10, 10)
#list_main = [-1, -2, -3, 0, 5, -10, 9, 4, 0, -3] # Якщо не використовувати список із завдання 1
print("Main List: ", list_main)

list2 = []
list3 = []
for index in range(list_lenght):
    if list_main[index] >= 0:
        list2.append(list_main[index])
    else:
        list3.append(list_main[index])
print("List + : {}\nList - : {}".format(list2, list3))

# Завдання 3
suma = 0
for index in range(list_lenght-1):
    if (abs(list_main[index] + list_main[index + 1]) < max(list_main[index], list_main[index + 1])):
        suma += 1
print("Count of neighbours with different signs is ", suma)