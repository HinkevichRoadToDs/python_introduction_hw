'''
task1
'''
# def DeleteDecimalPart(number : str) -> int:
#     int_part = 0
#     float_number = float(number)
#     if float_number < 0:
#         float_number *= -1
#     if float_number < 10:
#         int_part = 1
#     elif float_number < 100:
#         int_part = 2
#     elif float_number < 1000:   
#         int_part = 3
#     elif float_number < 10000:   
#         int_part = 4
#     elif float_number < 100000:   
#         int_part = 5 
#     numb_length = 0
#     numb_length = len(number)-1 - int_part
#     count = 0
#     while count < numb_length:
#         float_number *=10
#         count += 1
#     return int(float_number)
# string_number = input("введите вещественное число ")
# if string_number.count('.') == 1:
#     new_int_number = DeleteDecimalPart(string_number)
#     print(new_int_number)
#     sum_digits = 0
#     while 1 < new_int_number:
#         sum_digits += new_int_number % 10
#         new_int_number //= 10
#         if new_int_number == 1:
#            sum_digits +=1
#            break 
#     print(sum_digits)
# else:
#     intsum_digits = 0
#     for n in string_number:
#         intsum_digits += int(n)
#     print(intsum_digits)
# print(DeleteDecimalPart('122.55555'))
'''
task2
'''
# number = int(input("введите число N "))
# dict_1 = {}
# temp = 1
# for i in range(1,number+1):
#     temp *= i
#     dict_1[i] = temp
# print(dict_1)
'''
task3
'''
# number = int(input("введите число N "))
# dict_1 = {}
# for i in range(1,number+1):
#     dict_1[i] = round((1+1/i) ** i,2)
# print(dict_1)
'''
task4
'''
import random
number = int(input("введите число N "))
list_1 = []
for i in range(0,number):
    list_1.append(random.randint(-number,number)) 
print(list_1)

count = 0
print(f'Сейчас вы будете вводить позиции нужных вам элементов,\nразмер списка равен {number},не выходите за рамки размера списка,\nкак только вы закончите, введите точку(.): ')
prod = 1
while count < 100:
    pos = input()
    if pos == '.':
        print(f'произведение = {prod}')
        break
    pos = int(pos)
    if pos < 0:
        pos *=-1
    if pos > number-1:
        print(f'вы вышли за рамки списка, позиция равна {number-1}')
        pos = number-1
    print(f'на позиции с индексом {pos} находится: {list_1[pos]}')
    prod *= list_1[pos]
    print(f'текущее произведение = {prod}')