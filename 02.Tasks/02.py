# Задача 2. Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
summa = 1
number = int(input("Enter a natural number: "))
mylist = [1]
mytuple = ("1", )
if number == 0:
    print("Nothing to multiply")
    exit()
for i in range(2, number + 1):
    summa *= i
    mylist.append(summa)
    mytuple = mytuple + (mytuple[i - 2] + "*" + str(i), )
print(f"If N = {number}, then {mylist} {mytuple}")
