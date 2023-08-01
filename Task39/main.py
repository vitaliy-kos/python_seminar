# Задача №39. Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива
# Пример:
# Ввод: 
# 7 
# 3 1 3 4 2 4 12 (каждое число вводится с новой строки)
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12

import random

# def list_gen(len):
#     new_list = []
#     for _ in range(n):
#         a = random.randint(0, 5)
#         new_list.append(a)
#     return new_list

n = int(input('Длина первого списка: '))
m = int(input('Длина второго списка: '))

first_list = [random.randint(0,11) for _ in range(n)]
print(first_list)
second_list = [random.randint(0,11) for _ in range(m)]
print(second_list)


compare = [i for i in first_list if i not in second_list]
print(compare)