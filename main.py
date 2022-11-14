import random

game_map = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]


def choose_the_winner():
    for line 
    for i in range(3):
        if all(game_map[j][i] == 'x' for j in range(3)):
            result = True
    return result

print(choose_the_winner)
 
while True:
    print('   0   1   2')
    for index, line in enumerate(game_map):
        print(index, end='  ')
        print(*line, sep=' | ')
        if index < 2:
            print('  -----------')

    user_raw, user_column = map(int, input().split())
    game_map[user_raw][user_column] = 'x'
    while True:
        bot_raw = random.randint(0,2)
        bot_column = random.randint(0,2)
        if game_map[bot_raw][bot_column] == ' ':
            game_map[bot_raw][bot_column] = '0'
            break
            