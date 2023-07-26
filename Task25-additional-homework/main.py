# задача 1 необязательная. Напишите программу, которая получает целое число и 
# возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# * Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

def rev(list):
    result = []
    for i in list:
        result.insert(0, i)
    return result

def get_string(list):
    result = ''
    for i in list:
        result = result + str(i)
    return result

inserted_number = int(input ("Insert number: "))
rate = int(input("Insert calculus systems: "))
num = inserted_number

numbers = []
remain = rate

while remain <= num:
    numbers.append(num % rate)
    num = num // rate
numbers.append(num)

true_list = rev(numbers)
str = get_string(true_list)

print(f'Number {inserted_number} in {rate} calculus systems = {str}')

print(f"Checking with bin function: {bin(inserted_number)}")
print(f"Checking with oct function: {oct(inserted_number)}")