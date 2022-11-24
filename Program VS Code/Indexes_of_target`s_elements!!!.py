def Binary_search(array,target):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = int((left + right) / 2)
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return None

def Find_target_indexes(array,target):
    index = Binary_search(array,target)

    arr_indexes = []
    arr_indexes.append(index)

    if index == 0:
        while array[index] == array[index + 1]:
            arr_indexes.append(index + 1)
            index += 1
    elif index == len(array) + 1:
         while array[index] == array[index - 1]:
            arr_indexes.append(index + 1)
            index -= 1
    else:
        if array[index] == array[index - 1]:
            while array[index] == array[index - 1]:
                arr_indexes.append(index + 1)
                index -= 1
        if array[index] == array[index + 1]:
            while array[index] == array[index + 1]:
                arr_indexes.append(index + 1)
                index += 1
    return arr_indexes

def main():
    array = [int(x) for x in input().split()]
    target = int(input())
    answer = Find_target_indexes(array,target)
    for i in answer:
        print(i,end = " ")

main()