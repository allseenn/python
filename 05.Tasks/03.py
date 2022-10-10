# 3. Создайте программу для игры в "Крестики-нолики".
import random
import os
# Man turn
def man_turn(board):
    zero = input("Enter number of cell: ")
    for x in board:
        if x == zero:
            x = "0"
    return board
# Bot turn
def bot_turn(board):
    cross = input("Enter number of cell: ")
    for x in board:
        if x == cross:
            x = "X"
    return board
# Function clear screen and draw board
def fresh_screen(board):
    #clear = lambda: os.system('cls')
    #clear()
    for x in board:
        print(" ".join(x))
    return board

board = \
[
["1", "2", "3"],
["4", "5", "6"],
["7", "8", "9"]
]
bot = "Bot"
fresh_screen(board)
man = input("Enter your name: ")
# First player random choice
lot = random.choice([man, bot])
if lot == bot:
    fresh_screen(board)
    print(f'First player is {lot} with CROSS')
else:
    fresh_screen(board)
    print(f"{man}, you're first player with ZERO")
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
    count += 1
