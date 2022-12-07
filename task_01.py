# 2) Морской бой.
import random
def print_arr(arr):
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()
def install_ships_player(ships_1, ships_2, max_coordinate):
    my_list_player = [[0 for i in range(max_coordinate)] for y in range(max_coordinate)]
    while ships_1 > 0:
        coordinate_1 = int(input('Введите точку Х: '))
        coordinate_2 = int(input('Введите точку У: '))
        if my_list_player[coordinate_1][coordinate_2] == 0:
            my_list_player[coordinate_1][coordinate_2] = 1
            ships_1 -= 1
    while ships_2 > 0:
        coordinate_1 = int(input('Введите точку Х: '))
        coordinate_2 = int(input('Введите точку У: '))
        if my_list_player[coordinate_1][coordinate_2] == 0:
            my_list_player[coordinate_1][coordinate_2] = 2
            my_list_player[coordinate_1][coordinate_2 + 1] = 2
            ships_2 -= 1
    return my_list_player


def install_ships_bot(ships_1, ships_2, max_coordinate):
    my_list_bot = [[0 for i in range(max_coordinate)] for y in range(max_coordinate)]
    while ships_1 > 0:
        coordinate_1 = random.randint(0, max_coordinate - 1)
        coordinate_2 = random.randint(0, max_coordinate - 1)
        if my_list_bot[coordinate_1][coordinate_2] == 0:
            my_list_bot[coordinate_1][coordinate_2] = 1
            ships_1 -= 1
    while ships_2 > 0:
        coordinate_1 = random.randint(0, max_coordinate - 1)
        coordinate_2 = random.randint(0, max_coordinate - 1)
        if my_list_bot [coordinate_1][coordinate_2] == 0:
            my_list_bot[coordinate_1][coordinate_2] = 2
            my_list_bot[coordinate_1][coordinate_2 + 1] = 2
            ships_2 -= 1
    return my_list_bot

def game_battle_ships(arr_bot, arr_player, ships_1, ships_2):
    ships_bot = ships_1 + ships_2 * 2
    ships_player = ships_1 + ships_2 * 2
    while ships_bot > 0 and ships_player > 0:
        print(ships_player, ships_bot)
        z = int(input('Введите координату Х: '))
        y = int(input('Введите координату Y: '))
        list_bum = []
        if z < len(arr_bot) and y < len(arr_bot):
            print(z, y)
            if arr_bot[z][y] == 1:
                arr_bot[z][y] = 'X'
                print('Вы уничтожили однопалубный корабль!')
                print(f'По координатам:[{z}, {y}]')
                ships_bot -= 1
            elif arr_bot[z][y] == 2:
                arr_bot[z][y] = 'X'
                print('Вы ранили двупалубный корабль!')
                ships_bot -= 1
            elif arr_bot[z][y] == 'M' or arr_bot[z][y] == 'X':
                print('Вы уже стреляли по данной точке!')
            elif arr_bot[z][y] == 0:
                arr_bot[z][y] = 'M'
                print('Вы промазали!')
        else:
            print('Такой кординаты не существует')
        z_1 = random.randint(0, int(len(arr_player )) -1)
        y_1 = random.randint(0, int(len(arr_player )) -1)
        if arr_player[z_1][y_1] == 1:
            arr_player[z_1][y_1] == 'X'
            ships_player -=1
            print('Вaм уничтожили однопалубный корабль!')
        elif arr_player[z_1][y_1] == 2:
            arr_player[z_1][y_1] == 'X'
            ships_player -= 1
            print('Вам ранили двупалубный корабль!')
        elif arr_player[z_1][y_1] == 'M' or arr_player[z_1][y_1] == 'X':
            print('Бот выстрелил повторно в точку')
        elif arr_player[z_1][y_1] == 0:
            arr_player[z_1][y_1] = 'M'
            print('Бот промазал')
        if ships_player == 0 or ships_bot == 0:
            if ships_player > ships_bot:
                print('Вы победили \n Ваше поле')
                print_arr(arr_player)
                print('Поле бота')
                print_arr(arr_bot)
            else:
                print('Вы проиграли\n Ваше поле')
                print_arr(arr_player)
                print('Поле бота')
                print_arr(arr_bot)



x = int(input('Какой размерности будет поле? '))
game_battle_ships(install_ships_bot(1, 1, x), install_ships_player(1,1,x), 1, 1)

