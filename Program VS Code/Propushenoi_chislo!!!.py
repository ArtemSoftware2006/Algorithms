def main():
    array = [1, 0, 4, 3,5,6,9,2]
    Propushenoi_chislo(array)

def Propushenoi_chislo(array):
    new_arr = []
    for n in range(len(array) + 1):
        new_arr.append(n)

    for i in range(len(array)):
        new_arr.pop( Bin_search(new_arr, array[i]))
    print(new_arr[len(new_arr) - 1])
            
    
def Bin_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = int((left + right)/2) 
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return False

main()