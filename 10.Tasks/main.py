import telebot
import logging
import viewer
##### TOKEN ###############
with open ('D:\Documents\Bots\GBpyBot.txt', 'r') as file:
    TOKEN = file.readline()
#TOKEN = ""
#############################
bot = telebot.TeleBot(TOKEN)

logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
value = ''
old_value = ''

@bot.message_handler(commands=['start', 's'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
/s /start - данное сообщение
/h /help - вызов справки
/c /calc - запуск калькулятора
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['help', 'h'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
/i /info - описание программы
/a /add - описание сложения
/s /subtract - описание вычитания
/m /multiply - описание умножения
/d /divide - описание деления
/p /power - описание возведения в степень
/r /root - описание извлечения корня
/x /complex - описание работы с комплексными числами
/e /expression - сложные выражения
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['info', 'i'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Бот выводит графическое представление калькулятора инлайн, т.е. внутри списка сообщений.
/calc - Для начала работы в окне ввода текста необходимо ввести команду
/help Для вызова справки, необходимо выполнить команду
Калькулятор может выполнять следующие операции:
/a Сложение
/s Вычитание
/m Умножение
/d Деление
/p Возведение в степень
/r Извлечение корня
/x Работать с комплексными числами
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['add', 'a'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Для сложения целых чисел, нажимаем на калькуляторе кнопку с соответствующим числом, 
знак +, второе слагаемое и знак =
Выражение может состоять из нескольких слагаемых, 
а так же содержать дробные числа:
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['subtract', 's'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Для вычитания целых чисел, нажимаем на калькуляторе кнопку с соответствующим числом, 
знак -, вычитаемое и знак =
Выражение может состоять из нескольких вычитаемых,
а так же содержать дробные числа
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['multiply', 'm'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Для умножения целых чисел, нажимаем на калькуляторе кнопку с соответствующим числом,
знак *, второй множитель и знак =
Выражение может состоять из нескольких множителей, 
а так же содержать дробные числа
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['divide', 'd'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Для деления целых чисел, нажимаем на калькуляторе кнопку с соответствующим числом, 
знак /, делитель и знак =
Выражение может состоять из нескольких делителей, а так же содержать дробные числа
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['power', 'p'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Для возведения в степень целых чисел, нажимаем на калькуляторе кнопку 
с соответствующим числом, два знака **, вводим показатель степени и знак =
Основание степени и показатель могут быть дробными числами:
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['root', 'r'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Для нахождения корня, основание возвести в соответствующую дробную степень, 
отделя показатель степени скобками корень квадратный из четырех, далее =:
4**(1/2)=
Корень кубический из 125:
125**(1/3)=
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['complex', 'x'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Для работы с комплексными числами нажимаем С, 
вводим в скобках (действительная часть, мнимая), знак равно
complex(1,2)=
Арифметические операция над комплесными числами, 
аналогично вышеизложенному описанию, только указываем знак +, -, / или *:
complex(1,2)+complex(1,2)=
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['expression', 'e'])
def start(message):
    logger.info("User %s enter %s", message.chat.username, message.text)
    mess = """
Используя скобки (), можно составлять сложные выражения, 
содержащие степени, корни, комплексные числа, 
задавая нужный приоритет выполнения операции.
complex(1,2)+(5**2-125**(1/3))
    """
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['calc', 'c'])
def getMessage(message):
    global value
    logger.info("User %s enter %s", message.chat.username, message.text)
    if value == '':
        bot.send_message(message.from_user.id,
                         '0', reply_markup=viewer.keyboard)
    else:
        bot.send_message(message.from_user.id,
                         value, reply_markup=viewer.keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    logger.info("User enter %s", value)
    data = query.data
    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        value = str(eval(value))
    else:
        value += data
    if value != old_value:
        if value == '':
            bot.edit_message_text(
                chat_id=query.message.chat.id, message_id=query.message.id, text='0', reply_markup=viewer.keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id, text=value, reply_markup=viewer.keyboard)
        old_value = value

bot.polling()