
n1 = 321
n2 = 0
while n1 > 0:
    Number = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10 + Number
print(n2)

