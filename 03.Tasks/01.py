# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

length = random.randrange(5,10)
my_list = []
count = 0
while(count <= length):
    my_list.append(random.randint(0,10))
    count += 1
print(my_list, end=" -> ")
summa = 0
count = 0
print("odd elements has indexes", end=" ")
for i in my_list:
    if count % 2 != 0:
        print(f"{i},", end=" ")
        summa += i
    count += 1
print(f"sum is: {summa}")