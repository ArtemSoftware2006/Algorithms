alfavit_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alfavit_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letters_RU = 33
letters_EN = 25

lang = int(input("Введите язык ( 1 -- РУССКИЙ / 2 -- ENGLISH ): "))
smeshenie = int(input("Введите смещение: "))
message = input("Введите сообщение для ДЕШИФРОВАНИЯ: ").upper()

de_itog=""

if lang == 1:
    for i in message:
        mesto = alfavit_RU.find(i)

        if mesto < smeshenie:
            new_mesto = letters_RU + mesto - smeshenie
        else:
            new_mesto = mesto - smeshenie

        if i in alfavit_RU:
            de_itog += alfavit_RU[new_mesto]
        else:
            de_itog += i
else:
    for i in message:
        mesto = alfavit_EN.find(i)
        if mesto < smeshenie:
            new_mesto = letters_EN + mesto - smeshenie
        else:
            new_mesto = mesto - smeshenie

        if i in alfavit_EN:
            de_itog += alfavit_EN[new_mesto]
        else:
            de_itog += i
print("Дешифр:" + de_itog)
