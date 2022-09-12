# 2 Найти максимальное из пяти чисел.
# list = []
# for i in range(5):
#     x = float(input('Enter number: '))
#     list.append(x)
# number = max(list)
# print (number)

# list1 = [1, 2, 3, 4, 5]
# max = list1[0]
# # for i in range(len(list1)):
# #    if list1[i] > max:
# #     max = list1[i]
# #     i = i+1
# # print (max)
# for i in list1:
#     if i > max:
#         max = i
# print (i)

# 3 Вывести на экран числа от -N до N.

# n = int(input('enter number: '))
# for i in range(-n, n+1):
#     print(i)

# 4 Показать первую цифру дробной части числа.

# a = float(input('enter number: '))
# a = int(a*10%10)
# print(a)

# 5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

# a = 75
# if a%30 != 0 and a% 15 == 0:
#     print('кратно 15 и не кратно 30')
# elif a%10 == 0 or a%5 == 0:
#     print('кратно 5 и 10')
# else:
#     print('wrong')

# a = int(input('Введите число '))
# if a % 30 == 0:
#     print('не ok')
# elif a % 5 == 0 and a % 10 == 0 or a % 15 == 0:
#     print('ok')
# else:
#     print('не ok')

# 6 Дано число обозначающее день недели. Вывести его название и
# указать является ли он выходным.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f'x = {x}, y = {y}, z = {z}')
#             print(not(x or y or z) == (not x and not y and not z))

# 1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N
# членов.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81

# n = int(input('Enter number: '))
# for i in range(n):
#     print((-3)**i)

#     2.Для натурального n создать список, состоящий из элементов последовательности 3n + 1
# Пример:
# - Для n = 6: [4, 7, 10, 13, 16, 19]

# n = int(input('Enter number: '))
# list = []
# for i in range(1, n+1):
#     list.append(3*i+1)
# print(list)

# 3.Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

# string_1 = input('Задайте первую строку: ')
# string_2 = input('Задайте вторую строку: ')
# count = 0
# for i in range(len(string_1)):
#     # print(string_1[i:i+len(string_2)])
#     if string_1[i:i+len(string_2)] == string_2:
#         count +=1
# print(count)

# 11 Пользователь вводит размеры трех комнат (длину и ширину).
# Необходимо вывести площадь каждой комнаты и общую площадь.

