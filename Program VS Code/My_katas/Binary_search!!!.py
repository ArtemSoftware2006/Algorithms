#Реализация бинарного поиска

def Binary_search(array,target):
    left, right = 0, len(array)  - 1
    while left <= right:
        middle = int((left + right) / 2)
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
print(Binary_search([-2,0,2,3,4,7,12,45,222,459,1000],10))