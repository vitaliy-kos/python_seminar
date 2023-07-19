# Дано натуральное число A > 1. Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# Input: 5 
# Output: 6

number = int(input("Введите число: "))
first_elem, second_elem, current = 0, 1, 1
count = 2

while current < number:
    current = first_elem + second_elem
    first_elem = second_elem
    second_elem = current
    count += 1


if current == number:
    print(f"{number}-й лемент Фибоначи = {count}")
else:
    print("-1")