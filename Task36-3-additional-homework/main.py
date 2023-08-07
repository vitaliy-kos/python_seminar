# Задание 3 тяжелое необязательное 
# Сделайте приложение Калькулятор аналогично встроенному в Windows.

from tkinter import *

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '+', '=', '4')
           )

calculation = ""
need_clear = False

def btn_click(item):
    global calculation
    global need_clear
    try:
        if need_clear:
            clear_input()
            need_clear = False

        input['state'] = "normal"
        calculation += item
        input.insert(END, item)

        if item == '=':
            result = str(eval(calculation[:-1]))
            input.delete(0, END)
            input.insert(0, result)
            calculation = ""
            need_clear = True

        input['state'] = "readonly"

    except SyntaxError:
        input.delete(0, END)
        input.insert(0, 'Error')

    except ZeroDivisionError:
        input.delete(0, END)
        input.insert(0, 'Error (devide by 0)')

def clear_input():
    global calculation
    calculation = ""
    input['state'] = "normal"
    input.delete(0, END)
    input['state'] = "readonly"

root = Tk()
root.geometry("300x290")
root.title("Калькулятор")
root.resizable(0, 0)

frame = Frame(root)
frame.grid(row=0, column=0, columnspan=4, sticky="nsew")

input = Entry(frame, font=('Arial', '35'), width=14, state="readonly", justify='right')
input.pack(fill=BOTH)

button = Button(root, text='Очистить', command=lambda: clear_input())
button.grid(row=1, column=3, sticky="nsew")

for row in range(4):
    for col in range(4):
        Button(root, width=1, height=1, text=buttons[row][col],
               command=lambda row=row, col=col: btn_click(buttons[row][col]), font=('Arial', '30')).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)

root.mainloop()