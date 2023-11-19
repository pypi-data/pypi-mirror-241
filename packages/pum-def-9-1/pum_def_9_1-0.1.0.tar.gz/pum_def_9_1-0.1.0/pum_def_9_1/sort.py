"""
Сортировка пузырьком

Массив -> отсортированный массив
"""
def buble_sort(massive):
    for i in range(len(massive) - 1):
        for j in range(len(massive) - i - 1):
            if massive[j + 1] < massive[j]:
                massive[j], massive[j + 1] = massive[j + 1], massive[j]
    return massive


"""
Сортировка выбором

Массив -> отсортированный массив
"""
def select_sort(massive):
    for i in range(len(massive) - 1):
        x = massive[i]
        m = i
        for j in range(i + 1, len(massive)):
            if massive[j] < x:
                x = massive[j]
                m = j
        massive[m], massive[i] = massive[i], massive[m]
    return massive


"""
Сортировка пузырьком

Массив -> отсортированный массив
"""
def insertion_sort(massive):
    for i in range(1,len((massive))):
        temp = massive[i]
        j = i - 1
        while (j >= 0 and temp < massive[j]):
            massive[j+1] = massive[j]
            j = j - 1
        massive[j+1] = temp
    return massive



"""
Сортировка пузырьком

Массив -> отсортированный массив
"""
from collections import defaultdict
def mx(massive):
    max_element = massive[0]
    for i in range(len(massive)):
        if massive[i] > max_element:
            max_element = massive[i]
    return max_element


def mn(massive):
    min_element = massive[0]
    for i in range(len(massive)):
        if massive[i] < min_element:
            min_element = massive[i]
    return min_element
def count_sort(massive):
    count = defaultdict(int)

    for i in massive:
        count[i] += 1
    result = []
    for j in range(mn(massive), (mx(massive)+1)):
        if count.get(j) is not None:
            for i in range(count.get(j)):
                result.append(j)
    return result


