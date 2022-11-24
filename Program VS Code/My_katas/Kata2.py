import random

def QS(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        less_numb = []
        more_numb = []
        piv_numb = []
        for n in array:
            if n < pivot:
                less_numb.append(n)
            elif n > pivot:
                more_numb.append(n)
            else:
                piv_numb.append(n)
        return QS(less_numb) + piv_numb + QS(more_numb)

print(QS([1, 3, 5, 6, 12, 56, 3, 0,-4, -2, -77, -12, 0, 9 ,3, 5]))


def Insertion_Sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0  and array[j] > key:
            array[j + 1] = array[j]
            j-=1
        array[j + 1] = key
    return array

def Insert_search(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

print(Insert_search([1, 3, 5, 6, 12, 56, 3, 0,-4, -2, -77, -12, 0, 9 ,3, 5]))











