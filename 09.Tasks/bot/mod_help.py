from telegram import Update
import datetime as dt

START = """
Добро пожаловать, в игру крестики нолики!
Для вызова списка команд набери /h
Вызов справки по команде /h <command> 
Ознакомиться с правилами игры /h rules
Приятного отдыха!
"""

HELP="""
/start - краткое описание
/h - вывод данного окна
/h rules - вывод правил игры
/h author - авторская информация
/h time - вывод текущего времени
/n - (пере)запуск новый игры
/s <number> - ход с номером ячейки
"""
time = dt.datetime.now().strftime("%Y%m%d %H:%M:%S")

author = """
@allseen Ростислав Ромашин
"""
rules = """
ПРАВИЛА ИГРЫ КРЕСТИКИ НОЛИКИ:
1 2 3  Поле размером 3x3 ячейки
4 5 6  Бот играет крестиками X
7 8 9  Человек играет ноликами O
Право первого хода определяет жребий
Ячейки пронумерованы от 1 до 9
Игроки заполняют свободные ячейки
Игрок вводит команду /s 5
Где /s это сокращение от step
  /s|пробел|номер ячейки|
Игрок первым занявший любой ряд  
3-мя своими символами по вертикали,
горизонтали или диагонали, выигрывает.
Если за пять ходов никто не выиграл,
то объявляется ничья.
"""

async def start(update: Update, context):
    await update.message.reply_text(f'Привет, {update.effective_user.first_name} {START}')

async def help(update: Update, context):
    string = update.message.text.split()
    if len(string) == 1:
        await update.message.reply_text(f'{HELP}')
    else:
        await update.message.reply_text(f'{globals()[string[1]]}')