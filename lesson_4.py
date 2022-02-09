# mylist = ['apple', 'banana', 'cherry', 1, 2, 3, 4, 5,
#           {'a': 1, 'b': 1, 'c': 1, 'd': 1}]
# print(len(mylist))
#
# string = 'Hello'
# print(len(string))
#
# d = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
# key= list(d.keys())
# values = list(d.values())
# print(len(d))
#
# mystr = "Привет Python!"
# underline = '-' * len(mystr)
# print(f'{underline}\n{mystr}\n{underline}')

#
# new_list = [0, 1, 2, 3, 4]
# print(type(new_list))
# for number in new_list:
#     print(number)
#
# # ==================================
#

# import random, time
# print(time.time())
# time.sleep(5)
# print(time.time())
# print(random.randrange(3, 9))
# print(list(range(100,1, -1)))

# for num in range(0,100,20):
# # for num in range(0,5,1):==>range(5)
# for num in range(10):
#     print(num)
# else:
#     print("Числа закончились")

# ==================================
# for num in range(5):
#     if num == 3:
#         print(num)
#         break
#     else:
#         print(num)
# else:
#     print("Числа закончились")

# # ==================================
#
# for num in range(5):
#     if num == 3:
#         continue
#     else:
#         print(num)
# else:
#     print("Числа закончились")

# ====================================
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("Конец")
# # ====================================
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     else:
#         print(i)
#         i += 1
# else:
#     print("Конец")
# # ====================================
# i = 0
# while i < 5:
#     if i == 3:
#         i += 1
#         continue
#
#     else:
#         print(i)
#         i += 1
# else:
#     print("Конец")

import time
import random

end_time = time.time() + 20

while time.time() < end_time:
    print(random.randint(0, 10))
    time.sleep(5)
else:
    print("Alarm")
#
# def generator(rang):
#     for num in range(rang):
#         yield num
#
#
# generator(10)
# """
# This is program written for finding the max power of two, which will be no more than given number
# """
#
# N = int(input('Choose your number: '))
# n = 1
# pow = 0
#
# while N >= n:
#     n *= 2
#     pow +=1
# else:
#     print(int(n/2), 'is the max power of 2, which is no more than your number. It is 2 in the power of', (pow-1))

