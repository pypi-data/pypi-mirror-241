from clear import *
from sys import exit


def print_binary():
    print("Бинарный поиск. Введите цифру интересующего алгоритма\n"
          "1. Бинарный поиск слева направо\n"
          "2. Бинарный поиск справа налево\n"
          )
    answer = input()

    if answer == '1':
        print(
        "Бинарный поиск слева направо\n"
        "Элемент, массив -> индекс элемента\n\n"

        "def left_bound(element, massive):\n"
        "    left = -1\n"
        "    right = len(massive)\n"
        "    while right - left > 1:\n"
        "        middle = (left + right) // 2\n"
        "        if massive[middle] < element:\n"
        "            left = middle\n"
        "        else:\n"
        "            right = middle\n"
        "    return left + 1\n"
        )
        print_binary()
    elif answer == '2':
        print(
        "Бинарный поиск справа налево\n"    
        "Элемент, массив -> индекс элемента\n"
        "def right_bound(element, massive):\n"
        "    left = -1\n"
        "    right = len(element)\n"
        "    while right - left > 1:\n"
        "        middle = (left + right) // 2\n"
        "        if element[middle] <= massive:\n"
        "            left = middle\n"
        "        else:\n"
        "            right = middle\n"
        "    return right - 1\n"
        )
        print_binary()

    elif answer == 'exit':
        exit()
    elif answer.isalpha() == True and answer != 'exit':
        clear()
        print("Неправильная команда. Допустимые команды: 'exit'\n")
        print_binary()
    elif answer.isnumeric() == True and answer != '1' and answer != '2':
        clear()
        print("Неправильное число. Допустимые числа: '1', '2'\n")
        print_binary()
    else:
        clear()
        print("Ошибка ввода. Неправильный ввод\n")
        print_binary()
