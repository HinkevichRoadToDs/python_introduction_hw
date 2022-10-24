# homework
'''
На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно
взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) * Подумайте как наделить бота ""интеллектом""
ситуация - 29 конфет: игрок, оказавшийся в этой ситуации априори проигрывает,
так как у него есть вариант взять от 1 до 28 конфет и в итоге все равно не возьмет последним
'''
# from random import randint
#
#
# def inGame(bank, list_1):
#     while bank > 0:
#         take = int(input(f' Остаток : {bank}, Сколько ты берешь? '))
#         bank -= take
#         list_1.append(take)
#         if bank == 0:
#             print('Ты забрал последние конфеты, Барли проиграл.')
#             break
#         if bank <= 28:
#             print(f'Барли берет последние {bank} конфет и выигрывает, ты проиграл')
#             break
#         if bank >= 30 and bank <= 57:
#             temp = bank - 29
#             bot_take = temp
#             print('Барли: ты попал в ловушку Джокера\n'
#                   '────┌┴┴┐────\n'
#                   '▀▀█═╡▀▀╞═█▀▀\n'
#                   '────└╥╥┘────\n'
#                   '─────╝╚─────\n')
#         else:
#             bot_take = randint(1, 28)
#         print(f'Барли берет {bot_take} конфет(ы)')
#         bank -= bot_take
#         list_1.append(f'Барли:{bot_take}')
#     print(f' журнал сражения:{list(enumerate(list_1))}')
#
#
# def toss():
#     toss_var = randint(0, 1)
#     bank = 200
#     print('Привет, я робот Барли, давай начнем игру.')
#     list_1 = []
#     if toss_var:
#
#         bot_take = randint(1, 28)
#         print(f'я хожу первым, беру {bot_take} конфет(ы)')
#         bank -= bot_take
#         list_1.append(f'Барли:{bot_take}')
#         inGame(bank, list_1)
#     else:
#         print('ходи первым')
#         take = int(input('Сколько ты берешь(не больше 28)? '))
#         bank -= take
#         list_1.append(take)
#         bot_take = randint(1, 28)
#         bank -= bot_take
#         list_1.append(f'Барли:{bot_take}')
#         print(f'Барли берет {bot_take} конфет')
#         inGame(bank, list_1)
# toss()
'''
Создайте программу для игры в ""Крестики-нолики"".
'''
from random import randint

game_field = {1: ' ', 2: ' ', 3: ' ',
              4: ' ', 5: ' ', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}
def TicTacToeGame():
    toss = randint(0, 1)
    gameField(game_field)
    if toss:
        print('Первый ход за Крестиками')
        O_player = []
        inGame(game_field, O_player)
    else:
        print('Первый ход за Нуликами')
        O_player = []
        while True:
            try:
                pos = int(input('Нулики введите позицию(от 1 до 9) '))
                break
            except:
                print('(!)Недопустимое значение')
                continue
        O_player.append(pos)
        game_field[pos] = 'O'
        inGame(game_field, O_player)

def checkWin(x_player, O_player):
    win_positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in win_positions:
        if all(j in x_player for j in i):
            print('X победили')
            return True
    for i in win_positions:
        if all(j in O_player for j in i):
            print('О победили')
            return True
    if len(x_player) + len(O_player) == 9:
        print('Ничья, игра закончена')
        return True

def inGame(game_field, O_player):
    x_player = []
    while True:
        gameField(game_field)
        try:
            posX = int(input('Крестики введите позицию(от 1 до 9) '))
        except:
            print('(!)Недопустимое значение')
            continue
        if game_field[posX] is not ' ':
            print('(!)Ячейка уже занята')
            continue
        x_player.append(posX)
        game_field[posX] = 'X'
        gameField(game_field)
        if checkWin(x_player, O_player):
            gameField(game_field)
            return
        try:
            posO = int(input('Нулики введите позицию(от 1 до 9) '))
        except:
            print('(!)Недопустимое значение')
            continue
        if game_field[posO] is not ' ':
            print('(!)Ячейка уже занята')
            continue
        O_player.append(posO)
        game_field[posO] = 'O'
        if checkWin(x_player, O_player):
            gameField(game_field)
            return
def gameField(game_field):
    print(f'Игровое поле:\n[{game_field[1]}]__[{game_field[2]}]__[{game_field[3]}]\n'
          f'[{game_field[4]}]__[{game_field[5]}]__[{game_field[6]}]\n'
          f'[{game_field[7]}]__[{game_field[8]}]__[{game_field[9]}]\n')

TicTacToeGame()
