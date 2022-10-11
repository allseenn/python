# 3. Создайте программу для игры в "Крестики-нолики".
import random
import os
# Function check winner after every turn
def winner_check(board):
    winner = ""
    # check rows
    if board[0] == board[1] == board[2]: winner = board[0]
    elif board[3] == board[4] == board[5]: winner = board[3]
    elif board[6] == board[7] == board[8]: winner = board[6]
    # check columns
    if board[0] == board[3] == board[6]: winner = board[0]
    elif board[1] == board[4] == board[7]: winner = board[1]
    elif board[2] == board[5] == board[8]: winner = board[2]
    # check diagonals
    if board[0] == board[4] == board[8]: winner = board[0]
    elif board[2] == board[4] == board[6]: winner = board[2]
    return winner
# Function checks man turn
def man_turn(board):
    clean_list = ([x for x in board if x.isdigit()])
    choose = input("Your turn, enter cell number: ")
    while choose not in clean_list:
        fresh_screen(board)
        print(f'{choose} is invalid: ')
        choose = input("Your turn, enter cell number: ")
    for num, x in enumerate(board):
        if x == choose:
            board[num] = "O"
    return board
# Function make random Bot turn
def bot_turn(board):
    clean_list = ([x for x in board if x.isdigit()])
    choose = random.choice(list(map(int, clean_list)))
    for num, x in enumerate(board):
        board[choose-1] = "X"
    return board
# Function clear screen and draw board
def fresh_screen(board):
    os.system('cls')
    for num, x in enumerate(board):
        print(*x, end=" ")
        if (num+1)%3 == 0:
            print()
    return board
# Play board
board = \
[
"1", "2", "3",
"4", "5", "6",
"7", "8", "9"
]
# Bot name, could be changed
bot = "Bot"
fresh_screen(board)
man = input("Enter your name: ")
# First player random choice
lot = random.choice([man, bot])
if lot == bot:
    fresh_screen(board)
    print(f'{lot} is first with eXes. ', end="")
    input("Press enter to start!")
else:
    fresh_screen(board)
    print(f"{man} is first wih zer0s. ", end="")
# Game core
count = 0
while count < 9:
    if lot == bot:
        board = bot_turn(board)
        fresh_screen(board)
        lot = man
    else:
        board = man_turn(board)
        fresh_screen(board)
        lot = bot
    if winner_check(board) == "O":
        print(f'The winner is {man}')
        exit()
    elif winner_check(board) == "X":
        print(f'The winner is {bot}')  
        exit()
    count += 1
print("Nobody wins")
exit()
