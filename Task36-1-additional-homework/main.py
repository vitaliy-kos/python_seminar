# Задание 1 необязательное 
# Сделайте локальный чат-бот с внешним хранилищем. 
# Тема чат-бота - любая вам интересная.

from random import *
import json

appointments = {}
doctors = ["Терапевт", "Стоматолог", "Травматолог", "Окулист", "Хирург"]
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
times = ["10:00", "12:00", "14:00", "16:00", "18:00"]

def save_one_appointment(phone, doc, day, time):
    appointments = get_appointments()
    appointments[phone] = [doc, day, time]

    with open("appointment.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(appointments, ensure_ascii=False))
    return

def save_appointments(appointments):
    with open("appointment.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(appointments, ensure_ascii=False))
    return

def cancel_appointment(phone):
    appointments = get_appointments()
    del appointments[phone]
    save_appointments(appointments)
    return

def get_appointments():
    with open("appointment.json", "r", encoding="utf-8") as fh:
        appointments = json.load(fh)
    return appointments

while True:
    command = input("Введите команду: ")

    if command == '/start':

        print("Бот записи к врачу начал свою работу!")

    if command == '/stop':

        print("Бот завершил свою работу. Обращайтесь снова, если необходимо.")
        break

    if command == '/appointment':

        print(f"Введите к какому доктору нужно записаться (Возможные варианты: {', '.join(doctors)}): ")
        doc = input()
        if doc not in doctors:
            print("Такого доктора нет в списке!")
            continue
        
        print(f"Выберите день, в который вам удобно посетить доктора (Возможные варианты: {', '.join(days)}): ")
        day = input()
        if day not in days:
            print("Указан несуществующий день недели!")
            continue
        
        print(f"Выберите время, в которое вам удобно (Возможные варианты: {', '.join(times)}): ")
        time = input()
        if time not in times:
            print("Указан несуществующий день недели!")
            continue

        print(f"Введите ваш номер телефона в формате 79779997799: ")
        phone = input()

        save_one_appointment(phone, doc, day, time)
        print(f"Вы успешно записались к доктору - {doc}, день - {day}, время - {time}. Ваш номер - {phone}")
        continue

    if command == '/cancel-appointment':

        cancel_phone = input("Введите Ваш номер для отмены записи:")

        cancel_appointment(cancel_phone)
        print("Запись отменена.")
        continue

    if command == '/help':

        print("Бот имеет следующие функции: /start - запуск бота, /stop - остановка бота, /appointment - записаться к врачу, /cancel-appointment - отменить запись, /help - посмотреть туториал")
    
    else:
        
        print("Неопознанная команда. Изучите мануал /help.")