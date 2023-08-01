# Задача №41. Дан массив, состоящий из целых чисел. Напишите программу, которая в 
# данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Пример:
# Ввод:              Ввод:
# 5                  5
# 12345              1 5 1 5 1
# Вывод:             Вывод:
# 0                  2
import random

def find_elems(my_list):
    count = 0

    for i in range(len(my_list)):
        prev_index = (i-1) % n
        next_index = (i+1) % n
        prev = my_list[prev_index]
        cur = my_list[i]
        next = my_list[next_index]

        if prev < cur and next < cur:
            count += 1

    return count

n = int(input('Длина списка: '))
my_list = [random.randint(0,11) for _ in range(n)]

print(my_list)
print(find_elems(my_list))