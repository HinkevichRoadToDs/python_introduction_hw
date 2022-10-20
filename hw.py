'''
task1
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл users_hobby.txt.
'''
# file_users = open('users.txt', 'r')
# users_lst = file_users.read().splitlines()
# file_users.close()
# print(users_lst)
#
# file_hobbies = open('hobbies.txt', 'r')
# hobbies_lst = file_hobbies.read().splitlines()
# file_hobbies.close()
# print(hobbies_lst)
# #1
# users_hobbies_dict = {}
# i = 0
# for user in users_lst:
#     users_hobbies_dict[user] = hobbies_lst[i]
#     i +=1
# print(users_hobbies_dict)
# #2
# # users_hobbies_dict1 = dict(zip(users_lst,hobbies_lst))
# # print(users_hobbies_dict1)
# with open('users_hobbies.txt','w') as fileUH:
#     for key,value in users_hobbies_dict.items():
#         fileUH.write(f'{key} : {value}\n')
'''
task2
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
# num = int(input('n = '))
# divider = 2
# multipliers_lst = []
# dict_1 = {}
# while divider <= num:
#     if num % divider == 0:
#         dict_1[int(num)] = divider
#         num /= divider
#         multipliers_lst.append(divider)
#     else:
#         divider +=1
# print(multipliers_lst)
# print(dict_1)
'''
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
'''
# from random import randint as rint
# num_lst = []
# for i in range(0,20):
#     num_lst.append(rint(0,50))
# print(f'список с рандомными значениями:\n{num_lst}')
# dict_repeats = {}
# for number in num_lst:
#     if number not in dict_repeats.keys():
#         dict_repeats[number] = 1
#     else:
#         dict_repeats[number] += 1
# print(f'словарь с подсчитаным количеством повторений для каждого элемента:\n{dict_repeats}')
# result_lst = []
# for key,value in dict_repeats.items():
#     if value == 1:
#         result_lst.append(key)
# print(f'список неповторяющихся элементов:\n{result_lst}')
'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
'''
# from random import uniform as uf
#
# k = int(input('Задайте натуральную степень k: '))
# lst_coef = []
# for i in range(0, k+1):
#     lst_coef.append(round(uf(0, 101), 2))
# print(f'коэффициенты: {lst_coef}')
# polynomial = ''
# i = 0
# while k >= 0:
#     if lst_coef[i] != 0 and k not in (1,0):
#         polynomial += str(lst_coef[i]) + '(x)^' + str(k) + ' + '
#     if k == 1:
#         polynomial += str(lst_coef[i]) + '(x)' + ' + '
#     if k == 0:
#         polynomial += str(lst_coef[i]) + ' = 0'
#     i += 1
#     k -= 1
# print(polynomial)
'''
task5 
'''
with open('poly.txt', 'r') as data:
    poly1 = data.readline()
    poly2 = data.readline()
poly1_lst = poly1.split('+')
poly2_lst = poly2.split('+')
def FindCoef(poly_lst):
    coef_lst = []
    for item in poly_lst:
        if 'x' in item:
            index = item.find('x')
            try:
                coef_lst.append(int(item[:index]))
            except:
                if item[:index] == '':
                    coef_lst.append(0)
        else:
            coef_lst.append(item)
    coef_lst = [int(c) for c in coef_lst]
    return coef_lst
coef1_lst = FindCoef(poly1_lst)
coef2_lst = FindCoef(poly2_lst)
new_coef_lst = []
for i in range(len(coef1_lst)):
    new_coef_lst.append(coef1_lst[i] + coef2_lst[i])
print(new_coef_lst)
#Допустим я знаю заранее, что самый большой показатель степени у х это 3
k = 3
new_poly = ''
i = 0
while k >= 0:
    if new_coef_lst[i] != 0 and k not in (1, 0):
        new_poly += str(new_coef_lst[i]) + 'x' + str(k) + ' + '
    if k == 1:
        new_poly += str(new_coef_lst[i]) + 'x' + ' + '
    if k == 0:
        new_poly += str(new_coef_lst[i])
    i += 1
    k -= 1
print(new_poly)
with open('new_poly.txt','w') as data:
    data.write(new_poly)