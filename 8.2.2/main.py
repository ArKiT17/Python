import random
n = int(input("Введіть розмір матриці N: "))
mat = [[random.randint(0, 10) for i in range(n)] for j in range(n)]
print("Матриця: ")
for i in range(n):
    for j in range(n):
        print(mat[i][j], end='\t')
    print()

min_ = 99999
r = 0
fill = [['-' for i in range(n)] for j in range(n)]
for i in range(int(n/2), n):
    for j in range(int(n/2)-r, int(n/2+1)+r):
        if(mat[i][j] < min_):
            min_ = mat[i][j]
        fill[i][j] = '#'
    r+=1
print("Шукана область: ")
for i in range(n):
    for j in range(n):
        print(fill[i][j], end = '\t')
    print()
print("Мінімальний елемент в цій області: ", min_)