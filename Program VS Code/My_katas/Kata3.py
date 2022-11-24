import random

def QS(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = random.choice(arr)
        less_numb = []
        more_numb = []
        piv_numb = []
        for n in arr:
            if n > pivot:
                more_numb.append(n)
            elif n < pivot:
                less_numb.append(n)
            else:
                piv_numb.append(n)
        return QS(less_numb) + piv_numb + QS(more_numb)

print(QS([10, 0 ,23, -3, -34, 78,1, 56,3 ,0.33]))

def insert_sort(arr):
    for i in range(1,len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j  + 1] = key
    return arr
print(insert_sort([10, 0 ,23, -3, -34, 78,1, 56,3 ,0,33]))


def Insertion_sort(array):
    for i in range(1,len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def Ins_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j] = key
    return arr

print(Ins_sort([10, 2, 0, 45, -6, -9, 100]))

def B_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = int((left + right) / 2)
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1
print(B_search([10, 11, 13, 20, 19, 100, 140], 100))



















