#Разбить число на наименьшие неповторяющиеся слагаемые
number = int(input())

simple_numb = []

i = 0
sum_i = 0

while sum_i < number:
    i += 1
    sum_i += i
    simple_numb.append(i)

if sum_i == number:
    print(len(simple_numb))
    for num in simple_numb:
        print (num, end=" ")
else:
    sum_i -= simple_numb[len(simple_numb) - 1]
    sum_i -= simple_numb[len(simple_numb) - 2]

    simple_numb.pop(len(simple_numb) - 1)
    i = simple_numb[len(simple_numb) - 1]
    simple_numb.pop(len(simple_numb) - 1)

    while i <= number:
        if sum_i + i == number:
            simple_numb.append(i)
            break
        i += 1
    print(len(simple_numb))
    for num in simple_numb:
        print (num, end=" ")
