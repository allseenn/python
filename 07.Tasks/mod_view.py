import os
BASE = 'base.csv'
MAIN = "\
1. Создать базу\n\
2. Удалить базу\n\
3. Добавить запись\n\
4. Удалить запись\n\
5. Найти записи\n\
e. Экспорт\n\
q. Выход"
ADD = "\
m. Главное меню\n\
q. Выход"
DELETE = "\
i. СНИЛС\n\
n. ФИО\n\
a. Возраст\n\
u. ВУС\n\
c. Категория\n\
d. Адрес\n\
o. Сотовый\n\
f. Телефон\n\
q. Выход\n\
r. Удалить"
SEARCH = "\
i. СНИЛС\n\
n. ФИО\n\
a. Возраст\n\
u. ВУС\n\
c. Категория\n\
d. Адрес\n\
o. Сотовый\n\
f. Телефон\n\
q. Выход\n\
s. Поиск"
SAVE = "\
i. СНИЛС\n\
n. ФИО\n\
a. Возраст\n\
u. ВУС\n\
c. Категория\n\
d. Адрес\n\
o. Сотовый\n\
f. Телефон\n\
q. Выход\n\
s. Сохранить"
MINI = "\
m. Главное меню\n\
q. Выход"
ERROR = "\
Нет такова пункта меню!\n\
m. Главное меню\n\
q. Выход"
DROP = "\
m. Главное меню\n\
q. Выход"
EXPORT = "\
h. Экспорт в html\n\
x. Экспорт в xml\n\
v. Экспорт в csv\n\
p. Вывод на экран\n\
m. Главное меню\n\
q. Выход"
HTML = "\
m.меню, q.выход, e.экспорт"
XML = "\
m.меню, q.выход, e.экспорт"
CSV = "\
m.меню, q.выход, e.экспорт"
PRINTS = "\
m.меню, q.выход, e.экспорт"

def mini():
    os.system('cls')
    print(MINI)

def main():
    if os.path.isfile(BASE):
        os.system('cls')
        print(MAIN)
    else:
        os.system('cls')
        print("Нет базы!!!")
        print(MAIN)

def drop():
    os.system('cls')
    print(DROP)

def delete():
    os.system('cls')
    print(DELETE)

def search():
    os.system('cls')
    print(SEARCH)

def save():
    os.system('cls')
    print(SAVE)

def export():
    os.system('cls')
    print(EXPORT)

def html():
    os.system('cls')
    print(HTML)

def xml():
    os.system('cls')
    print(XML)

def csv():
    os.system('cls')
    print(CSV)

def prints():
    os.system('cls')
    print(PRINTS)

def error():
    os.system('cls')
    print(ERROR)
