# Задача №3. Общее обсуждение
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# import math

print("Введите количество учащихся в первом классе: ")
# a = math.ceil(int(input()) / 2)
a = int(input())
a = int(a / 2) + (a % 2)
print("Введите количество учащихся во втором классе: ")
# b = math.ceil(int(input()) / 2)
b = int(input())
b = int(b / 2) + (b % 2)
print("Введите количество учащихся в третьем классе: ")
# c = math.ceil(int(input()) / 2)
c = int(input())
c = int(c / 2) + (c % 2)

sum = a + b + c

print(f"Результат: {sum}")

