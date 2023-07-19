# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

number = int(input("Insert number: "))
temp = []
i = 0

while 2 ** i <= number:
    temp.append(2 ** i)
    i += 1

print(f"Result: {temp}")

# --- дополнительная задача 1 сложная необязательная 
# Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

number = float(input("Insert number: "))
result = 0

while number != int(number):
    number *= 10

number = int(number)

while number > 0:
    result += number % 10
    number //= 10

print(f"Result: {result}")