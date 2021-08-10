'''This is a python script for 2 player tic-tac-toe game !!'''
import sys
def replay():
    '''This function is used to ask user
    if he/she wants to play again or not'''
    user_in_re = ''
    while user_in_re.lower() not in ['y', 'n']:
        user_in_re = input('Do you want to play the game again ? (y/n)\n')
    return user_in_re.lower() == 'y'

def is_draw(metrix):
    '''This function checks
    if the match has been drawn'''
    draw_set = ['O', 'X']
    row1 = list(map(str, metrix[0]))
    row2 = list(map(str, metrix[1]))
    row3 = list(map(str, metrix[2]))
    return sorted(set(row1)) == sorted(set(row2)) and \
            sorted(set(row2)) == sorted(set(row3)) and \
            sorted(set(row3)) == draw_set

def replace_by_empty(row):
    '''This function replaces the digits in matrix with empty strings
    which is to be used in display() function.'''
    new_str=''
    for i in ','.join(map(str,row)):
        if i.isdigit():
            new_str+=' '
        else:
            new_str+=i
    return new_str.split(',')

def display(metrix):
    '''This function display the updated board to the user.'''
    row1 = replace_by_empty(metrix[0])
    row2 = replace_by_empty(metrix[1])
    row3 = replace_by_empty(metrix[2])
    print(' {} | {} | {} '.format(row1[0], row1[1], row1[2]))
    print('---|---|---')
    print(' {} | {} | {} '.format(row2[0], row2[1], row2[2]))
    print('---|---|---')
    print(' {} | {} | {} '.format(row3[0], row3[1], row3[2]))

def horizontal_check(row):
    '''Row check: if any user has won'''
    if set(row) == {'X'} or set(row) == {'O'}:
        return True
    return False

def vertical_check(row1,row2,row3):
    '''Column check: if any user has won'''
    for i in range(3):
        if row1[i] == row2[i] == row3[i]:
            return True
    return False

def diagnol_check(row1,row2,row3):
    '''Diagnol check: if any user has won'''
    if row1[0]==row2[1]==row3[2] or row1[2]==row2[1]==row3[0]:
        return True
    return False

def check_rules(metrix):
    '''This function checks for all the rules defined above'''
    if is_draw(metrix):
        return 'draw'
    if horizontal_check(metrix[0]) or horizontal_check(metrix[1]) or horizontal_check(metrix[2]):
        return 'won'
    if vertical_check(metrix[0],metrix[1],metrix[2]):
        return 'won'
    if diagnol_check(metrix[0],metrix[1],metrix[2]):
        return 'won'
    return ''

def get_user_input(player_name,metrix):
    '''This function takes the input from the user
    which is to be inserted into the board.'''
    num = '0'
    number_li = list(map(str,range(1,10)))
    while num not in number_li:
        display(metrix)
        num = input(f'{player_name}, please choose your number. (1-9)\n')
        if num.lower() == 'bye':
            sys.exit()
        if num not in number_li:
            print('Sorry, this is not a valid number.')
    return int(num)

def  replace_index(row,player,num):
    '''This function replaces the digit in the board
    with the input (X or O) taken from the user'''
    i = row.index(num)
    row.remove(num)
    row.insert(i,player[1])

def set_pointer(player,num,metrix):
    '''This function calls the replace_index functions internally
    to replace the digits in the board
    and then calls check_rules function to check
    if the match has been drawn or any user has won.'''
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
    if result.lower() == 'draw':
        print('The game has ended in a draw...!!!')
        display(metrix)
        if replay():
            start_game()
        return True
    return False


def start_game():
    '''This function act as the starting point of the game.
    It creates a new board which is displayed, asks the player names from the users
    and then initiate the game by asking for the input from first player'''
    metrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print('Welcome to TIC TAC TOE !!!')
    player_details = dict()
    player_details['first_player'] = [input('Please enter the name of Player 1:\n'), 'X']
    player_details['second_player'] = [input('Please enter the name of Player 2:\n'), 'O']
    print(f'{player_details["first_player"][0]}, you would use "X"\n' \
          f'{player_details["second_player"][0]}, you would use "O"\n')
    flag = True
    stop = False
    while not stop:
        if flag:
            num = get_user_input(player_details['first_player'][0],metrix)
            flag = False
            stop = set_pointer(player_details['first_player'],num,metrix)
        else:
            num = get_user_input(player_details['second_player'][0],metrix)
            flag = True
            stop = set_pointer(player_details['second_player'],num,metrix)


if __name__ == '__main__':
    PLAY = ''
    while PLAY.lower() not in ['y','n']:
        PLAY = input('Do you want to play (y/n)\n')
    if PLAY.lower() == 'y':
        start_game()
    else:
        sys.exit()
    print('Bye !!')
