# Д/з 3. Задача 5. Улучшение
# # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# # Пример:
# # # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# number = int(input("Enter a number: "))
# my_list = [0]
# count = 1
# if number > 0:
#     my_list = [1, 0, 1]
# while(count < number):
#     my_list.append(my_list[len(my_list)-1] + my_list[len(my_list)-2])
#     if count % 2 == 0:
#         my_list.insert(0, my_list[len(my_list)-1])
#     else:
#         my_list.insert(0, -my_list[len(my_list)-1])
#     count += 1
# print(my_list)

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     else:
#      return (fibonacci(n - 1) + fibonacci(n - 2))
# print(fibonacci(3))
# #print([fibonacci(x) for x in range(6)])
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
fib_list = [fib(x) for x in range(int(input("Enter a number: "))) if x > 0] 
print(list([i for sublist in [list(z) for z in zip(reversed([-x for n, x in enumerate(fib_list) if n%2==1]),reversed([x for n, x in enumerate(fib_list) if n%2==0]))] for i in sublist]) + [0] + fib_list)
