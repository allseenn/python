# Создайте программу для игры в ""Крестики-нолики"".

import telebot
from telebot import types

TOKEN = "5501756584:AAEw3bT6QibRgjGBP1enKb5diEZXmRVMfmU"
bot = telebot.TeleBot(TOKEN)

pole = list(range(1, 10))
player = 'X'
win_komb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

@bot.message_handler(commands=['start'])
def bot_pole(message):
    bot.send_message(message.chat.id, draw_pole() )
    
    

@bot.message_handler(content_types=['text'])
def bot_message(message, pole=pole):
    global player
    hod = message.text
    if  hod not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        bot.send_message(message.chat.id,'Введите верный номер клеточки для хода')
    else:
        hod = int(hod)
        if str(pole[hod-1]) in 'XO':
            bot.send_message(message.chat.id, 'Клетка занята, выберите другую')
        else:
            pole[hod-1] = player
            bot.send_message(message.chat.id, draw_pole() )
            if player == 'X':
                player = 'O'
            else:
                player = 'X'


def draw_pole(): # функция отрисовки игрового поля
    new_pole = '-------------\n'
    for i in range(3):
        new_pole += '| ' + str(pole[0 + i*3]) + ' | ' +  str(pole[1 + i*3]) + ' | ' + str(pole[2 + i*3]) + ' |\n'
    new_pole +='-------------'
    return new_pole

def take_hod(hod, pole=pole): # фукнция хода игрока
    while True:
        # hod = input('Куда поставить ' + player + ' ? ')
        if  hod not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # print('Введите вереый номер клеточки для хода')
            continue
        hod = int(hod)
        if str(pole[hod-1]) in 'XO':
            # print('Клетка занята, выберите другую')
            continue
        pole[hod-1] = player
        break
    


def check_win(): # функция проверка на выигрыш
    for elem in win_komb:
        if pole[elem[0]] == pole[elem[1]] == pole[elem[2]]:
            return pole[elem[0]]
    else:
        return False

# def game(): # функция самой игры и смены ходов
#     a = 0
#     while True:
#         if a % 2 == 0: 
#             bot_message()
#             take_hod('X')
#         else:
#             take_hod('O')
#         if a > 3:
#             win = check_win()
#             if win:
#                 # os.system('cls')
#                 draw_pole()
#                 print(win, 'Выиграл!!!')
#                 break
#         a += 1
#         if a > 8:
#             # os.system('cls')
#             draw_pole()
#             print('Ничья!!')
#             break
# game()

bot.polling()