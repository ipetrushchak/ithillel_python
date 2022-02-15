# Создание списка

# s = []  # Пустой список
# l = ['s', 'p', ['isok'], 2, (1,1,1), {"id":1}]
#
# # print(s)
# print(type(l))

# #
# my_list2 = ['один', 'два', 'три', 'четыре', 'пять']
# my_list1 = [1, 2, 3, 4, 5]
# # print([1])

# print(my_list2)
# # ================================
# my_list3 = ['один', 10, 2.25, [5, 15], 'пять']
# tretii_elemnt = my_list3[4] #
# #
# print(my_list3[3][1])
# print(third_elem)
# # =================== Срез списка
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# print(my_list[1:3])
# print(my_list[1:])
# print(my_list[:3])
# print(my_list[::-1])
# my_list[1:3] = ['Привет',  'Мир'] # Поскольку списки изменяемые, менять элементы можно с помощью оператора среза:
# print(my_list)
# ========== Вставить в список
# my_list = [1, 2, 3, 4, 5]
# my_list.insert(5, 'Привет')
# print(my_list)
# ========================= Добавить в список
# my_list = ['один', 'два', 'три', 'четыре', 'пять', "арбуз"]
# # my_list.append('ещё один')
# # print(my_list)
#
# # c = [i * 3 for i in "list"]
#
#
# # c = [i * 3 for i in 'list' if i != 'l' and i != 'i']
# # print(c)
# # compl = [c + d for c in 'list'
# #          if c != 'i'
# #             for d in 'spam'
# #                 if d != 'a']
# # print(compl)
# # ==================================== Sort
# # prices = [159.54, 37.13, 71.17, 12.5, 1.36]
# # prices.sort(reverse=True)
# # print(prices)
# list_2 = [3, 5, 2, 4, 1]
# list_2.sort()
# my_list.sort()
# print(my_list)
# ============= Перевернуть список
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()  # Перевернутое значение
# print(my_list)
# ============= Индекс элемента
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# print(my_list[3])
# # print(my_list.index('четыре'))
# for i in my_list:
#     print(my_list.index(i))
# ==========Удалить элемент
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# removed = my_list.pop(2)
# removed2 = my_list.pop(my_list.index('четыре'))
# print(my_list)
# print(removed, removed2)
#
# my_list.insert(2, 'три')
# my_list.insert(3, 'четыре')
# print(my_list)
# # ================ или Del
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# del my_list[2]
# print(my_list)

# my_list = ['один', 'два', 'три', 'четыре', 'пять', 'четырнадцать']
# # del my_list[1:3]
# del my_list[0]
# print(my_list)
# print(max(my_list))
# # =========== Функции агрегации
# my_list = [5, 3, 2, 4, 1.1]
# # print(len(my_list))
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list)) # sum() работает только с числовыми значениями.
# max(), len() и другие можно использовать и со строками.
# =============Сравнить списки
# my_list1 = ['один', 'два', 'три', 'четыре', 'пять']
# my_list2 = ['один', 'два', 'три', 'четыре', 'пять']
# list_2 = ['три', 'один', 'пять', 'два', 'четыре']
# print(my_list1 == my_list2)
# print(my_list1 == list_2)
# ===================Математические операции на списках
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# print(list_1 + list_2)
# new_list = [x in range len(list_1) list_1[x] + list_2[x]]
# print(new_list)
#
# list_1 = [1, 2, 3]
# print(list_1  *  2)

# =============Списки и строки
# my_str = 'Monty Python'
# my_list = list(my_str)
# print(str(my_list))
#
# my_list = my_str.split()
# print(my_list)
# ================== Объединить список в строку
# my_list = ['Monty', 'Python']
# delimiter = ''
# output = delimiter.join(my_list)
# print(output)
# print("".join(my_list))
# =================== Алиасинг (псевдонимы) Alias
# my_list = ['Monty', 'Python']
# list_2 = my_list
# # list_2[1] = 'Java:)'
# print(my_list)
# print(list_2)

# # ================ Генерация Списка List generation
# c = [c * 3 for c in 'list']
# print(c)

# # ============================= List Comprehantion
# print([x*x for x in range(10)])
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# print([list_1[x]+list_2[x] for x in list_1])
# # =============================== map
# list_of_words = ['one', 'two', 'list', '', 'dict']
# list_of_words = ['ONE', 'TWO', 'LIST', '', 'DICT']
# map(str.upper, list_of_words)
# map(str.lower, list_of_words)
# print(list(map(str.lower, list_of_words)))
# # --------------------------------- Конвертация в числа:
# list_of_str = ['1', '2', '5', '10']
# int_list=list(map(int, list_of_str))
# print(sum(int_list))
# # ======================== List comprehension вместо map
# print([word.upper() for word in list_of_words])
# print(sum([int(x) for x in list_of_str]))

# # =================== Форматирование строк
# vlans = [100, 110, 150, 200, 201, 202]
# print([f'vlan {x}' for x in vlans])
# # ============ Для получения пар элементов используется zip:
# nums = [1, 2, 3, 4, 5]
# nums2 = [100, 200, 300, 400, 500]
# print([x * y for x, y in zip(nums, nums2)])
# # =============
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print([x+y for x, y in zip(list_1,list_2)])
# # =========== zip и кортежи
# a = [1, 2, 3]
# b = [100, 200, 300]
# print(list(zip(a, b)))
# # =========== Использование zip для создания словаря
# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']
# print(dict(zip(d_keys, d_values)))
#
# # ========= Tuples
# list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
# tuple_keys = tuple(list_keys)
# tuple_list = list(tuple_keys)
# print((tuple_keys))
# print(tuple_list)
# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
# print(a.__sizeof__())
# print(b.__sizeof__())

# ==========
# tuple_keys[1] = 'test' # кортеж неизменяем, присвоить новое значение нельзя
# =========== Поменять местами переменными
# a = 2
# b = 3
# a, b, c, d = 2, 3, 4, 5
# a = "Орел"
# b = "Решка"
# a, b = b, a
# temp = a
# a = b
# b = temp

# print(a)
# print(b)

# # ================== Sorted
tuple_keys = ('hostname', 'location', 'vendor', 'model', 'ios', 'ip', 'location', 'location')
print(sorted(tuple_keys), type(sorted(tuple_keys)))
print(max(tuple_keys))
print(min(tuple_keys))
print(tuple_keys.count('location'))

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(min(t))
# my_list = [5, 3, 2, 4, 1.1]
print(len(t))
print(min(t))
print(max(t))
print(sum(t)) # sum() работает только с числовыми значениями.
# max(), len() и другие можно использовать и со строками.