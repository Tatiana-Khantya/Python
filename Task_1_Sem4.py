# 1 Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.

# list1 = [int(s) for s in input('Введите набор чисел через пробел: ').split()]
# print(list1)
# mx = max(list1)
# mn = min(list1)
# print(f"{mx} {mn}")

stroka = '20 56 899 -14 6'
list1 = [int(s) for s in stroka.split()]
print(list1)
mx = max(list1)
mn = min(list1)
print(f"{mx} {mn}")