# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

length = random.randrange(5,10)
my_list = []
count = 0
while(count <= length):
    my_list.append(random.randint(0,9))
    count += 1
print(my_list, end=" => ")
sum_list = []
count = 0
while(count <= length):
    sum_list.append(my_list[count] * my_list[length])
    count += 1
    length -= 1
print(sum_list)
