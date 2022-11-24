# Найти наименьшее количество точек, покрывающих все отрезки
numbers = int(input())
otrezki = []
for i in range(numbers):
    otrezki.append([int(x) for x in input().split()])
#Сортировка отрезков по правой точке

for i in range(1,numbers):
    key = otrezki[i]
    j = i - 1
    while j >= 0 and otrezki[j][1] > key[1]:
        otrezki[j + 1] = otrezki[j]
        j -= 1
    otrezki[j + 1] = key

counter = 0
indexes = []
coordinats = []
i = 0
while otrezki:
    i += 1
    if i < len(otrezki) and otrezki[0][1] >= otrezki[i][0]:
        indexes.append(i)
    else:
        coordinats.append(otrezki[0][1])
        counter += 1
        for f in indexes:
            otrezki.pop(indexes[len(indexes) - f] - 1)
        if otrezki:
            otrezki.pop(0)
        i = 0
        indexes.clear()

print(counter)
for t in coordinats:
    print(t,end = " ")
