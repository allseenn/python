import os
BASE = 'base.csv'
MAIN = "\
1. Создать базу\n\
2. Удалить базу\n\
3. Добавить запись\n\
4. Удалить записи\n\
5. Изменить записи\n\
6. Найти записи\n\
i. Импорт\n\
e. Экспорт\n\
q. Выход"
ADD = "\
m. Главное меню\n\
q. Выход"
DELETE = "\
i. СНИЛС\n\
l. Фамилия\n\
n. Имя\n\
f. Отчество\n\
a. Возраст\n\
u. Должность\n\
c. Оклад\n\
d. Адрес\n\
o. Сотовый\n\
p. Телефон\n\
m. Меню\n\
q. Выход\n\
r. Удалить"
SEARCH = "\
i. СНИЛС\n\
l. Фамилия\n\
n. Имя\n\
f. Отчество\n\
a. Возраст\n\
u. Должность\n\
c. Оклад\n\
d. Адрес\n\
o. Сотовый\n\
p. Телефон\n\
m. Меню\n\
q. Выход\n\
s. Поиск"
SAVE = "\
i. СНИЛС\n\
l. Фамилия\n\
n. Имя\n\
f. Отчество\n\
a. Возраст\n\
u. Должность\n\
c. Оклад\n\
d. Адрес\n\
o. Сотовый\n\
p. Телефон\n\
m. Меню\n\
q. Выход\n\
s. Сохранить"
EDIT = "\
i. СНИЛС\n\
l. Фамилия\n\
n. Имя\n\
f. Отчество\n\
a. Возраст\n\
u. Должность\n\
c. Оклад\n\
d. Адрес\n\
o. Сотовый\n\
p. Телефон\n\
m. Меню\n\
q. Выход\n\
y. Изменить"
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
b. Сохранить в буфер\n\
j. Экспорт в json\n\
h. Экспорт в html\n\
x. Экспорт в xml\n\
v. Экспорт в csv\n\
p. Вывод на экран\n\
m. Главное меню\n\
q. Выход"
IMP = "\
j. JSON имя файла\n\
n. CSV ; имя файла\n\
c. CSV , имя файла\n\
t. CSV t имя файла\n\
i. Выполнить импорт\n\
m. Главное меню\n\
q. Выход"
BUFFER = "\
m.меню, q.выход, e.экспорт"
JASON = "\
m.меню, q.выход, e.экспорт"
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

def edit():
    os.system('cls')
    print(EDIT)

def export():
    os.system('cls')
    print(EXPORT)

def imp():
    os.system('cls')
    print(IMP)

def buffer():
    os.system('cls')
    print(BUFFER)

def jason():
    os.system('cls')
    print(JASON)

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
