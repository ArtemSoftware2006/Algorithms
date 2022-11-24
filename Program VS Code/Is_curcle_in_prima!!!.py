#Поместится ли круг в прямоугольник
Weigh,Hight, Radius=map(int,input().split())

if Radius*2 <= Weigh and Hight >= Radius*2:
    print("YES")
else:
    print("NO")