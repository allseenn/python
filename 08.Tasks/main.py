import mod_view
import mod_db
import mod_export
import mod_import

data = ["", "", "", "", "", "", "", "", "", ""]
res = []
imp = ['', '', '', '']
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
            elif sub == "l":
                data[1] = input("Введите Фамилию: ")
            elif sub == "n":
                data[2] = input("Введите Имя: ")
            elif sub == "f":
                data[3] = input("Введите Отчество: ")
            elif sub == "a":
                data[4] = input("Введите возраст: ")
            elif sub == "u":
                data[5] = input("Введите должность: ")
            elif sub == "c":
                data[6] = input("Введите оклад: ")
            elif sub == "d":
                data[7] = input("Введите адрес: ")
            elif sub == "o":
                data[8] = input("Введите мобильный: ")
            elif sub == "p":
                data[9] = input("Введите телефон: ")
            elif sub == "q":
                exit()
            elif sub == "s":
                mod_view.mini()
                print(mod_db.save(data))
                break
            elif sub == "m":
                mod_view.main()
                break
        submenu = input("Введите номер меню: ")
    elif submenu == "4": # Удалить запись
        sub = ""
        while "r" not in sub:# Меню удаления
            mod_view.delete()
            print(*data)
            sub = input("Введите номер меню: ")
            if sub == "i":
                data[0] = input("Введите номер СНИЛС: ")
            elif sub == "l":
                data[1] = input("Введите Фамилию: ")
            elif sub == "n":
                data[2] = input("Введите Имя: ")
            elif sub == "f":
                data[3] = input("Введите Отчество: ")
            elif sub == "a":
                data[4] = input("Введите возраст: ")
            elif sub == "u":
                data[5] = input("Введите должность: ")
            elif sub == "c":
                data[6] = input("Введите оклад: ")
            elif sub == "d":
                data[7] = input("Введите адрес: ")
            elif sub == "o":
                data[8] = input("Введите мобильный: ")
            elif sub == "p":
                data[9] = input("Введите телефон: ")
            elif sub == "q":
                exit()
            elif sub == "r":
                mod_view.mini()
                print(mod_db.delete(data))
                break
            elif sub == "m":
                mod_view.main()
                break
        submenu = input("Введите номер меню: ")
    elif submenu == "5": # Изменить запись
        sub = ""
        while "y" not in sub:# Меню записи
            mod_view.edit()
            print(*data)
            sub = input("Введите номер меню: ")
            if sub == "i":
                data[0] = input("Введите номер СНИЛС: ")
            elif sub == "l":
                data[1] = input("Введите Фамилию: ")
            elif sub == "n":
                data[2] = input("Введите Имя: ")
            elif sub == "f":
                data[3] = input("Введите Отчество: ")
            elif sub == "a":
                data[4] = input("Введите возраст: ")
            elif sub == "u":
                data[5] = input("Введите должность: ")
            elif sub == "c":
                data[6] = input("Введите оклад: ")
            elif sub == "d":
                data[7] = input("Введите адрес: ")
            elif sub == "o":
                data[8] = input("Введите мобильный: ")
            elif sub == "p":
                data[9] = input("Введите телефон: ")
            elif sub == "q":
                exit()
            elif sub == "y":
                mod_view.mini()
                print(mod_db.edit(data))
                break
            elif sub == "m":
                mod_view.main()
                break
        submenu = input("Введите номер меню: ")
    elif submenu == "6": # Найти записи
        sub = ""
        while "s" not in sub:# Меню поиска
            mod_view.search()
            print(*data)
            sub = input("Введите номер меню: ")
            if sub == "i":
                data[0] = input("Введите номер СНИЛС: ")
            elif sub == "l":
                data[1] = input("Введите Фамилию: ")
            elif sub == "n":
                data[2] = input("Введите Имя: ")
            elif sub == "f":
                data[3] = input("Введите Отчество: ")
            elif sub == "a":
                data[4] = input("Введите возраст: ")
            elif sub == "u":
                data[5] = input("Введите должность: ")
            elif sub == "c":
                data[6] = input("Введите оклад: ")
            elif sub == "d":
                data[7] = input("Введите адрес: ")
            elif sub == "o":
                data[8] = input("Введите мобильный: ")
            elif sub == "p":
                data[9] = input("Введите телефон: ")
            elif sub == "q":
                exit()
            elif sub == "s":
                submenu = "e"
                break
            elif sub == "m":
                submenu = "m"
                break
        #submenu = "e"
    elif submenu == "e": # ПодМеню поиска
        res = mod_db.search(data)
        mod_view.export()
        print(f"Найдено {len(res)} записей")
        submenu = input("Введите номер меню: ")
    elif submenu == "t": # ПодМеню импорта
        res = mod_db.search(data)
        mod_view.export()
        print(f"Найдено {len(res)} записей")
        submenu = input("Введите номер меню: ")
    elif submenu == "b": # ПодМеню Сохранить в буфер
        mod_view.html()
        data = res[0]
        print(f'В буфере: {" ".join(data)}')
        submenu = input("Введите номер меню: ")
    elif submenu == "i": # ПМеню экспорта
        sub = ""
        while "i" not in sub:# ПодПодменю экспорта
            mod_view.imp()
            print(*imp)
            sub = input("Введите номер меню: ")
            if sub == "j":
                imp[0] = input("Имя json файла: ")
            elif sub == "n":
                imp[1] = input("Имя csv разделитель ';' : ")
            elif sub == "c":
                imp[2] = input("Имя csv разделитель ',' : ")
            elif sub == "t":
                imp[3] = input("Имя csv разделитель табуляция : ")
            elif sub == "q":
                exit()
            elif sub == "i":
                mod_view.imp()
                print(mod_import.imp(imp))
                break
            elif sub == "m":
                mod_view.main()
                break
        submenu = input("Введите номер меню: ")
    elif submenu == "h": # ПодМеню экспорта html
        mod_view.html()
        print(mod_export.html(res))
        submenu = input("Введите номер меню: ")
    elif submenu == "x": # ПодМеню экспорта xml
        mod_view.xml()
        print(mod_export.xml(res))
        submenu = input("Введите номер меню: ")
    elif submenu == "j": # ПодМеню экспорта jason
        mod_view.jason()
        print(mod_export.jason(res))
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