# 2. Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# - a) Добавьте игру против бота
# - b) Подумайте как наделить бота "интеллектом"
import random
# Function checks man to take rules quantity max and min candies
def man_quantity(min, max):
    candy = int(input("How many candies you takes?: "))
    while candy > max or candy < min: 
        print ("You could take more than 0 and no more than 28 candies!")
        candy = int(input("How many candies you takes?: "))
    return candy
# Function bot take random candies
def bot_quantity(min, max):
    candy = random.randint(min, max+1)
    print(f"{bot}, takes {candy} candies")
    return candy
# Print rules of the game
text = "On the desk is 2021 candies.\n\
2 players make move one by one.\n\
Who is first player decides the lot.\n\
With on movie player could take no more than 28 candies\n\
Winner is player with last move.\n\
How many candies must take first player to win?"
print(text)
# Games VARS, could be changed
candies = 221
max = 28
min = 1
bot = "Bot"
##############################
man = input("Enter your name: ")
# First player random choice
lot = random.choice([man, bot])
if lot == bot:
    print(f'First player is {lot}')
else:
    print(f"{man}, you're first player")
# Game core
while candies > 1:
    if lot == bot:
        candies -= bot_quantity(min, max)
        if candies < 0:
            break
        print(f'{candies} candies left')
        lot = man
    else:
        candies -= man_quantity(min, max)
        if candies < 0:
            break
        print(f'{candies} candies left')
        lot = bot

# Who is looser :))
print(f"{lot}, is lost, {candies} candies!")
