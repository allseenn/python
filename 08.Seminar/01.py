# **Задача:** Создать информационную систему позволяющую работать с 
# сотрудниками некой компании \ студентами вуза \ учениками школы

import json
import csv
from pathlib import Path

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))
{"id": 1, "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432", "first_name": "\u0418\u0432\u0430\u043d \u041f\u0435\u0442\u0440\u043e\u0432\u0438\u0447", "position": "\u0433\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440", "phone_number": "111", "salary": 1000.0}
{"id": 2, "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432\u0430", "first_name": "\u041c\u0430\u0440\u0438\u044f \u0418\u0432\u0430\u043d\u043e\u0432\u043d\u0430", "position": "\u0433\u043b\u0430\u0432\u043d\u044b\u0439 \u0431\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440", "phone_number": "222", "salary": 999.99}
# 1	Иванов	Иван Петрович	генеральный директор	111	1000.0
# 2	Иванова	Мария Ивановна	главный бухгалтер	222	999.99
def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee


def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

# https://ru.wikipedia.org/wiki/Задача_Иосифа_Флавия
# Sample Input 1:
# 2
# 1
# Sample Output 1:
# 2
# Sample Input 2:
# 5
# 2
# Sample Output 2:
# 3
# Sample Input 3:
# 7
# 5
# Sample Output 3:
# 6
