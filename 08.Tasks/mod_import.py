import json
import csv
BASE = 'base.csv'

def imp(name):
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    count = 0
    if name[0] != '':
        with open(name[0], "r") as file0in:
            data0 = json.load(file0in)
        dict_fields = ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Рождение', 'Профессия', 'Оклад', 'Адрес', 'Сотовый', 'Городской']
        with open(BASE,'a', encoding='cp1251') as file0out:
            w = csv.DictWriter(file0out, fieldnames=dict_fields, delimiter=";", lineterminator="\n")
            w.writerows(data0)
        count += len(data0)
    if name[1] != '':  
        with open(name[1], "r") as file1in:
            csv_reader = csv.reader(file1in, delimiter=";", lineterminator="\n")
            for row in csv_reader:
                temp = {}
                temp['СНИЛС'] = int(row[0])
                temp['Фамилия'] = row[1]
                temp['Имя'] = row[2]
                temp['Отчество'] = row[3]
                temp['Рождение'] = row[4]
                temp['Профессия'] = row[5]
                temp['Оклад'] = int(row[6])
                temp['Адрес'] = row[7]
                temp['Сотовый'] = int(row[8])
                temp['Городской'] = int(row[8])
                data1.append(temp)
        dict_fields = ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Рождение', 'Профессия', 'Оклад', 'Адрес', 'Сотовый', 'Городской']
        with open(BASE,'a', encoding='cp1251') as file1out:
            w = csv.DictWriter(file1out, fieldnames=dict_fields, delimiter=";", lineterminator="\n")
            w.writerows(data1)
        count += len(data1)
    if name[2] != '':  
        with open(name[2], "r") as file2in:
            csv_reader = csv.reader(file2in, delimiter=",", lineterminator="\n")
            for row in csv_reader:
                temp = {}
                temp['СНИЛС'] = int(row[0])
                temp['Фамилия'] = row[1]
                temp['Имя'] = row[2]
                temp['Отчество'] = row[3]
                temp['Рождение'] = row[4]
                temp['Профессия'] = row[5]
                temp['Оклад'] = int(row[6])
                temp['Адрес'] = row[7]
                temp['Сотовый'] = int(row[8])
                temp['Городской'] = int(row[8])
                data2.append(temp)
        dict_fields = ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Рождение', 'Профессия', 'Оклад', 'Адрес', 'Сотовый', 'Городской']
        with open(BASE,'a', encoding='cp1251') as file2out:
            w = csv.DictWriter(file2out, fieldnames=dict_fields, delimiter=";", lineterminator="\n")
            w.writerows(data2)
        count += len(data2)
    if name[3] != '':  
        with open(name[3], "r") as file3in:
            csv_reader = csv.reader(file3in, delimiter='\t', lineterminator='\n')
            for row in csv_reader:
                temp = {}
                temp['СНИЛС'] = int(row[0])
                temp['Фамилия'] = row[1]
                temp['Имя'] = row[2]
                temp['Отчество'] = row[3]
                temp['Рождение'] = row[4]
                temp['Профессия'] = row[5]
                temp['Оклад'] = int(row[6])
                temp['Адрес'] = row[7]
                temp['Сотовый'] = int(row[8])
                temp['Городской'] = int(row[8])
                data3.append(temp)
        dict_fields = ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Рождение', 'Профессия', 'Оклад', 'Адрес', 'Сотовый', 'Городской']
        with open(BASE,'a', encoding='cp1251') as file3out:
            w = csv.DictWriter(file3out, fieldnames=dict_fields, delimiter=";", lineterminator="\n")
            w.writerows(data3)
        count += len(data3)
    return f'Импортировано {count} зап.'

