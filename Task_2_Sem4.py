# 2 Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения;
# 2) с помощью дополнительных библиотек Python.

a = int(input('Введите коэффициент a: '))
b = int(input('Введите коэффициент b: '))
c = int(input('Введите коэффициент c: '))
d = b**2 - 4*a*c
print(d)
if d < 0:
    result = 'действительных корней нет'
elif d == 0:
    result = f'уравнение имеет один корень: {-b/2*a}'
else:
    result = f'Корни уравнения : x1 = {(-b+d**0.5)/(2*a)}, x2 = {(-b-d**0.5)/(2*a)}'
print (result)

import math
if a == 0:
    result = 'действительных корней нет'
if a != 0:
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    result = f'Корни уравнения : x1 = {x1}, x2 = {x2}'
else:
    print(result)