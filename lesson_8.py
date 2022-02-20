"""
Функции
"""


# ======= Inbuilt functions
# dict([object]) - преобразование к словарю.
# frozenset([последовательность]) – замороженная послеовательность
# int([object], [основание системы счисления])
# list([object]) - создает список.
# range([start=0], stop, [step=1])
# set([object]) - создает множество.
# str([object], [кодировка], [ошибки])
# tuple(obj) - преобразование к кортежу.
# complex([real[, imag]]) - преобразование к комплексному числу
# print(bool(4))
# print(bool())
# print(bool(None))
# print(bool(False))
# print(bool("False"))
#
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
#           "December"]
# month_with_numbers = dict(zip(months, list(range(1, 13))))
# print(month_with_numbers)


# =======================
# def add(x, y):
#     return \
#         x + y
# # --------
# b=add(15,59)
# print(b)
# c=add('abc', 'def')
# print(c)
# Sololearn: learn ot Code
# t=(1,2,3)
# a,b = t
# print(a)
# print(b)
# print(c)
# print(d)
# print(sum(range(10)))# # -------
# print(add(100, 120))
# # ----
# def compute_surface(radius: float) -> float:
#     from math import pi
#     return pi * radius * radius
#
#
# print(compute_surface(14.8))
# # =========
# def newfunc(n): #1 n=100, #2 n=200
#     def myfunc(x):
#         return x + n
#     return myfunc
# new = newfunc(100)  # new - это тоже функция  n=100
# print(myfunc(250))
# =========
# def function_sample(a, b, c=2):  # c - необязательный аргумент
#     return a + b + c
#
#
# print(function_sample(1, 2)) # a = 1, b = 2, c = 2 (по умолчанию)
# print(function_sample(1, 2, 3))  # a = 1, b = 2, c = 3
# print(function_sample(b=6, a=1, c=6)) # a = 3, c = 6, b не определен
# =============Глобальные и локальные переменные
# def f():
#     x = 100
#     print(x)
#
#
# f()  # >>100
#
# print(x)
# ==============
# x = 100
#
# from lesson_7 import dict_months
# def f():
#     print(x)
#
#
# f()
# print(dict_months['March'])
# # ==============
# def f():
#     global x  # Определение глобальной переменной
#     x = 200
#
#
# # f()
# print(x)


# ==============
# def check_passwd(username, password):
#     if len(password) < 8:
#         print('Пароль слишком короткий')
#         return False
#     elif username in password:
#         print('Пароль содержит имя пользователя')
#         return False
#     else:
#         print(f'Пароль для пользователя {username} прошел все проверки')
#         return True
#
# # print(check_passwd("Vania","Vania"))
# print(check_passwd(password='12345', username='nata'))


# ========== *args
#
# def adder(*nums):
#     sum = 0
#
#     for n in nums:
#         sum += n
#
#     print("Sum: ", sum)
#
#
# adder(3, 5)
# adder(4, 5, 6, 7)
# adder(1, 2, 3, 5, 6)
# ==========
def intro(**data):
    print("\nData type of argument: ", type(data))

    for key, value in data.items():
        print(f"{key} is {value}")

final_dict={}

# print(intro(Firstname="Sita",
#             Lastname="Sharma",
#             Age=22,
#             Phone=1234567890))
print(
    intro(Firstname="John",
          Lastname="Wood",
          Email="johnwood@nomail.com",
          Country="Wakanda",
          Age=25,
          Phone=9876543210))
# =================== Lambda
# sum_arg = lambda a, b: a + b
# print(sum_arg(1, 2))
# =========
# list_of_tuples = [('IT_VLAN', 320),('Mngmt_VLAN', 99),('User_VLAN', 1010),('DB_VLAN', 11)]
# y = sorted(list_of_tuples, key=lambda x: x[1])
# print(y)
# ========= Синтаксис функции генератора:
# def fibonacci(xterms):
#     # первые два условия
#     x1 = 0
#     x2 = 1
#     count = 0
#
#     if xterms <= 0:
#         print("Укажите целое число больше 0")
#     elif xterms == 1:
#         print("Последовательность Фибоначчи до", xterms, ":")
#         print(x1)
#     else:
#         while count < xterms:
#             xth = x1 + x2
#             x1 = x2
#             x2 = xth
#             count += 1
#             yield xth
#
#
# fib = fibonacci(33)
#
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# ==============
# Создаем список
# alist = [4, 16, 64, 256, 65536]
#
# # Вычислим квадратный корень, используя генерацию списка
# out = [a**(1/2) for a in alist]
# print(out)
#
# # Используем выражение генератора, чтобы вычислить квадратный корень
# out = (a**(1/2) for a in alist)
# print(out)
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out)) # после этого вызова будет StopIteration
# print(next(out))
# ========
# alist = ['Python', 'Java', 'C', 'C++', 'CSharp']
#
# def list_items():
#     for item in alist:
#         yield item
#
# gen = list_items()
#
# iter = 0
#
# while iter < len(alist):
#     print(next(gen))
#     iter += 1
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
