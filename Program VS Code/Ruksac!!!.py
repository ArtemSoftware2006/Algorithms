#НАйти максимальную сумму, на которую вор может обокрасть магазин
answer = 0

numbers_things, Limit = map(int,input().split())

price_things = [0] * numbers_things
weight_thing = [0] * numbers_things

price_of_gram_and_weight_things = []

for i in range(numbers_things):
    price_things[i],weight_thing[i] = map(int,input().split())
    price_of_gram_and_weight_things.append([ price_things[i] / weight_thing[i],weight_thing[i]])
    for i in range(1,len(price_of_gram_and_weight_things)):
        key = price_of_gram_and_weight_things[i]
        j = i - 1
        while j >= 0  and price_of_gram_and_weight_things[j][0] > key[0]:
            price_of_gram_and_weight_things[j + 1] = price_of_gram_and_weight_things[j]
            j-=1
        price_of_gram_and_weight_things[j + 1] = key

end = len(price_of_gram_and_weight_things)
i = 1
while Limit > 0:
    if Limit - price_of_gram_and_weight_things[end - i][1] >= 0:
        Limit = Limit - price_of_gram_and_weight_things[end - i][1]
        answer = answer + price_of_gram_and_weight_things[end - i][0] * price_of_gram_and_weight_things[end - i][1]
    else:
        answer = answer + price_of_gram_and_weight_things[end - i][0] * Limit
        break
    i = i + 1
    if end - i == -1:
        break
print(round(answer,3))
