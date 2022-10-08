# Задача 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint
my_list = []
for i in range(randint(7,17)):
    my_list.append(randint(0,10))
print(my_list)
print(set(my_list))