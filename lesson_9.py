# =============== Decorator
# def decorator_function(function_sample):
#     def wrapper():
#         print('Функция-обёртка!')
#         print(f'Оборачиваемая функция: {function_sample}')
#         print('Выполняем обёрнутую функцию...')
#         function_sample()
#         print('Выходим из обёртки')
#     return wrapper
# @decorator_function

# def hello_world():
#     print('Hello world!')
# print(hello_world())

# ==============Вариант №2
def decorator2(function_sample, *arg, **kwargs):
    print('Функция-обёртка!')
    print(f'Оборачиваемая функция: {function_sample}')
    print('Выполняем обёрнутую функцию...')
    function_sample(*arg, **kwargs)
    print('Выходим из обёртки')


# ============ Пример использования
# def benchmark(function_sample):
#     import time
#
#     def wrapper():
#         start = time.time()
#         function_sample()
#         end = time.time()
#         print(f'[*] Время выполнения: {end - start} секунд.')
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
#
#
# fetch_webpage()
# =========  Функция filter
# список чисел
# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#

# функция, которая проверяет числа
# def filter_odd_num(in_num):
#     if in_num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# out_filter = filter(filter_odd_num, numbers)
#
# print("Тип объекта out_filter: ", type(out_filter))
# print("Отфильтрованный список: ", list(out_filter))
#

# ========= map
# def square(number):
#     return number ** 2
#
#
# numbers = [1, 2, 3, 4, 5]
# squared = map(square, numbers)
# print(list(squared))
# =======
# Введение в Алгоритмы
# Операторы членства (Membership Operators)
# print('apple' in ['orange', 'apple', 'grape'],
#       't' in 'pythonist',
#       'q' in 'pythonist')

# Линейный поиск
# def LinearSearch(lys, element):
#     for i in range(len(lys)):
#         if lys[i] == element:
#             return i
#     return -1
#

# print(LinearSearch([1,2,3,4,5,2,1], 2))
# ================ Бинарный поиск через итеративную реализацию

"""
Предполагая, что мы ищем значение val в отсортированном массиве, 
алгоритм сравнивает val со значением среднего элемента массива, 
который мы будем называть mid. Если mid — это тот элемент, который мы ищем (в лучшем случае), 
мы возвращаем его индекс.
Если нет, мы определяем, в какой половине массива мы будем искать val дальше, 
основываясь на том, меньше или больше значение val значения mid, и отбрасываем вторую половину массива.
Затем мы рекурсивно или итеративно выполняем те же шаги, выбирая новое значение для mid, 
сравнивая его с val и отбрасывая половину массива на каждой итерации алгоритма.
"""

#
# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys) - 1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first + last) // 2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val < lys[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index


# print(
#     BinarySearch([10,20,30,40,50], 10),
#     BinarySearch([10,20,30,40,50], 20),
#     BinarySearch([10,20,30,40,50], 30),
#     BinarySearch([10,20,30,40,50], 40),
#     BinarySearch([10,20,30,40,50], 50),
#     BinarySearch([10,20,30,40,50], 9),
#     BinarySearch([10,20,30,40,50], 51),
#     BinarySearch([10,20,30,40,50], 100)
# )
# print(
#     BinarySearch([4, 4, 4, 4, 4], 4),  # -> 2
#     LinearSearch([4, 4, 4, 4, 4], 4),  # 0
#     BinarySearch([1, 2, 3, 4, 4, 4, 5], 4)  # -> 3  Проверяєм работает ли алгоритм
# )
# ================== Jump Search
# import math
#
#
# def JumpSearch(lys, val):
#     length = len(lys)
#     jump = int(math.sqrt(length))
#     left, right = 0, 0
#     while left < length and lys[left] <= val:
#         right = min(length - 1, left + jump)
#         if lys[left] <= val <= lys[right]:
#             break
#         left += jump
#     if left >= length or lys[left] > val:
#         return -1
#     right = min(length - 1, right)
#     i = left
#     while i <= right and lys[i] <= val:
#         if lys[i] == val:
#             return i
#         i += 1
#     return -1
#
#
# print(
#     JumpSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
#     JumpSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
# )

# https://techrocks.ru/2020/08/12/python-search-algorithms/
# Сортировка методом "Пузырька" помощью циклов for
from datetime import datetime
from random import randint

''' random list with 10 position generating'''
N = 10000
a = []
for i in range(N):
    a.append(randint(1, 99))


# print(a)
# bubble_solting_using_for
def bubble_solting_using_for(arr: list) -> list:
    for i in range(len(arr) - 1):
        for j in range((len(arr) - i - 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# bubble_solting_using_while
def bubble_solting_using_while(arr: list) -> list:
    i = 0
    while i < len(arr) - 1:
        j = 0
        while j < len(arr) - 1 - i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
    return arr


# print(bubble_solting_using_for(a))
# print(bubble_solting_using_while(a))

# bubble_solting_using_for(a)

def decorator_function2(function_sample, *param1, **param2):
    time_start = datetime.now()
    function_sample(*param1, **param2)
    time_end = datetime.now()
    print(f'Runtime for execution of {str(function_sample)} is {time_end-time_start}')


decorator_function2(bubble_solting_using_for, a)
decorator_function2(bubble_solting_using_while, a)


# Сортировка выбором
def select_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]


decorator_function2(select_sort, a)
# Сортировка вставками
