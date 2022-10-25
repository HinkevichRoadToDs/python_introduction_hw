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
from random import randint


def inGame(bank, list_1):
    while bank > 0:
        take = int(input(f' Остаток : {bank}, Сколько ты берешь? '))
        bank -= take
        list_1.append(take)
        if bank == 0:
            print('Ты забрал последние конфеты, Барли проиграл.')
            break
        if bank <= 28:
            print(f'Барли берет последние {bank} конфет и выигрывает, ты проиграл')
            break
        if bank >= 30 and bank <= 57:
            temp = bank - 29
            bot_take = temp
            print('Барли: ты попал в ловушку Джокера\n'
                  '────┌┴┴┐────\n'
                  '▀▀█═╡▀▀╞═█▀▀\n'
                  '────└╥╥┘────\n'
                  '─────╝╚─────\n')
        else:
            bot_take = randint(1, 28)
        print(f'Барли берет {bot_take} конфет(ы)')
        bank -= bot_take
        list_1.append(f'Барли:{bot_take}')
    print(f' журнал сражения:{list(enumerate(list_1))}')


def toss():
    toss_var = randint(0, 1)
    bank = 200
    print('Привет, я робот Барли, давай начнем игру.')
    list_1 = []
    if toss_var:

        bot_take = randint(1, 28)
        print(f'я хожу первым, беру {bot_take} конфет(ы)')
        bank -= bot_take
        list_1.append(f'Барли:{bot_take}')
        inGame(bank, list_1)
    else:
        print('ходи первым')
        take = int(input('Сколько ты берешь(не больше 28)? '))
        bank -= take
        list_1.append(take)
        bot_take = randint(1, 28)
        bank -= bot_take
        list_1.append(f'Барли:{bot_take}')
        print(f'Барли берет {bot_take} конфет')
        inGame(bank, list_1)
toss()