import tkinter as tk
import math

# значение а принимает последнии введенный знак математической операции, это необходимо для правильного создания дробных чисел
a = ' '
b, b1 = 0, 0
# Переменные под ячейки памяти
memory, memory1, memory2, memory3, memory4, memory5, memory6, memory7, memory8, memory9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


# Функция с помощью которой добавляются цифры в окно вывода
def add_digit(digit):
    value = text.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    text.delete(0, tk.END)
    text.insert(0, value + str(digit))


# Функция добавляющая символ математической операции
def add_funk(digit):
    value = text.get()
    if value[-1] in '+ - * / ^':
        value = value[:-1]
    text.delete(0, tk.END)
    text.insert(0, value + str(digit))
    global a
    a = digit


# Функция извлечения корня
def koren():
    try:
        value = text.get()
        value = 'math.sqrt(' + value + ')'
        text.delete(0, tk.END)
        text.insert(0, eval(value))
    except(ValueError, SyntaxError, NameError):
        text.insert(0, 'Ошибка')


# Функция меняющая знак числа
def znak():
    value = text.get()
    value = eval(value)
    value = '-1*' + str(value)
    text.delete(0, tk.END)
    text.insert(0, eval(value))


# Создание дробного числа
def drobi():
    value = text.get()
    index = value.rfind(a)
    val = value[index + 1:len(value) + 1]
    if "." not in val:
        value = value + '.'
    text.delete(0, tk.END)
    text.insert(0, value)


# Функция обозначающая команду равно
def calc():
    try:
        value = text.get()
        if '^' in value:
            value = value.replace('^', '**')
        text.delete(0, tk.END)
        text.insert(0, eval(value))
    except(ZeroDivisionError, NameError, SyntaxError):
        text.insert(0, 'Ошибка')


# Функция очищающая окно вывода
def delete():
    text.delete(0, tk.END)
    text.insert(0, 0)


# Функция очищающая окно ID
def delta2():
    text2.delete(0, tk.END)


# работа с ячейками памяти
# Прибаление значения к ячейке памяти
def M_plus():
    value = text.get()
    global memory
    memory = memory + int(value)


# Вычитание значения из ячейки памяти
def M_minus():
    value = text.get()
    global memory
    memory = memory - int(value)


# Чтение из ячейки памяти
def MR():
    text.delete(0, tk.END)
    text.insert(0, memory)


# Сохранение в ячейку памяти
def MS():
    value = text.get()
    global memory
    memory = int(value)


# Очищение яцейки памяти
def MC():
    global memory
    memory = 0
    text.delete(0, tk.END)
    text.insert(0, memory)


# Переход в расширенный режим калькулятора
def Rachireni_regim():
    global b, btn7, btn_kovichki, btn_proz, btn_strelka, btn_odinX, btn_kvadrat, btn_CE, btn3, btn4, btn5, btn6, text2

    # Очищение окна ID
    def delete2():
        text2.delete(0, tk.END)

    # Вычисление суммы трех последних цифр для создания нужного количества ячеек памяти
    def rekursia():
        try:
            z = text2.get()
            p = int(z[-1]) + int(z[-2]) + int(z[-3])
            if p > 9:
                p = str(p)
                p = int(p[0]) + int(p[1])
            text2.delete(0, tk.END)
            text2.insert(0, p)
            make_button(p)
        except IndexError:
            text2.delete(0, tk.END)

    # Удаление по одному значению справа налево в окне вывода
    def sterka():
        value = text.get()
        value = value[:len(value) - 1]
        text.delete(0, tk.END)
        text.insert(0, value)

    # Возведение в квадрат
    def square():
        value = float(text.get())
        value = value ** 2
        text.delete(0, tk.END)
        text.insert(0, value)

    # Взятие процента от введенного числа
    def procent():
        value = float(text.get())
        value = value / 100
        text.delete(0, tk.END)
        text.insert(0, value)

    # Деление единицы на введенное число
    def delenie_na_1():
        try:
            value = float(text.get())
            value = 1 / value
            text.delete(0, tk.END)
            text.insert(0, value)
        except(ZeroDivisionError, ValueError):
            text.delete(0, tk.END)
            text.insert(0, 'NONE')

    # Вычисление синуса
    def sinus():
        value = text.get()
        value = 'math.sin(' + value + ')'
        value = eval(value)
        text.delete(0, tk.END)
        text.insert(0, value)

    # Вычисление косинуса
    def cosinus():
        value = text.get()
        value = 'math.cos(' + value + ')'
        value = eval(value)
        text.delete(0, tk.END)
        text.insert(0, value)

    # Вычисление тангенса
    def tangens():
        value = text.get()
        value = 'math.tan(' + value + ')'
        value = eval(value)
        text.delete(0, tk.END)
        text.insert(0, value)

    # Вычисление тангенса
    def logorifm():
        value = text.get()
        value = 'math.log(' + value + ')'
        value = eval(value)
        text.delete(0, tk.END)
        text.insert(0, value)

    # Возведение числа в третью степень
    def kub():
        value = float(text.get())
        value = value ** 3
        text.delete(0, tk.END)
        text.insert(0, value)

    # Функции для работы с первой ячейкой памяти расширенного режима
    # Функции для работы с первой ячейкой памяти
    def M_plus_1():
        global memory1
        value = text.get()
        memory1 = memory1 + int(value)

    def M_minus_1():
        global memory1
        value = text.get()
        memory1 = memory1 - int(value)

    def MR_1():
        text.delete(0, tk.END)
        text.insert(0, memory1)

    def MS_1():
        global memory1
        value = text.get()
        memory1 = int(value)

    def MC_1():
        global memory1
        memory1 = 0
        text.delete(0, tk.END)
        text.insert(0, memory1)

    # Функции для работы со второй ячейкой памяти расширенного режима
    def M_plus_2():
        global memory2
        value = text.get()
        memory2 = memory2 + int(value)

    def M_minus_2():
        global memory2
        value = text.get()
        memory2 = memory2 - int(value)

    def MR_2():
        text.delete(0, tk.END)
        text.insert(0, memory2)

    def MS_2():
        global memory2
        value = text.get()
        memory2 = int(value)

    def MC_2():
        global memory2
        memory2 = 0
        text.delete(0, tk.END)
        text.insert(0, memory2)

    # Функции для работы с третьей ячейкой памяти расширенного режима
    def M_plus_3():
        global memory3
        value = text.get()
        memory3 = memory3 + int(value)

    def M_minus_3():
        global memory3
        value = text.get()
        memory3 = memory3 - int(value)

    def MR_3():
        text.delete(0, tk.END)
        text.insert(0, memory3)

    def MS_3():
        global memory3
        value = text.get()
        memory3 = int(value)

    def MC_3():
        global memory3
        memory3 = 0
        text.delete(0, tk.END)
        text.insert(0, memory3)

    # Функции для работы с четвертой ячейкой памяти расширенного режима
    def M_plus_4():
        global memory4
        value = text.get()
        memory4 = memory4 + int(value)

    def M_minus_4():
        global memory4
        value = text.get()
        memory4 = memory4 - int(value)

    def MR_4():
        text.delete(0, tk.END)
        text.insert(0, memory4)

    def MS_4():
        global memory4
        value = text.get()
        memory4 = int(value)

    def MC_4():
        global memory4
        memory4 = 0
        text.delete(0, tk.END)
        text.insert(0, memory4)

    # Функции для работы с пятой ячейкой памяти расширенного режима
    def M_plus_5():
        global memory5
        value = text.get()
        memory5 = memory5 + int(value)

    def M_minus_5():
        global memory5
        value = text.get()
        memory5 = memory5 - int(value)

    def MR_5():
        text.delete(0, tk.END)
        text.insert(0, memory5)

    def MS_5():
        global memory5
        value = text.get()
        memory5 = int(value)

    def MC_5():
        global memory5
        memory5 = 0
        text.delete(0, tk.END)
        text.insert(0, memory5)

    # Функции для работы с шестой ячейкой памяти расширенного режима
    def M_plus_6():
        global memory6
        value = text.get()
        memory6 = memory6 + int(value)

    def M_minus_6():
        global memory6
        value = text.get()
        memory6 = memory6 - int(value)

    def MR_6():
        text.delete(0, tk.END)
        text.insert(0, memory6)

    def MS_6():
        global memory6
        value = text.get()
        memory6 = int(value)

    def MC_6():
        global memory6
        memory6 = 0
        text.delete(0, tk.END)
        text.insert(0, memory6)

    # Функции для работы с седьмой ячейкой памяти расширенного режима
    def M_plus_7():
        global memory7
        value = text.get()
        memory7 = memory7 + int(value)

    def M_minus_7():
        global memory7
        value = text.get()
        memory7 = memory7 - int(value)

    def MR_7():
        text.delete(0, tk.END)
        text.insert(0, memory7)

    def MS_7():
        global memory7
        value = text.get()
        memory7 = int(value)

    def MC_7():
        global memory7
        memory7 = 0
        text.delete(0, tk.END)
        text.insert(0, memory7)

    # Функции для работы с восьмой ячейкой памяти расширенного режима
    def M_plus_8():
        global memory8
        value = text.get()
        memory8 = memory8 + int(value)

    def M_minus_8():
        global memory8
        value = text.get()
        memory8 = memory8 - int(value)

    def MR_8():
        text.delete(0, tk.END)
        text.insert(0, memory8)

    def MS_8():
        global memory8
        value = text.get()
        memory8 = int(value)

    def MC_8():
        global memory8
        memory8 = 0
        text.delete(0, tk.END)
        text.insert(0, memory8)

    # Функции для работы с девятой ячейкой памяти расширенного режима
    def M_plus_9():
        global memory9
        value = text.get()
        memory9 = memory9 + int(value)

    def M_minus_9():
        global memory9
        value = text.get()
        memory9 = memory9 - int(value)

    def MR_9():
        text.delete(0, tk.END)
        text.insert(0, memory9)

    def MS_9():
        global memory9
        value = text.get()
        memory9 = int(value)

    def MC_9():
        global memory9
        memory9 = 0
        text.delete(0, tk.END)
        text.insert(0, memory9)

    # Изменение размеров окна, создание и удаление нужных кнопок при переходе в расширенный режим
    if b % 2 == 0:
        win.geometry('865x832+60+10')
        btn3.destroy()
        btn4.destroy()
        btn5.destroy()
        btn6.destroy()
        btn7.destroy()
        btn_kovichki = tk.Button(win, width=8, height=3, text='< >', bg='red', fg='white', command=rekursia)
        btn_kovichki.place(x=110, y=145)
        btn_proz = tk.Button(win, width=8, height=3, text='%', bg='#0000CD', fg='white', command=procent)
        btn_proz.place(x=30, y=215)
        btn_strelka = tk.Button(win, width=8, height=3, text='←', bg='#0000CD', fg='white', command=sterka)
        btn_strelka.place(x=110, y=215)
        btn_odinX = tk.Button(win, width=8, height=3, text='1/x', bg='#0000CD', fg='white', command=delenie_na_1)
        btn_odinX.place(x=190, y=215)
        btn_kvadrat = tk.Button(win, width=8, height=3, text='x^2', bg='#0000CD', fg='white', command=square)
        btn_kvadrat.place(x=270, y=215)
        btn_CE = tk.Button(win, width=8, height=3, text='CE', bg='red', fg='white', command=delete2)
        btn_CE.place(x=350, y=215)
        text2 = tk.Entry(win, width=14, bg='snow2', fg='black', font='Arial, 24')
        text2.place(x=480, y=40, height=30)
        label_1 = tk.Label(win, text='Черкашин Артем Сергеевич', font='Arial, 14', bg='#C0C0C0')
        label_1.place(x=450, y=10)
        label_2 = tk.Label(win, text='ID', font='Arial, 14', bg='#C0C0C0')
        label_2.place(x=450, y=40)
        btn_sin = tk.Button(win, width=8, height=3, text='sin', bg='#696969', fg='white', command=sinus)
        btn_sin.place(x=430, y=145)
        btn_cos = tk.Button(win, width=8, height=3, text='cos', bg='#696969', fg='white', command=cosinus)
        btn_cos.place(x=510, y=145)
        btn_tan = tk.Button(win, width=8, height=3, text='tan', bg='#696969', fg='white', command=tangens)
        btn_tan.place(x=590, y=145)
        btn_ln = tk.Button(win, width=8, height=3, text='Ln', bg='#696969', fg='white', command=logorifm)
        btn_ln.place(x=670, y=145)
        btn_x3 = tk.Button(win, width=8, height=3, text='x^3', bg='#696969', fg='white', command=kub)
        btn_x3.place(x=750, y=145)

        # Создание ячеек памяти расширенного режима
        def make_button(p):
            x4 = 430
            y = 145
            for i in range(p):
                spisok_func_summ = [M_plus_1, M_plus_2, M_plus_3, M_plus_4, M_plus_5, M_plus_6, M_plus_7, M_plus_8,
                                    M_plus_9]
                spisok_func_minus = [M_minus_1, M_minus_2, M_minus_3, M_minus_4, M_minus_5, M_minus_6, M_minus_7,
                                     M_minus_8, M_minus_9]
                spisok_read = [MR_1, MR_2, MR_3, MR_4, MR_5, MR_6, MR_7, MR_8, MR_9]
                spisok_save = [MS_1, MS_2, MS_3, MS_4, MS_5, MS_6, MS_7, MS_8, MS_9]
                spisok_clean = [MC_1, MC_2, MC_3, MC_4, MC_5, MC_6, MC_7, MC_8, MC_9]
                y = y + 70
                bttn_1 = tk.Button(win, width=8, height=3, text='MC', bg='red', fg='white', command=spisok_clean[i])
                bttn_1.place(x=x4, y=y)
                bttn_2 = tk.Button(win, width=8, height=3, text='MR', bg='red', fg='white', command=spisok_read[i])
                bttn_2.place(x=x4 + 80, y=y)
                bttn_3 = tk.Button(win, width=8, height=3, text='MS', bg='red', fg='white', command=spisok_save[i])
                bttn_3.place(x=x4 + 160, y=y)
                bttn_4 = tk.Button(win, width=8, height=3, text='M+', bg='red', fg='white', command=spisok_func_summ[i])
                bttn_4.place(x=x4 + 240, y=y)
                bttn_5 = tk.Button(win, width=8, height=3, text='M-', bg='red', fg='white',
                                   command=spisok_func_minus[i])
                bttn_5.place(x=x4 + 320, y=y)
                label = tk.Label(win, text=i + 1, width=2, height=2, bg='#0000CD', fg='white')
                label.place(x=x4 + 410, y=y + 10)

        b = b + 1
    # Переход обратно в обычный режим, удаление созданных и создание начальных кнопок, уменьшение размеров окна
    else:
        win.geometry('430x550+60+10')
        btn_kovichki.destroy()
        btn_proz.destroy()
        btn_strelka.destroy()
        btn_odinX.destroy()
        btn_kvadrat.destroy()
        btn_CE.destroy()
        btn3 = tk.Button(win, width=8, height=3, text='MC', bg='snow4', fg='white', command=MC)
        btn3.place(x=30, y=215)
        btn4 = tk.Button(win, width=8, height=3, text='MR', bg='snow4', fg='white', command=MR)
        btn4.place(x=110, y=215)
        btn5 = tk.Button(win, width=8, height=3, text='MS', bg='snow4', fg='white', command=MS)
        btn5.place(x=190, y=215)
        btn6 = tk.Button(win, width=8, height=3, text='M+', bg='snow4', fg='white', command=M_plus)
        btn6.place(x=270, y=215)
        btn7 = tk.Button(win, width=8, height=3, text='M-', bg='snow4', fg='white', command=M_minus)
        btn7.place(x=350, y=215)
        b = b + 1


# Создание базового окна и окна вывода(Entry), задание их параметров
win = tk.Tk()
win.title('Калькулятор - обычный режим ')
win.geometry('430x550+60+10')
win.config(bg='#C0C0C0')
win.resizable(False, False)
text = tk.Entry(win, width=15, bg='snow2', fg='black', justify=tk.RIGHT, font='Arial, 34')
text.insert(0, '0')
text.place(x=35, y=10, height=80)
# Создание и размещение кнопок
btn1 = tk.Button(win, width=8, height=3, text='≡', bg='red', fg='white', command=Rachireni_regim)
btn1.place(x=30, y=145)
btn2 = tk.Button(win, width=4, height=1, text='C', bg='red', fg='white', font='Times 20', command=delete)
btn2.place(x=346, y=146)
btn3 = tk.Button(win, width=8, height=3, text='MC', bg='snow4', fg='white', command=MC)
btn3.place(x=30, y=215)
btn4 = tk.Button(win, width=8, height=3, text='MR', bg='snow4', fg='white', command=MR)
btn4.place(x=110, y=215)
btn5 = tk.Button(win, width=8, height=3, text='MS', bg='snow4', fg='white', command=MS)
btn5.place(x=190, y=215)
btn6 = tk.Button(win, width=8, height=3, text='M+', bg='snow4', fg='white', command=M_plus)
btn6.place(x=270, y=215)
btn7 = tk.Button(win, width=8, height=3, text='M-', bg='snow4', fg='white', command=M_minus)
btn7.place(x=350, y=215)
btn8 = tk.Button(win, width=8, height=3, text='7', fg='#0000FF', command=lambda: add_digit(7))
btn8.place(x=30, y=285)
btn9 = tk.Button(win, width=8, height=3, text='8', fg='#0000FF', command=lambda: add_digit(8))
btn9.place(x=110, y=285)
btn10 = tk.Button(win, width=8, height=3, text='9', fg='#0000FF', command=lambda: add_digit(9))
btn10.place(x=190, y=285)
btn11 = tk.Button(win, width=8, height=3, text='/', bg='snow4', fg='white', command=lambda: add_funk('/'))
btn11.place(x=270, y=285)
btn12 = tk.Button(win, width=8, height=3, text='x^y', bg='snow4', fg='white', command=lambda: add_funk('^'))
btn12.place(x=350, y=285)
btn13 = tk.Button(win, width=8, height=3, text='4', fg='#0000FF', command=lambda: add_digit(4))
btn13.place(x=30, y=355)
btn14 = tk.Button(win, width=8, height=3, text='5', fg='#0000FF', command=lambda: add_digit(5))
btn14.place(x=110, y=355)
btn15 = tk.Button(win, width=8, height=3, text='6', fg='#0000FF', command=lambda: add_digit(6))
btn15.place(x=190, y=355)
btn16 = tk.Button(win, width=8, height=3, text='*', bg='snow4', fg='white', command=lambda: add_funk('*'))
btn16.place(x=270, y=355)
btn17 = tk.Button(win, width=8, height=3, text='√', bg='snow4', fg='white', command=koren)
btn17.place(x=350, y=355)
btn18 = tk.Button(win, width=8, height=3, text='1', fg='#0000FF', command=lambda: add_digit(1))
btn18.place(x=30, y=420)
btn19 = tk.Button(win, width=8, height=3, text='2', fg='#0000FF', command=lambda: add_digit(2))
btn19.place(x=110, y=420)
btn20 = tk.Button(win, width=8, height=3, text='3', fg='#0000FF', command=lambda: add_digit(3))
btn20.place(x=190, y=420)
btn21 = tk.Button(win, width=8, height=3, text='-', bg='snow4', fg='white', command=lambda: add_funk('-'))
btn21.place(x=270, y=420)
btn22 = tk.Button(win, width=8, height=3, text='+/-', bg='snow4', fg='white', command=znak)
btn22.place(x=350, y=420)
btn23 = tk.Button(win, width=19, height=3, text='0', fg='#0000FF', command=lambda: add_digit(0))
btn23.place(x=30, y=490)
btn24 = tk.Button(win, width=8, height=3, text='.', fg='#0000FF', command=drobi)
btn24.place(x=190, y=490)
btn25 = tk.Button(win, width=8, height=3, text='+', bg='snow4', fg='white', command=lambda: add_funk('+'))
btn25.place(x=270, y=490)
btn26 = tk.Button(win, width=8, height=3, text='=', bg='#0000CD', fg='white', command=calc)
btn26.place(x=350, y=490)
win.mainloop()
