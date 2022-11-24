# Найти все делителм числа
import time

start = time.time()

def GetAllDivisors(number):
    divisors = [1]
    for i in range(2,int(number / 2) + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors
number = int(input())
print(GetAllDivisors(number))

end = time.time()

print("Время: ", (end - start))