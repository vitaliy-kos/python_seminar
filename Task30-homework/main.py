# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Insert A value: "))
d = int(input("Insert D value: "))
n = int(input("Insert N value: "))
array = []

for i in range(n):
    array.append(a + i * d)

print(array)