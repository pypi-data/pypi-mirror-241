"""
Утилита со всеми функциями для ПУМа (pum_def_9_1)
"""


from pum_def_9_1.binary import print_binary
from pum_def_9_1.linear import print_linear
from pum_def_9_1.sort import print_sort
from pum_def_9_1.clear import *
from sys import exit

def start():
    print("Введите цифру интересующей вас темы\n"
          "1. Линейный поиск\n"
          "2. Бинарный поиск\n"
          "3. Сортировки\n"
          "Для завершения работы введите 'exit'")
    select = input()

    if select == '1':
        print_linear()
    elif select == '2':
        print_binary()
    elif select == '3':
        print_sort()

    elif select == 'exit':
        exit()
    elif select.isalpha() == True and select != 'exit':
        clear()
        print("Неправильная команда. Допустимые команды: 'exit'\n")
        start()
    elif select.isnumeric() == True and select != '1' and select != '2' and select != '3':
        clear()
        print("Неправильное число. Допустимые числа: '1' '2' '3'\n")
        start()
    else:
        clear()
        print('Ошибка ввода. Неправильный ввод\n')
        start()


start()  #первичный запуск кода
