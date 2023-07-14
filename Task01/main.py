# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# import math

print("Введите дистанцию маршрута в км: ")
interval = input()
print("Введите может машина проехать в день км:")
distPerDay = input()
# print(round(m / n))
# print(math.ceil(m / n))

res = int(interval / distPerDay)
res = res + (res % 2)
print(res)
