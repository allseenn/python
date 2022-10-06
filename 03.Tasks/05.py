# # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# # Пример:
# # # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
number = int(input("Enter a number: "))
my_list = [0]
count = 1
if number > 0:
    my_list = [1, 0, 1]
while(count < number):
    my_list.append(my_list[len(my_list)-1] + my_list[len(my_list)-2])
    if count % 2 == 0:
        my_list.insert(0, my_list[len(my_list)-1])
    else:
        my_list.insert(0, -my_list[len(my_list)-1])
    count += 1
print(my_list)

# # рекурсия тормозит нещадно после 40
# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# from datetime import timedelta
# from time import time
# import time
# start_time = time.time()

# def fibonacci(n):
#     first, second = 0, 1
#     fibonacci_num = 0
#     for i in range(n):
#         fibonacci_num = first + second
#         second = first
#         first = fibonacci_num
#     return fibonacci_num


# def negative_fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2


# set_number = (input("Введите число: "))
# while not set_number.isdigit():
#     set_number = (input("Введите еще раз: "))
# set_number = int(set_number)
# list = [0]

# for i in range(1, set_number + 1):
#     list.append(fibonacci(i))
#     list.insert(0, negative_fibonacci(i))
# print(list)

# seconds = time.time() - start_time
# print('Time Taken:', time.strftime("%H:%M:%S",time.gmtime(seconds)))

# from math import pow

# def is_int(number):
#     return number.isdigit()

# def function(number):
#     if number in (1, 2): 
#         return 1
    
#     return function(number - 1) + function(number - 2)

# number = None

# while not is_int(str(number)):
#     number = input(«Input number:»)

# number = int(number)

# result = list()
# for i in range(-number, number + 1):
#     if i != 0: 
#         result.append(int(pow(i / abs(i), i + 1) * function(abs(i))))
#     else:
#         result.append(0)

# print(result)
# k = int(input('Введите число: '))
# print(k)
# nego = [1,-1]
# fibo = [1,1]
# for i in range(2,k):
#     lst_fibo = fibo[i-1]+fibo[i-2]
#     fibo.append(lst_fibo)
# for x, elem in enumerate(fibo, 2):
#     if x % 2 != 0:
#         lst_nego = elem * -1
#         nego.append(lst_nego)
#     else:
#         nego.append(elem)
# nego.reverse()
# nego.append(0)
# print(nego+fibo)
