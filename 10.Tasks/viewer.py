import telebot

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('\uFF08', callback_data='('),
             telebot.types.InlineKeyboardButton('\uFF09', callback_data=')'),
             telebot.types.InlineKeyboardButton('\u232B', callback_data='<='),
             telebot.types.InlineKeyboardButton('\u2797', callback_data='/'))
keyboard.row(telebot.types.InlineKeyboardButton('\uFF17', callback_data='7'),
             telebot.types.InlineKeyboardButton('\uFF18', callback_data='8'),
             telebot.types.InlineKeyboardButton('\uFF19', callback_data='9'),
             telebot.types.InlineKeyboardButton('\u2716', callback_data='*'))
keyboard.row(telebot.types.InlineKeyboardButton('\uFF14', callback_data='4'),
             telebot.types.InlineKeyboardButton('\uFF15', callback_data='5'),
             telebot.types.InlineKeyboardButton('\uFF16', callback_data='6'),
             telebot.types.InlineKeyboardButton('\u2796', callback_data='-'))
keyboard.row(telebot.types.InlineKeyboardButton('\uFF11', callback_data='1'),
             telebot.types.InlineKeyboardButton('\uFF12', callback_data='2'),
             telebot.types.InlineKeyboardButton('\uFF13', callback_data='3'),
             telebot.types.InlineKeyboardButton('\u2795', callback_data='+'))
keyboard.row(telebot.types.InlineKeyboardButton('\uFF23', callback_data='complex'),
             telebot.types.InlineKeyboardButton('\uFF10', callback_data='0'),
             telebot.types.InlineKeyboardButton('\u275F', callback_data='.'),
             telebot.types.InlineKeyboardButton('\U0001F7F0', callback_data='='))
