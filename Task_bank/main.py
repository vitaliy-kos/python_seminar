age = int(input("Введите ваш возраст: "))
salary = int(input("Введите ваш доход: "))
credits = int(input("Введите трату на обслуживание кредитов: "))
months = int(input("Введите предпочитаемый срок кредита: "))
creditSum = int(input("Введите желаемую сумму кредита: "))

ageMonths = age * 12
treshold = 50 * 12
duration = ageMonths + months > treshold
creditExpenses = credits + creditSum/months > salary / 2

if duration or creditExpenses:
    print("Отказ")
# elif  not duration and not creditExpenses:
else:
     print("Одобрено")