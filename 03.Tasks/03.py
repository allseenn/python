# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

length = random.randrange(5,9)
my_list = []
count = 0
while(count <= length):
    my_list.append(round(random.randrange(0,99) + random.random(),2))
    count += 1
print(my_list, end=" => ")
max = 0
min = 1
for i in my_list:
    if i % 1 > max:
        max = i % 1
    if i % 1 < min:
        min = i % 1
print(round(max - min, 2))