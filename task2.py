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
            if game_field[posX] is not ' ':
                print('(!)Ячейка уже занята')
                continue
        except:
            print('(!)Недопустимое значение')
            continue
        x_player.append(posX)
        game_field[posX] = 'X'
        gameField(game_field)
        if checkWin(x_player, O_player):
            gameField(game_field)
            return
        while True:
            try:
                posO = int(input('Нулики введите позицию(от 1 до 9) '))
            except:
                print('(!)Недопустимое значение')
                continue
            if game_field[posO] is not ' ':
                print('(!)Ячейка уже занята')
                continue
            break
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