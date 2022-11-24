# Вывести сумму всех делителей числа
def GetAllDivisors(number):
    divisors = [1]
    for i in range(2,int(number / 2) + 1):
        if number % i == 0:
            divisors.append(i)
    divisors.append(number)
    return divisors

number = int(input())

array = GetAllDivisors(number)
sum = array[0]
for i in range(1,len(array)):
    sum += array[i]

print(sum)
