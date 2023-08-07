# Задача 36: Напишите функцию вывода таблицы умножения 
# print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую 
# элемент по номеру строки и столбца. Аргументы num_rows и num_columns 
# указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно 
# два аргумента, как, например, у операции умножения.
# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1   2   3   4   5   6
# 2   4   6   8  10  12 
# 3   6   9  12  15  18 
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36

# Решение задачи без графического интерфейса

# def print_operation_table(func, num_rows = 6, num_columns = 6):
#     for x in range(1, num_columns + 1):
#         for y in range(1, num_rows + 1):
#             print("%4s" % func(x,y), end='')
#         print()

# print_operation_table(lambda x, y: x * y)

from tkinter import *
from tkinter import ttk

def print_operation_table(func, num_rows = 6, num_columns = 6):
    columns = [i for i in range(1, num_columns + 1)]
    table = ttk.Treeview(columns=columns, show="headings", height=num_rows-1, )
    table.grid(row=10, column=0, pady=30)

    for x in columns:
        table.heading(f"#{x}", text=f"{x}", anchor=W)
        table.column(f"#{x}", stretch=NO, width=60, anchor=CENTER)
        
    for y in range(2, num_rows + 1):
        row_values = []
        for x in columns:
            row_values.append(func(x,y))
        table.insert(parent='', index='end', iid=y, text="Label", values=row_values)

text_task = 'Напишите функцию вывода таблицы умножения print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.'

window = Tk()
window.title("Задача 36: Таблица умножения")
window.geometry('600x600')
window.resizable(0, 0)

header = Label(window, text="Задача 36", font=('Arial', '50'))
header.grid(column=0, row=0)

description = Label(window, text=text_task, font=('Arial', '18'), justify='center', wraplength=600)
description.grid(column=0, row=1, pady=30)

btn = Button(window, text="Вывести!", command=lambda: print_operation_table(lambda x, y: x * y))
btn.grid(column=0, row=4)

window.mainloop()