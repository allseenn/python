# Д/з 3, Задача 1. Улучшение
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random
# length = random.randrange(5,10)
# my_list = []
# count = 0
# while(count <= length):
#     my_list.append(random.randint(0,10))
#     count += 1
# print(my_list, end=" -> ")
# summa = 0
# count = 0
# print("odd indexes has values", end=" ")
# for i in my_list:
#     if count % 2 != 0:
#         print(f"{i},", end=" ")
#         summa += i
#     count += 1
# print(f"sum is: {summa}")
import random
my_list = [random.randint(0,9) for x in range(random.randint(5,10))]
odd_list = [x for n, x in enumerate(my_list) if n % 2 != 0] 
print(f'{my_list} => odd indexes has values {" и ".join(map(str, odd_list))}, sum is {sum(odd_list)}') 