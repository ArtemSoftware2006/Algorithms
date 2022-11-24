# Найдите простые числа в интервале натуральных чисел
import time
start = time.time()

min_numb, max_numb = map(int,input().split())

primes = [1] * (max_numb + 1)

for i in range(2, max_numb + 1):
    if primes[i]:
        for j in range(i * i, max_numb + 1, i):
            primes[j] = 0
for i in range(1, max_numb + 1):
    if min_numb < i and primes[i] == 1:
        print(i)

end = time.time()

print("Время: ", (end - start))
