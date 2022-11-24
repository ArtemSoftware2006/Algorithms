#Быки и Коровы

print("Игра Быуи и Коровы начинается!")
print("Я загадал 4-x  значное число...")
secret_number = 1234
number = int(input("Введите ваше число "))

def CifresInNumb(numb):
    numbs = []
    for i in range(4):
        numbs.append(numb%10)
        numb = int(numb/10)
    return numbs

inputCifrs = CifresInNumb(number)
secretCifries = CifresInNumb(secret_number)
output = []
while inputCifrs != secretCifries:
    for i in range(len(secretCifries)):
        if secretCifries[i] == inputCifrs[i]:
            output.append("Б")
        else:
            for j in range(len(secretCifries)):
                if inputCifrs[i] == secretCifries[j]:
                    output.append("К")
                    break
                if j == len(secretCifries) - 1:
                    output.append(inputCifrs[i])

    for i in range(1,len(output) + 1,1):
        print(output[len(output) - i])

    if(inputCifrs == secretCifries):
        break
    else:
        output = []
        print("Попробуйте угадать снова!")
        number = int(input("Введите число: "))
        inputCifrs = CifresInNumb(number)
            
print("Вы угадали число!")

