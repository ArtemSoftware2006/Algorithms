#Ката на различный ввод и вывод в Python


def main():
    
    #Различные вводы чисел
    i = int(input())
    
    #Различные вводы массива
    #Не работает
    #array = map(int,input().split())
    arr_1 = [int(x) for x in input().split()]

    #Различный вывод массива
    for i in arr_1:
        print(i,end = " ")
