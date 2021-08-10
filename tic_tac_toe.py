import sys
from IPython.display import clear_output
def replay():
    replay=''
    while replay.lower() not in ['y', 'n']:
        replay = input('Do you want to play the game again ? (y/n)\n')
    return replay.lower() == 'y'

def is_draw(metrix):
    draw_set = ['O', 'X']
    row1 = list(map(str, metrix[0]))
    row2 = list(map(str, metrix[1]))
    row3 = list(map(str, metrix[2]))
    if sorted(set(row1)) == sorted(set(row2)) and sorted(set(row2)) == sorted(set(row3)) and sorted(set(row3)) == draw_set:
        return True

def replace_by_empty(row):
    new_str=''
    for i in ','.join(map(str,row)):
        if i.isdigit():
            new_str+=' '
        else:
            new_str+=i
    return new_str.split(',')

def display(metrix):
    row1 = replace_by_empty(metrix[0])
    row2 = replace_by_empty(metrix[1])
    row3 = replace_by_empty(metrix[2])
    print(' {} | {} | {} '.format(row1[0], row1[1], row1[2]))
    print('---|---|---')
    print(' {} | {} | {} '.format(row2[0], row2[1], row2[2]))
    print('---|---|---')
    print(' {} | {} | {} '.format(row3[0], row3[1], row3[2]))

def horizontal_check(row):
    if set(row) == {'X'} or set(row) == {'O'}:
        return True

def vertical_check(row1,row2,row3):
    for i in range(3):
        if row1[i] == row2[i] == row3[i]:
            return True

def diagnol_check(row1,row2,row3):
    if row1[0]==row2[1]==row3[2] or row1[2]==row2[1]==row3[0]:
        return True

def check_rules(metrix):
    if is_draw(metrix):
        return 'draw'
    elif horizontal_check(metrix[0]) or horizontal_check(metrix[1]) or horizontal_check(metrix[2]):
        return 'won'
    elif vertical_check(metrix[0],metrix[1],metrix[2]):
        return 'won'
    elif diagnol_check(metrix[0],metrix[1],metrix[2]):
        return 'won'
    else:
        return ''

def get_user_input(player_name,metrix):
    num = '0'
    li = list(map(str,range(1,10)))
    while num not in li:
        display(metrix)
        num = input(f'{player_name}, please choose your number. (1-9)\n')
        if num.lower() == 'bye':
            sys.exit()
        if num not in li:
            print(f'Sorry, this is not a valid number.')
    return int(num)

def  replace_index(row,player,num):
    i = row.index(num)
    row.remove(num)
    row.insert(i,player[1])

def set_pointer(player,num,metrix):
    if num in metrix[0]:
        replace_index(metrix[0],player,num)
    elif num in metrix[1]:
        replace_index(metrix[1], player, num)
    elif num in metrix[2]:
        replace_index(metrix[2], player, num)
    result = check_rules(metrix)

    if result.lower() == 'won':
        print(f'Congratulations {player[0]} !!, you won\n')
        display(metrix)
        if replay():
            start_game()
            return True
        else:
            return True
    elif result.lower() == 'draw':
        print(f'The game has ended in a draw...!!!')
        display(metrix)
        if replay():
            start_game()
            return True
        else:
            return True


def start_game():
    metrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print('Welcome to TIC TAC TOE !!!')
    d = dict()
    d['first_player'] = [input('Please enter the name of Player 1:\n'), 'X']
    d['second_player'] = [input('Please enter the name of Player 2:\n'), 'O']
    print(f'{d["first_player"][0]}, you would use "X"\n' \
          f'{d["second_player"][0]}, you would use "O"\n')
    flag = True
    stop = False
    while not stop:
        if flag == True:
            num = get_user_input(d['first_player'][0],metrix)
            flag = False
            stop = set_pointer(d['first_player'],num,metrix)
        else:
            num = get_user_input(d['second_player'][0],metrix)
            flag = True
            stop = set_pointer(d['second_player'],num,metrix)


if __name__ == '__main__':
    play = ''
    while play.lower() not in ['y','n']:
        play = input('Do you want to play (y/n)\n')
    if play.lower() == 'y':
        start_game()
    else:
       sys.exit()
    print('Bye !!')

