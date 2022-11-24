number = int(input())
numbers = []
#Записвыаем в массив цифры из числа
for i in range(6):
    numbers.append(number%10)
    number = int(number/10)
#Билет счастливый?
if numbers[0] + numbers[1] + numbers[2] == numbers[3]+ numbers[4] + numbers[5]:
    print("YES")
else:
    print("NO")