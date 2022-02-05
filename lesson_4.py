# for number in [0, 1, 2, 3, 4]:
#     print(number)
#
# # ==================================
#
for num in range(5):
    print(num)
else:
    print("Числа закончились")

# ==================================
# for num in range(5):
#     if num ==3:
#         break
#     else:
#         print(num)
# else:
#     print("Числа закончились")
# # ==================================

for num in range(5):
    if num == 3:
        continue
    else:
        print(num)
else:
    print("Числа закончились")

# ====================================
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Конец")
# # ====================================
i = 0
while i < 5:
    if i == 3:
        break
    else:
        print(i)
        i += 1
else:
    print("Конец")
# # ====================================
# i = 0
# while i < 5:
#     if i == 3:
#         continue
#     else:
#         print(i)
#         i += 1
# else:
#     print("Конец")
