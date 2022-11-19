# Завдання 2. За допомогою функції range() вивести на екран такі
# послідовності чисел:
# a) 0, 1, 2, 3, 4,
# b) 5, 6, 7, 8, 9,
# c) 1, 3, 5, 7, 9,
# d) -2, -1, 0, 1, 2, 3, 4,
# e) 100, 80, 60, 40, 20,
for i in range(5):
    print(i, end=", ")

print("\n===========")

for i in range(5, 10):
    print(i, end=", ")

print("\n===========")

for i in range(1, 10, 2):
    print(i, end=", ")

print("\n===========")

for i in range(-2, 5):
    print(i, end=", ")

print("\n===========")

for i in range(100, 0, -20):
    print(i, end=", ")
