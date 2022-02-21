
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