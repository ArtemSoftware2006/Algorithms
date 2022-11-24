
#Доделать вывод
def Binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = int((left + right) / 2)
        if array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
        else:
            return target
    return None

def sravnenie_arraies(min_arr, max_arr):
    answer = []
    for n in min_arr:
        a = Binary_search(max_arr,n)
        if a != None:
            answer.append(a)
    return answer
    

def main():
    arr_1 = [int(x) for x in input().split()]
    arr_2 = [int(x) for x in input().split()]

    if len(arr_2) > len(arr_1):
        for i in sravnenie_arraies(arr_1, arr_2):
            print(i,end = " ")
    else:
        for i in sravnenie_arraies(arr_2, arr_1):
            print(i,end = " ")
main()
