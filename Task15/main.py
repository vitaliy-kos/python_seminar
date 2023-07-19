# Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. Понятно, что для себя нужно 
# выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать самый легкий 
# и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка 
# содержит N чисел, записанных на новой строчке каждое. Здесь каждое 
# число – это масса соответствующего арбуза

# Input: 5 -> 5 1 6 5 9 Output: 1 9

import random

amount_watermelons = int(input("Insert number of watermelons: "))
temps = []

for i in range(amount_watermelons):
    temps.append(int(input(f"Insert weight of {i+1} watermelon: ")))

max = temps[0]
min = temps[0]

for i in temps:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"Array weights of watermelons: {temps}")
print(f"Max weight of watermelon: {max}")
print(f"Min weight of watermelon: {min}")