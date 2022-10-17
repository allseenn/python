import mod_view
import mod_db
import mod_export

data = ["", "", "", "", "", "", "", ""]
res = []
submenu = "m"
while submenu != "q":
    if submenu == "0": # Мини меню без обновления
        mod_view.mini()
        submenu = input("Введите номер меню: ")
    elif submenu == "1": # Создать базу
        mod_view.mini()
        print(mod_db.generate(input("Введите кол-во строк в базе: ")))
        submenu = input("Введите номер меню: ")
    elif submenu == "2": # Удалить базу
        mod_view.drop()
        confirm = input("Уверены, что удалить, нажмите Y/n: ")
        if confirm == "Y":
            mod_view.mini()
            print(mod_db.drop())
            submenu = input("Введите номер меню: ")
        else: 
            submenu = "0"
    elif submenu == "3": # Добавить запись
        sub = ""
        while "s" not in sub:# Меню добавления
            mod_view.save()
            print(*data)
            sub = input("Введите номер меню: ")
            if sub == "i":
                data[0] = input("Введите номер СНИЛС: ")
            elif sub == "n":
                data[1] = input("Введите ФИО: ")
            elif sub == "a":
                data[2] = input("Введите возраст: ")
            elif sub == "u":
                data[3] = input("Введите ВУС: ")
            elif sub == "c":
                data[4] = input("Введите категорию: ")
            elif sub == "d":
                data[5] = input("Введите адрес: ")
            elif sub == "o":
                data[6] = input("Введите мобильный: ")
            elif sub == "f":
                data[7] = input("Введите телефон: ")
            elif sub == "q":
                exit()
        mod_view.mini()
        print(mod_db.save(data))
        submenu = input("Введите номер меню: ")
    elif submenu == "4": # Удалить запись
        sub = ""
        while "r" not in sub:# Меню удаления
            mod_view.delete()
            print(*data)
            sub = input("Введите номер меню: ")
            if sub == "i":
                data[0] = input("Введите номер СНИЛС: ")
            elif sub == "n":
                data[1] = input("Введите ФИО: ")
            elif sub == "a":
                data[2] = input("Введите возраст: ")
            elif sub == "u":
                data[3] = input("Введите ВУС: ")
            elif sub == "c":
                data[4] = input("Введите категорию: ")
            elif sub == "d":
                data[5] = input("Введите адрес: ")
            elif sub == "o":
                data[6] = input("Введите мобильный: ")
            elif sub == "f":
                data[7] = input("Введите телефон: ")
            elif sub == "q":
                exit()
        mod_view.mini()
        print(mod_db.delete(data))
        submenu = input("Введите номер меню: ")
    elif submenu == "5": # Найти записи
        sub = ""
        while "s" not in sub:# Меню поиска
            mod_view.search()
            print(*data)
            sub = input("Введите номер меню: ")
            if sub == "i":
                data[0] = input("Введите номер СНИЛС: ")
            elif sub == "n":
                data[1] = input("Введите ФИО: ")
            elif sub == "a":
                data[2] = input("Введите возраст: ")
            elif sub == "u":
                data[3] = input("Введите ВУС: ")
            elif sub == "c":
                data[4] = input("Введите категорию: ")
            elif sub == "d":
                data[5] = input("Введите адрес: ")
            elif sub == "o":
                data[6] = input("Введите мобильный: ")
            elif sub == "f":
                data[7] = input("Введите телефон: ")
            elif sub == "q":
                exit()
        submenu = "e"
    elif submenu == "e": # ПодМеню поиска
        res = mod_db.search(data)
        mod_view.export()
        print(f"Найдено {len(res)} записей")
        submenu = input("Введите номер меню: ")
    elif submenu == "h": # ПодМеню экспорта html
        mod_view.html()
        print(mod_export.html(res))
        submenu = input("Введите номер меню: ")
    elif submenu == "x": # ПодМеню экспорта xml
        mod_view.xml()
        print(mod_export.xml(res))
        submenu = input("Введите номер меню: ")
    elif submenu == "v": # ПодМеню экспорта cvs
        mod_view.csv()
        print(mod_export.csv(res))
        submenu = input("Введите номер меню: ")
    elif submenu == "p": # ПодМеню вывода на экран
        mod_view.prints()
        print(mod_export.prints(res))
        submenu = input("Введите номер меню: ")    
    elif submenu == "m": # Возврат в главное меню
        mod_view.main()
        submenu = input("Введите номер меню: ")
    elif submenu == "q": # Выход
        exit()
    else: # ПодМеню выхода либо возврата на главный экран при введении несуществующего меню
        mod_view.error()
        submenu = input("Введите номер меню: ")