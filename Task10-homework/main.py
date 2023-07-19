# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

amount_coins = int(input("Insert number of coins: "))
temps = []
heads, tails = 0, 0

for i in range(amount_coins):
    val = int(input(f"Insert value of {i+1} coin (heads(1) and tails(0)): "))
    if val == 1:
        heads += 1
    elif val == 0:
        tails +=1

if heads > tails:
    print(f"You need to turn {tails} tail coins.")
else:
    print(f"You need to turn {heads} head coins.")
