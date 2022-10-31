# 3 Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.


a = int(input('Укажите 1-е число : '))
b = int(input('Укажите 2-е число : '))

if b > a:
    a, b = b, a
for i in range(1, b):
    if (a * (i))%a == 0 and (a * (i))%b == 0:
        print(i)
        break
print(f' {a} {i} = {a * (i)}')


n = 12
flag = False
for i in range(2, n):
    if n % i == 0:
        flag = True
        break
if flag:
    print(f'число {n} не простое')
else:
    print(f'число {n} простое')

# import math
# a = int(input('Укажите 1-е число : '))
# b = int(input('Укажите 2-е число : '))
# print(math.lcm(a, b))
# print(math.gcd(a, b))
# print(a*b/math.gcd(a, b))