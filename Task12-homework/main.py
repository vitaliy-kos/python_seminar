# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Insert sum of numbers: "))
product = int(input("Insert product of numbers: "))

first_num = 0
second_num = 0

for x in range(sum):
    for y in range(product):
        if sum == x + y and product == x * y:
            first_num = x
            second_num = y

if first_num > 0:
    print(f'first number = {first_num}, second number = {second_num} ')
else:
    print(f'for theese combination not exist numbers')