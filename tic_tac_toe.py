import os
import shutil

class Player:

    bad_move1 = "Bad move... please re-read instructions..."
    bad_move2 = "Stop making bad moves or I will quit..."
    bad_move3 = "that's it i'm out of here \nbye"
    warnings = [bad_move1, bad_move2, bad_move3]
    victory_sets = [{1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7}]

    def __init__(self, name):
        self.name = name
        self.list_moves = []
        self.invalid_moves = []

    def validity_check(self, move, game_b):
        if move not in range(1, 10) or game_b[move - 1] != ' ':
            self.invalid_moves.append(move)
            print(Player.warnings[len(self.invalid_moves)-1])
            if len(self.invalid_moves) == 3:
                quit()
        else:
            return True

    def check_end(self, game_b):
        for st in Player.victory_sets:
            if st.issubset(self.list_moves):
                print(center_text("", terminal_width, fill_char='#'), end='')
                print (center_text(f'{self.name} wins!!!!!!', terminal_width, fill_char='#'), end='')
                print(center_text("", terminal_width, fill_char='#'))
                return True
        if ' ' not in game_b:
            print(center_text("it's a tie...", terminal_width, fill_char=' '))
            return True

terminal_width, _ = shutil.get_terminal_size()

def center_text(text, width, fill_char=' '):
    left_padding = (width - len(text)) // 2
    centered_text = text.center(width, fill_char)
    return centered_text

def another_game():
    print(center_text(f"Press 'Enter' for another game between {player_1.name} and {player_2.name}, type anything else to exit the program", terminal_width, fill_char=' '))
    if input() == '':
        return True

def update_game_board(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9):
    print(center_text(f'[{pos1}] [{pos2}] [{pos3}]',terminal_width, fill_char='.'))
    print(center_text(f'[{pos4}] [{pos5}] [{pos6}]', terminal_width, fill_char='.'))
    print(center_text(f'[{pos7}] [{pos8}] [{pos9}]', terminal_width, fill_char='.'))

init_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print(center_text('Tic-Tac-Toe...', terminal_width, fill_char=' '))
#print(center_text('Welcome to this masterpiece of a game...', terminal_width, fill_char=' '))
print(center_text('Player 1 will start by selecting a number according to the board below', terminal_width, fill_char=' '))
print(center_text('It is then time for Player 2 to pick', terminal_width, fill_char=' '))

update_game_board(*init_b)

name_1 = input(center_text("Player 1 name:", terminal_width, fill_char=' '))
player_1 = Player(name_1)
name_2 = input(center_text("Player 2 name:", terminal_width, fill_char=' '))
player_2 = Player(name_2)

print(center_text(f'Board is ready for {player_1.name} vs. {player_2.name}', terminal_width, fill_char=' '))
update_game_board(*game_b)

while True:

    while True:
        move_p1 = input(center_text(f"{player_1.name}, what is your move: ", terminal_width, fill_char=' '))
        try:
            move_p1 = int(move_p1)
        except:
            print(center_text(f'{player_1.name}... please re-read the rules and try again', terminal_width, fill_char='#'))
            continue
        if player_1.validity_check(move_p1, game_b):
            break

    player_1.list_moves.append(move_p1)
    game_b[move_p1-1] = 'X'
    update_game_board(*game_b)
    if player_1.check_end(game_b):
        if another_game():
            game_b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            player_1.list_moves = []
            player_2.list_moves = []
            update_game_board(*game_b)
            continue
        else:
            break

    while True:
        move_p2 = input(center_text(f"{player_2.name}, what is your move: ", terminal_width, fill_char=' '))
        try:
            move_p2 = int(move_p2)
        except:
            print(center_text(f'{player_1.name}please re-read the rules and try again', terminal_width, fill_char='#'))
            continue
        if player_2.validity_check(move_p2, game_b):
            break

    player_2.list_moves.append(move_p2)
    game_b[move_p2-1] = 'O'
    update_game_board(*game_b)
    if player_2.check_end(game_b):
        if another_game():
            game_b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            player_1.list_moves = []
            player_2.list_moves = []
            update_game_board(*game_b)
            continue
        else:
            break

print(center_text("End of game", terminal_width, fill_char=' '))

