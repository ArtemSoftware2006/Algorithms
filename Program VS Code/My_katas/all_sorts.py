# QuickSort

random_array = [39, 33, -213, 0, 435,0, 66, -34]
import random

def QS(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        less_numb = []
        more_numb = []
        e_numb = []
        for n in array:
            if n < pivot:
                less_numb.append(n)
            elif n > pivot:
                more_numb.append(n)
            else:
                e_numb.append(n)
        return QS(less_numb) + e_numb + QS(more_numb)

print("Quick_Sort")
print(QS([10, 10, 0, -1, 2,3, -66]))

# Bubble Sort

def Bubble_Sort(array):
    swap = True
    while swap:
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[ i + 1] = array[i + 1], array[i]
                swap = True
    return array

print("Bubble_Sort")
print(Bubble_Sort([10, 11, 90, 222, -21,0, 0]))

# Сортировка Выборкой

def Selection_Sort(array):
    for i in range(len(array)):
        lowest_value_index = i
        for j in range(i +1, len(array)):
            if array[lowest_value_index] > array[j]:
                lowest_value_index = j
        array[lowest_value_index], array[i] = array[i], array[lowest_value_index]
    return array

print("Selection_Sort")
print(Bubble_Sort([10, 11, 0, 45, -12, -2333, 0, 11]))

#Сортировка Вставкой

def Insertion_Sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0  and array[j] > key:
            array[j + 1] = array[j]
            j-=1
        array[j + 1] = key
    return array

print("Insertion_Sort")
print(Insertion_Sort([1, 45, 2, 45, 34, 12, -2, -56, 0, 34, -47]))