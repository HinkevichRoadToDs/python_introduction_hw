# homework
'''
task1
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
'''
# import random
# list_1 = []
# for item in range(0, 4):
#     list_1.append(random.randint(-100,100))
# print(list_1)
# sum_numbers = sum(list_1[1:: 2])
# print(sum_numbers)
'''
task2
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Хотелось закрепить как-то работу со срезами и методами списков, поэтому получилось так длинно
'''
# import random
# # заполнение списка рандомными значениями
# lst_length = int(input('Длина массива:'))
# list_1 = []
# for item in range(0, lst_length):
#     list_1.append(random.randint(-100, 100))
# print(list_1)
# lst_len_half = len(list_1) // 2
# # если длина - четное число
# if len(list_1) % 2 == 0:
#     list_left = list_1[0:lst_len_half]
#     list_right = list_1[lst_len_half::]
#     print(list_left, list_right)
#     list_result = []
#     list_right = list(reversed(list_right)) # list_right = list_right[:: -1]
#     for i in range(0, lst_len_half):
#         prod = list_left[i] * list_right[i]
#         list_result.append(prod)
#     print(list_result)
# # если длина нечетная, то элемент, которому не нашлась пара, добавляется просто в конец
# else:
#     list_left = list_1[0:lst_len_half]
#     list_right = list_1[(lst_len_half + 1)::]
#     middle_index = len(list_1) // 2
#     print(list_left, list_1[middle_index], list_right)
#     list_result = []
#     for i in range(0, lst_len_half):
#         prod = list_left[i] * list_right[-i-1]
#         list_result.append(prod)
#     list_result.append(list_1[middle_index])
#     print(list_result)
'''
task3
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.
'''
# import random
# # заполнение списка рандомными значениями
# lst_length = int(input('Длина массива:'))
# list_1 = []
# list_2 = []
# for item in range(0, lst_length):
#     list_1.append(random.uniform(-100, 100))
#     decimal_part = list_1[item] - int(list_1[item])
#     list_2.append(decimal_part)
# diff_max_min = max(list_2) - min(list_2)
# print(list_1)
# print(list_2)
# print(f'Разница между максимальным и минимальным значением дробной части элементов = {diff_max_min}')
'''
task4
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Там конечно нужно добавлять еще единицу к "обратному" коду, но я не смог это сделать
'''
# import functionIntoBinary as fun1
# number_input = int(input('Введите число: '))
# binary_number = fun1.binary(number_input)
# print(f'{number_input} в двоичной системе счисления : {binary_number}')
'''
task5
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
'''
# number_input = int(input('Введите число: '))
# def Fibonacci(n):
#     if n in(1, 2):
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# count = 1
# list_1 = []
# while count <= number_input:
#     list_1.append((-1) ** (count + 1) * Fibonacci(count))
#     count += 1
# list_1.reverse()
# list_1.append(0)
# count = 1
# while count <= number_input:
#     list_1.append(Fibonacci(count))
#     count += 1
# print(list_1)
