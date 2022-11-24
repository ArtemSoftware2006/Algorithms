# Вывести число задом на перед
def main(number):
    if number ==  0:
        print(0)
        return 0
    cifrs = []
    while number > 0:
        cifrs.append(number % 10)
        number = int(number / 10)

    for i in range(1,len(cifrs)):
        key = cifrs[i]
        j = i - 1
        while j >= 0  and cifrs[j] > key:
            cifrs[j + 1] = cifrs[j]
            j-=1
        cifrs[j + 1] = key

    ans = ""    
    for i in range(len(cifrs) - 1,-1,-1):
        ans = ans + str(cifrs[i])

    print(int(ans))

main(234)