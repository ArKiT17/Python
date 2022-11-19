import random
n = int(input("Введіть розмір матриці N: "))
mat = [[random.randint(0, 10) for i in range(n)] for j in range(n)]
print("Матриця: ")
for i in range(n):
    for j in range(n):
        print(mat[i][j], end='\t')
    print()
x = int(input("Введіть шукане число: "))
sum_ = 0
for i in range(n):
    for j in range(n):
        if(mat[i][j] == x):
            sum_ += 1
            print("Число {} знайдено на позиції {} {}".format(x, i+1, j+1))
print("Кількість входжень числа {}: {}".format(x, sum_))