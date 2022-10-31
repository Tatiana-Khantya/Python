# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
#  чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример: 1 2 3 5 6 7
# Вывод: 4

# with open("data.txt", "r") as file:
#     # print(file.readline())
#     list = list(map(int, (file.readline().split())))
#     print(list)
#     find_num = list[0]
#     for i in range(1, len(list)):
#         if list[i] - list[i-1] != 1:
#             print(list[i]-1)
#             break

# ......

# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Привет Приабвет приабев приветабв
# Вывод: Привет приабев
with open("data2.txt", "r", encoding='utf_8') as file:
    list = list(file.readline().split())
    stop_list = 'абв'
    filtered_list = ' '.join(filter(lambda x: stop_list not in x, list))
    print('Фильтр: ', filtered_list)

substr = 'абв'

with open('02.txt', 'r', encoding='utf-8') as f:
    for word in f.read().split():
        if word.find(substr) == -1:
            print(word, end=' ')    
