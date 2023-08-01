# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

min = int(input('Insert min value: '))
max = int(input('Insert max value: '))

rand_list = [random.randint(-100,100) for _ in range(10)]
print(rand_list)

indexes = []

for i in range(0, len(rand_list)):
    if rand_list[i] >= min and rand_list[i] <= max:
        indexes.append(i)

print(indexes)