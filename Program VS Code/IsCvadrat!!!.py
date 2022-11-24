# Проверить: является ли число абсолютным квадратом
def is_squer(number):
    if number == 0:
        return True
    for i in range(number):
        if i*i == number:
            return True
        if i+1 > number/2:
            return False
    return False
print(is_squer(100))