*a - раскрывание итерируемого объекта

Создать словарь:
1) Первый Способ:
d={
    #key:value,
    'moskva': 495,
    'piter': 812,
    'penza': 8412
}
2) Второй Способ:
r=dict(moskva= 495, piter= 812, penza= 8412)

3.1) Третий способ:
a=[['moskva', 495], ['piter',812,], ['penza', 8412]]
t=dict(a)
3.2)Используя функцию zip: # если длина списков будет разной, то лишнее просто не будет учитываться в словаре
a = ['a', 'b', 'c']
b = [1, 2, 3]
d = dict(zip(a, b))
3.3) С помощью генераторов  (comprehensions): # если длина списков будет разной, то лишнее просто не будет учитываться в словаре
a = ['a', 'b', 'c']
b = [1, 2, 3]
d = {
    i_a: i_b
    for i_a, i_b in zip(a, b)
}
4) Четвертый способ:
q=dict.fromkeys(['a','b','c'],100)

5) Пустой словарь:
t={}
или:
t=dict() # так правильнее

6) Обращение к ключу:
1: 495,
2: 812,
3: 8412
print(d[3])
d[4]='four' - добавляется новый ключ

7)Пример
person={}
s= "IVANOV IVAN Samara SGU 5 4 5 5 5 4 3"
s=s.split()
person['lastName']=s[0]
person['firstName']=s[1]
person['city']=s[3]
person['university']=s[3]
person['marks']=[]
for i in s[4:]:
    person['marks'].append(i)
print(person)

8) операции:
del[3] - удалит третий ключ
len(d) - количество пар
2 in d - есть ли 2 в словаре d?
for i in d:
    print(i) - вывод значений ключа
for i in d:
    print(i, d[i]) - вывод пар полностью
9) Методы:
d.clear() - очищает полностью словарь
d.add() - добавляет элемент вконце списка
d.remove() - удаляет элемент вызывая ошибку, если такого нет
d.discard() - удаляет элемент не вызывая ошибок, если такого нет
d.pop() - удаляет элемент и выводит на экран, можно применить в следующем коде
a = d.pop('1')  - переменной присвоиться значение ключа '1'
d['2'] = d.pop('1') - переименовали ключ '1' на ключ '2' - а точнее создали новый с таким же значением
d.keys() - выведет все ключи
d.values() - выведет все значения
1: 495,
2: 812,
3: 8412
d.get()
print(d.get(3)) - получает значение от ключа, т.е выведет 8412
print(d.get(5)) - если такого ключа нет то выведет None по умолчанию
print(d.get(5, 'no such key')) - если такого ключа нет то выведет no such key
print(min(d, key=d.get)) - получит ключ с минимальным значением
if d.get('a', {}).get('b',{}).get('c', {}): - проверяет есть ли значение в ключе 'c' в вложенном словаре d = {'a': {'b': {'c': 'x'}}}

d.setdefault(3) - возвратит значение ключа 3,
если такого ключа нет, то он создаст этот ключ без значения (3: None)
d.setdefault(7,'seven') - если такого ключа нет, то он создаст этот ключ со значением (7: 'seven')
print(d.pop(3)) - выведет значение ключа 3 , но при этом сам ключ со значением будет удален из словаря
print(d.popitem(3)) - удаляется из словаря пары и выводится на экран, с конца словаря
print(d.keys()) - возвращает все ключи словаря
print(d.values()) - возвращает все значения словаря
print(d.items()) - возвращает все пары словаря
print(d.items())
for para in d.items():
    print(para[0],para[1]) - выводится нулевой и первый элемент пары, т.е ключ и значение
for key in d.keys():
    print(key,end='') - выводятся ключи
for key in d():
    print(key,end='') - выводятся ключи
for value in d.values():
    print(value,end='') - выводятся значения
for key, value in d.items():
    print(key,value) - выводится ключ и значение пары, т.е ключ и значение
d.update(d_other) - позволяет дополнять данные словаря или обновлять их (в аргументе должен быть другой словарь)

from string import ascii_lowercase
d={}
for i in ascii_lowercase:
    print(d[i])
    d[i]=i+1
for para in d.items():
    print(para[0],para[1])

n = list((input().lower()).split())
for i in range(len(n)):

Сортировка Словарей:

for i in sorted(dict):           - сортировка словаря по ключам
    print(i, dict[i])

for i in sorted(dict.values()):          - сортировка по значениям (вывод без ключей)
    print(i)

for i in sorted(dict.items(),key=lambda para: para[1]):   - сортировка по значениям, вывод с ключами
    print(i)

for i in sorted(dict.items(),key=lambda para: (para[1],para[0])):   - сортировка по значениям, затем пары с совпадающими значениями сортируются по ключам
    print(i)

for i in sorted(dict.items(),key=lambda para: (-para[1],para[0])):   - сортировка по значениям в обратном порядке(если это цифры), затем пары с совпадающими значениями сортируются по ключам в обычном порядке
    print(i)

import collections # у этого модуля есть собственный словарь, который запоминает позиции и позволяет работать с сортировкой
d = {} # обычный словарь
d = collections.OrderedDict() # словарь модуля collections

Пример:
book = {}
for _ in range(int(input())):
    phone, name = input().split()
    book[name] = book.get(name, []) + [int(phone)]
for _ in range(int(input())):
    print(*book.get(input(), ['Неизвестный номер']))

Вложенный словарь:
1)
dict={ключи1: {ключи2: значения2}}
list=[ключи]
for i in list:
    print(i,dict[i][ключ2.1])  - вывод ключей1 и каких то значений из ключей2
    ключ2.1=dict[i][ключ2.1]
    ключ2.2=dict[i][ключ2.2]
    ключ2.3=dict[i][ключ2.3]
    print(ключ2.1,ключ2.2,ключ2.3) - вывод ключей1  и значений по определенным ключам2 - ключ2.1,ключ2.2,ключ2.3

2)
dict={ключи1: {ключи2: значения2}}
list=[ключи]
for i in list:
    print(i)
    for j in dict[i]:
        print(j, dict[i][j]) - вывод ключей1, ключей2 и их значений

    Генераторы словарей  # key:value
1)
a={}
for i in range(1,11):
    a[i] == i**2
print(a)
# генератор такого словаря будет следующим:
a = {i:i**2 for i in range(1,11)} #здесь key = i, а value = i**2
print(a) # выведет {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

2)
a = {word:len(word) for word in ['hello', 'hi', 'www']}
print(a) # выведет {'hello': 5, 'hi': 2, 'www': 3}

3)
data = {
    'Джефф Безос':'177' 
    'ИлоН МаСк':'126',
    'бернар АрнО':'150',
    'БиЛл ГейтС':'124',
}
new_data = {key.title():int(value) for key, value in data.items()}
print(data) # выведет {'Джефф Безос': '177', 'ИлоН МаСк': '126', 'бернар АрнО': '150', 'БиЛл ГейтС': '124'}
print(new_data) # выведет {'Джефф Безос': 177, 'Илон Маск': 126, 'Бернар Арно': 150, 'Билл Гейтс': 124}

4)
users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [3, 'username', '1234'],
    [51, 'qwerty','1234'],
]
new_users = {user[0]:user for user in users}
print(new_users)  # выведет {0: [0, 'Bob', 'password'], 1: [1, 'code', 'python'], 2: [2, 'Stack', 'overflow'], 3: [3, 'username', '1234'], 51: [51, 'qwerty', '1234']}

# Поменять местами ключи и значения
{word_id:word for (word,word_id) in namt_dict.items()} # меняем в нашем словаре ключи со значениями
