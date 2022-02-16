"""
Коллекции: Множества и Словари
Set, Frozenset, Dict
"""
#
# mySet = {'c', 'a', 't'}
# # выводится в любом случайном порядке
# print(mySet) # {'t', 'c', 'a'}
#
# wrong_empty_set = {}
# print(type(wrong_empty_set)) # <class "dict">
#
# new_set1 = {1,2,3}
# new_set2 = {3,2,1}
# print(new_set1==new_set2)
# # ===============================
# color_list = ["red", "green", "green", "blue", "purple", "purple"]
# color_set = set(color_list)
# print(color_set)
#
# # порядок может быть другим зависит от версии питона
# # {"red", "purple", "blue", "green"}
#
# print(len(color_set))
# =====================
# tremendously_huge_set = {"red", "green", "blue"}
#
# if "green" in tremendously_huge_set:
#     print("Green is there!")
# else:
#     print("Unfortunately, there is no green...")
# =============
# words = ['a', 'a', 'b', 'b', 'c', 'd', 'e']
# # mySet = set(words)
# # print(mySet)  # run several times to see magic )))
# ==========
# colors = {"red", "green", "blue"}
#
# for color in colors:
#     print(color) # run several times to see magic )))
# ============
# my_cats = {"bear", "pig", "cat", "cat"}
# your_cats = {"pig", "pig", "bear", "cat", "cat"}
# print(my_cats == your_cats)

# ============
# even_numbers = {i for i in range(10) if i % 2 == 0}
# odd_numbers = {i for i in range(10) if i % 2 == 1}
# # Очевидно, что множества чётных и нечётных чисел не пересекаются
# print((even_numbers))
# print(odd_numbers)
# if even_numbers.isdisjoint(odd_numbers):
#     print("Множества не пересекаются!")
# =======================
# # Множество чисел Фибоначчи меньших 100
# fibonacci_numbers = {0, 1, 2, 3, 34, 5, 8, 13, 21, 55, 89}
#
# # Множество натуральных чисел меньших 100
# natural_numbers = set(range(100))
#
# # Множество чисел Фибоначчи является подмножеством множества
# # натуральных чисел
# if fibonacci_numbers.issubset(natural_numbers):
#     print("Подмножество!")
#
# # В свою очередь множество натуральных чисел является
# # надмножеством множества чисел Фибоначчи
# if natural_numbers.issuperset(fibonacci_numbers):
#     print("Надмножество!")
# ===============
# my_fruits = {"apple", "orange"}
# your_fruits = {"orange", "banana", "pear"}

# Для объединения множеств можно использовать оператор `|`,
# оба операнда должны быть объектами типа set
# our_fruits = my_fruits | your_fruits
# print(our_fruits)
#
# # Вывод (порядок может быть другим): {"apple", "banana", "orange", "pear"}
#
# # Также можно использовать метод union.
# # Отличие состоит в том, что метод union принимает не только
# # объект типа set, а любой iterable-объект
# you_fruit_list: list = list(your_fruits)
# our_fruits: set = my_fruits.union(you_fruit_list)
# print(our_fruits)
# ===============
# colors = {"red", "green", "blue"}
#
# # Метод add добавляет новый элемент в множество
# colors.add("purple")
# # Добавление элемента, который уже есть в множестве, не изменяет
# # это множество
# colors.add("red")
# print(colors)

# ============ Set Update
# numbers = {1, 2, 3}
# numbers.update(i**2 for i in [1, 2, 3])
# print(numbers)
# ============ Разность двух множеств
# i_know: set = {"Python", "Go", "Java"}
# you_know: dict = {
#     "Go": 0.4,
#     "C++": 0.6,
#     "Delphi": 0.2,
#     "Java": 0.9
# }
#
# you_know_but_i_dont = set(you_know) - i_know # Обратите внимание, что оператор `-` работает только для объектов типа set
# print(you_know_but_i_dont)
#
# # Метод difference может работать с любым iterable-объектом,
# # каким является dict, например
# i_know_but_you_dont = i_know.difference(you_know)
# print(i_know_but_you_dont)

# ========================= Удаление элемента
# fruits = {"apple", "orange", "banana"}
#
# # Удаление элемента из множества.
# fruits.discard("orange")
# fruits.discard("pineapple")  #Если удаляемого элемента нет в множестве, то ничего не происходит
# print(fruits)

# # Вывод (порядок может быть другим):
# {"apple", "banana"}
#
# # Метод remove работает аналогично discard, но генерирует исключение,
# # если удаляемого элемента нет в множестве
# fruits.remove("pineapple")  # KeyError: "pineapple"

# ========== Симметрическая разность множеств
# это множество, включающее все элементы исходных множеств, не принадлежащие одновременно обоим исходным множествам
# non_positive = {-3, -2, -1, 0}
# non_negative = {0, 1, 2, 3} # или используется set(range(4))
# # Обратите внимание, что оператор `^` может применяться только для объектов типа set
# non_zero = non_positive ^ non_negative
# print(non_zero)

# ==================== Frozenset
# setCat = set('кот')
# frozenCat = frozenset('кот')
# print(setCat == frozenCat)
#
# print(type(setCat))    # set
# print(type(frozenCat)) #frozenset
#
# setCat.add('э') # можем добавить
# print(setCat)
# setCat.
# frozenCat.add('e') # эта строка вызовет ошибку при компиляции
# ==================== DICTs
# Создадим пустой словать Capitals
# Capitals = dict()

# Заполним его несколькими значениями
# Capitals['Hungary'] = 'Budapest'
# Capitals['Ukraine'] = 'Kiev'
# Capitals['USA'] = 'Washington'
# Capitals['Turkey'] = 'Ankara'
# Capitals['France'] = 'Paris'
#
#
# Countries = ['Hungary', 'France', 'USA','Turkey', 'Russia']

# print(Capitals)
# for country in Countries:
#     # Для каждой страны из списка проверим, есть ли она в словаре Capitals
#     if country in Capitals:
#         print('Столица страны ' + country + ': ' + Capitals[country])
#     else:
#         print('В базе нет страны c названием ' + country)
# =============
# Capitals = {'Hungary': 'Budapest', 'Ukraine': 'Kiev', 'USA': 'Washington'}
# Capitals = dict(Hungary = 'Budapest', Ukraine = 'Kiev', USA = 'Washington')
# Capitals = dict([("Hungary", "Budapest"), ("Ukraine", "Kiev"), ("USA", "Washington")])
# capitals_of_the_countries = dict(zip(["Hungary", "Ukraine", "USA"], ["Budapest", "Kiev", "Washington"]))
# print(Capitals)
# ============== Работа с элементами словаря
import copy

#
# a = {'ab': 'ba', 'aa': 'aa', 'bb': 'bx', 'ba': 'ab'}  # a= {}
# a["ab"] = "ax"
# copy_a = copy.copy(a)
# deepcopy_a = copy.deepcopy(a)
# copy_a["ab"] = "ax"
# print(copy_a, deepcopy_a)
# https://pythonworld.ru/moduli/modul-copy.html
# #
# key = 'ba'
# try:
#     del a[key]
# except KeyError:
#     print(f'There is no element with key {key} in dict')
# print(a)


# ============ Перебор элементов словаря
# a = dict(zip('abcdef', list(range(6))))
# for key in a:
#     print(key, a[key])

# # =============================== fromkeys
# # dictionary.fromkeys(sequence[, value])
# colors = {"red", "green", "blue"}
# # numbers = range(13)
# new_dict = dict.fromkeys(colors, "name")
# # new_dict2=
# print(new_dict)
#
# # vowels keys
# keys = {'a', 'e', 'i', 'o', 'u' }
# value = [1]
#
# vowels = dict.fromkeys(keys, value)
# print(vowels)
#
# # updating the value
# value.append(2)
# print(vowels)
# ============= get

# a = {'ab': 'ba', 'aa': 'aa', 'bb': 'bx', 'ba': 'ab'}  # a= {}
# print(a.get('ab'))
# # ================= items v python 3.x and viewitems() in ver2.x
# # print(type(a.items()))
# print(a.popitem())
# person = {'name': 'Phill', 'age': None, 'salary': 3500.0}

# # ('salary', 3500.0) is inserted at the last, so it is removed.
# result = person.popitem()
#
# print('Return Value = ', result)
# print('person = ', person)
#
# # inserting a new element pair
# person['profession'] = 'Plumber'
#
# # now ('profession', 'Plumber') is the latest element
# result = person.popitem()
#
# print('Return Value = ', result)
# person.pop('salary')
# print(person)
# age = person.setdefault('age', 22)
# age = person.get('age')
# person = {'name': 'Phill', 'age': 22}
# print('age =', age)
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
numbers = range(1, 13)

dict_months = dict(zip(month,numbers))
print(dict_months)
