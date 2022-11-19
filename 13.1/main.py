def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while (i > -1) and key < A[i]:
            A[i+1] = A[i]
            i -= 1
            A[i+1] = key
    return A

x = [5,2,4,6,1,3]
insertion_sort(x)
print(x)

def selection_sort(A):
    for i in range(len(A)):
        min_position = i
        for j in range(i+1, len(A)):
            if A[min_position] > A[j]:
                min_position = j
        A[i], A[min_position] = A[min_position], A[i]
    return A
x=[5,2,1,9,0,4,6]
selection_sort(x)
print(x)

def bubble_sort(A):
    for i in range(len(A)-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A
x=[5,1,2,3,9,8,0]
bubble_sort(x)
print(x)



def selection_sort(A):
    for i in range(len(A)):
        min_position = i
        for j in range(i+1, len(A)):
            if A[min_position] > A[j]:
                min_position = j
        A[i], A[min_position] = A[min_position], A[i]
    return A

def binary_search(A, item):
    first = 0
    last = len(A) - 1
    found = False
    while first <= last and not found:
        pos = 0
        mid_point = (first + last)//2
        if A[mid_point] == item:
            pos = mid_point
            found = True
        else:
            if item < A[mid_point]:
                last = mid_point-1
            else:
                first = mid_point+1
    if not found:
        pos = -1
    return found, pos
x=[5,2,1,9,0,4,6]
selection_sort(x)
print(x)
key = int(input('Enter your key for seach ->'))
result, index = binary_search(x, key)
print(result, index)