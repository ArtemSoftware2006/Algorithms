def main():
    arr_1 = [int(x) for x in input().split()]
    arr_2 = [int(x) for x in input().split()]
    print(Find_pairs(arr_1,arr_2))


def Find_pairs(arr_1,arr_2):
    i = 0
    max_distance = 0
    if len(arr_1) > len(arr_2):
        while i < len(arr_2):
            j = i
            while j < len(arr_1) and i <= j and arr_1[i] <= arr_2[j]:
                if max_distance < j - i:
                    max_distance = j - i
                j+=1
            i += 1
    else:
        while i < len(arr_1):
            j = i
            while j < len(arr_2) and i <= j and arr_1[i] <= arr_2[j]:
                if max_distance < j - i:
                    max_distance = j - i
                j+=1
            i += 1
    return max_distance

main()