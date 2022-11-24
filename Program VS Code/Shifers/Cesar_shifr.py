#Шифр Цезаря

alfavit_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alfavit_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letters_RU = 32
letters_EN = 25

lang = int(input("Введите язык ( 1 -- РУССКИЙ / 2 -- ENGLISH ): "))
smeshenie = int(input("Введите смещение: "))
message = input("Введите сообщение: ").upper()

itog=""

if lang == 1:
    for i in message:
        mesto = alfavit_RU.find(i)
        if mesto + smeshenie >= letters_RU:
            new_mesto = mesto + smeshenie - letters_RU - 1
        else:
            new_mesto = mesto + smeshenie

        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i
else:
    for i in message:

        mesto = alfavit_EN.find(i)

        if mesto + smeshenie >=letters_EN:
            new_mesto = mesto + smeshenie - letters_EN - 1
        else:      
            new_mesto = mesto + smeshenie

        if i in alfavit_EN:
            itog += alfavit_EN[new_mesto]
        else:
            itog += i


print("ШИФР: "+ itog)

de_itog = ""

if lang == 1:
    for i in itog:
        mesto = alfavit_RU.find(i)

        if mesto < smeshenie:
            new_mesto = letters_RU + mesto - smeshenie + 1
        else:
            new_mesto = mesto - smeshenie

        if i in alfavit_RU:
            de_itog += alfavit_RU[new_mesto]
        else:
            de_itog += i
else:
    for i in itog:
        mesto = alfavit_EN.find(i)
        if mesto < smeshenie:
            new_mesto = letters_EN + mesto - smeshenie + 1
        else:
            new_mesto = mesto - smeshenie

        if i in alfavit_EN:
            de_itog += alfavit_EN[new_mesto]
        else:
            de_itog += i
print("Дешифр:" + de_itog)

print(message == de_itog)


