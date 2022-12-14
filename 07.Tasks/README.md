### Задание 

- Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
- Есть файл, состоящий из N тысяч строк содержащих информацию о неких пользователях.
- Предлагаемые поля: id, имя, фамилия, день рождения, место работы, номер телефона (может быть несколько).
- В качестве символа разделителя использовать пустую строку.

### Пояснения

#### СУБД "Справочник военкомата 2022"
- Система управления базой данных, несуществующей организации ["Справочник военкомата 2022"](https://github.com/allseenn/python/tree/main/07.Tasks/main.py). Вся информация в данной СУБД (СНИЛС, ФИО, Телефоны и др.) генерируются автоматически и не содержит персональных данных.

- СУБД позволяет:

1. Создать базу
2. Удалить базу
3. Добавить запись
4. Удалить запись
5. Найти записи
6. Экспортировать в HTML
7. Экспортировать в XML
8. Экспортировать в CSV
9. Выводить результаты поиска на экран

 ### 1. Создать базу
- При первом запуске СУБД, либо при удаленной БД, отобразится сообщение "Нет базы!!!"
- ![noBase](pics/11.png)
- После ввода "1" литеры пункта меню "Создать базу", отобразиться следующее окно:
- ![5000](pics/12.png)
- После ввода желаемого количества строк, СУБД сгенерирует БД:
- ![m](pics/13.png)
- Для возврат в главное меню нажимаем "m".

### 2. Удалить базу
- Для удаления БД в главном меню вводим номер "2":
- ![2](pics/21.png)
- Для подтверждения удаления необходимо нажать прописную "Y":
- ![no base](pics/22.png)
- После удаления БД, возвращаемся в главное меню "m":
- ![2m](pics/23.png)

### 3. Добавить запись
- В главном меню выбираем номер "3":
- ![3](pics/31.png)
- Откроется подменю, для добавления записи необходимо заполнить все поля, выбирая соответствующую литеру, например, для СНИЛС это "i":
- ![i](pics/32.png)
- После ввода значения полей информация будет отображаться внизу экрана, над строкой ввода номера меню:
- ![s](pics/33.png)
- Для сохранения введенных значений в БД, необходимо сохранить/добавить запись, введя "s":
- ![3m](pics/34.png)
- Для возврата в главное меню используем "m".

### 4. Удалить запись
- В главном меню выбираем номер меню "4":
- ![4](pics/41.png)
- В открывшемся подменю заполняем все поля, путем ввода литеры соответствующего пункта меню, например для СНИЛС "i":
- ![4i](pics/42.png)
- После заполнения желаемых полей, для удаления записи или нескольких записей, в случае заполнения не всех полей, вводим "r":
- ![4m](pics/43.png)
- В отображенном подменю указано количество удаленных записей, соответствующих заданным критериям. Для возврата в главное меню нажимаем "m".

### 5. Найти записи
- В главном меню вводим номер "5":
- ![5](pics/51.png)
- В открывшемся подменю заполняем все поля с помощью соответствующих литер, например для ВУС это "u", для Категории "c". При заполнении полей, значения будут отображаться внизу экрана, над строкой ввода номера меню.
- Для запуска поиска нажимаем "s":
- ![5s](pics/52.png)
- В результате поиска откроется подменю с возможностью экспорта результатов поиска в 3 формата, либо вывод результатов на экран.
Внизу экрана, над строкой ввода номера записи отобразится количество найденных записей.
- ![h](pics/53.png)

### 6. Экспортировать в HTML
- После осуществления поиска (см. пункт 5. Найти запись) откроется подменю экспорта. Результаты последнего поиска сохраняются в памяти программы, что позволяет перемещаться по уровням меню. Так из главного меню при нажатии литеры "e" попадаем в меню экспорта, и при ранее осуществленном поиске, о количестве найденных записей сообщает надпись "Найдено записей".
- Для экспорта в файл формата HTML вводим "h" в поле ввода номера, подменю экспорта:
- ![e](pics/61.png)
- Данное окно сообщает о количестве экспортируемых строк и название сохраненного файла в корневом каталоге программы:
- ![html](pics/62.png)
- Для возврата в окно экспорта вводим "e". Для возврата в главное меню вводим "m".

### 7. Экспортировать в XML
- Из меню поиска (см.пункт 5.Найти запись). Либо при сохраненном запросе из главного меню нажимаем "e", для отрытия окна экспорта, в котором выбираем "x" для экспорта в формат XML:
- ![x](pics/71.png)
- В результате экспорта отобразится окно с результатом и именем сохраненного файла xml:
- ![7e](pics/72.png)
- Для возврата в окно экспорта вводим "e". Для возврата в главное меню вводим "m".

### 8. Экспортировать в CSV
- Из меню поиска (см.пункт 5.Найти запись). Либо при сохраненном запросе из главного меню нажимаем "e", для отрытия окна экспорта, в котором выбираем "v" для экспорта в формат CSV:
- ![v](pics/81.png)
- В результате экспорта отобразится окно с результатом и именем сохраненного файла xml:
- ![8e](pics/82.png)
- Для возврата в окно экспорта вводим "e". Для возврата в главное меню вводим "m".

### 9. Выводить результаты поиска на экран
- Из меню поиска (см.пункт 5.Найти запись). Либо при сохраненном запросе из главного меню нажимаем "e", для отрытия окна экспорта, в котором выбираем "p" для вывода записей на экран:
- ![v](pics/91.png)
- В результате на экран терминал будут выведены ранее найденные записи:
- ![9e](pics/92.png)
- Для возврата в окно экспорта вводим "e". Для возврата в главное меню вводим "m".