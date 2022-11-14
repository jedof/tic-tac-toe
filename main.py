import random

game_map = [['x', 'x', '0'],
            [' ', 'x', '0'],
            [' ', ' ', 'x']]

players = ('x', '0')


def choose_the_winner():
    for line in game_map:
        if len(set(line)) == 1 and line[0] in players:
            print(f"Строка. Победил {line[0]}")
            break
    for i in range(3):
        if len({game_map[j][i] for j in range(3)}) == 1 and game_map[0][i] in players:
            print(f"Столбец. Победил {game_map[0][i]}")
            break
    if game_map[1][1] in players:
        if len({game_map[0][0], game_map[1][1], game_map[2][2]}) == 1 or len({game_map[0][2], game_map[1][1], game_map[2][0]}) == 1:
            print(f"диагональ. Победил {game_map[1][1]}")
            
 
print(choose_the_winner())

# while True:
#     print('   0   1   2')
#     for index, line in enumerate(game_map):
#         print(index, end='  ')
#         print(*line, sep=' | ')
#         if index < 2:
#             print('  -----------')

#     user_raw, user_column = map(int, input().split())
#     game_map[user_raw][user_column] = 'x'
#     while True:
#         bot_raw = random.randint(0,2)
#         bot_column = random.randint(0,2)
#         if game_map[bot_raw][bot_column] == ' ':
#             game_map[bot_raw][bot_column] = '0'
#             break
#     choose_the_winner()
#     break