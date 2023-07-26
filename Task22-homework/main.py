# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Insert quantity elements N: "))
list_1 = []
for i in range(n):
    num = int(input(f"Insert {i+1} number: "))
    list_1.append(num)
print(list_1)


m = (int(input("Insert quantity elements M: ")))
list_2 = []
for i in range(m):
    num = int(input(f"Insert {i+1} number: "))
    list_2.append(num)
print(list_2)


num_list3 = list_1 + list_2
result = []
for i in num_list3:
    if num_list3.count(i) > 1 and i not in result:
        result.append(i)

for i in range(len(result)):
    for j in range(len(result) - 1):
        if result[j] > result[j+1]:
            result[j+1], result[j] = result[j], result[j+1]

print(f"Resulted list is: {result}")