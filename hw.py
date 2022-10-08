#task1
# numberDay = int(input('введите день недели'))
# if numberDay == 6 or numberDay == 7:
#     print('этот день - выходной')
# else:
#     print('это будний день')

#task2
# def checkExpression():
#     xyz = ['X','Y','Z']
#     xyz_list = []
#     for i in range(3):
#             xyz_list.append(input(f'введите {xyz[i]}: '))
#     print(xyz_list)

#     leftExp = not (xyz_list[0] or xyz_list[1] or xyz_list[2])
#     rightExp = not xyz_list[0] and not xyz_list[1] and not xyz_list[2]
#     result = leftExp == rightExp
#     return result
# result1 = checkExpression()
# if result1 == True:
#     print('выражение истинно')
# else:
#     print('выражение ложно')

#task3 
# number_x = float(input('x: '))
# number_y = float(input('y: '))
# if number_x != 0 or number_y != 0:
#     if number_x != 0 and number_y == 0:
#         print('точка лежит на оси абцисс')
#     elif number_x == 0 and number_y != 0:
#         print('точка лежит на оси ординат')
#     elif number_x > 0 and number_y > 0:
#         print('1-ая четверть')
#     elif number_x < 0 and number_y > 0:
#         print('2-ая четверть')
#     elif number_x < 0 and number_y < 0:
#         print('3-ая четверть')
#     elif number_x > 0 and number_y < 0:
#         print('4-ая четверть')
# else:
#     print('точка находится в центре координат')

#task4
# import math
# A_x,A_y = float(input('A(x): ')),float(input('A(y): '))
# B_x,B_y = float(input('B(x): ')),float(input('B(y): '))

# distance = round(math.sqrt((A_x - B_x)**2 + (A_y - B_y)**2),3)
# print(f'расстояние между A и B: {distance}')