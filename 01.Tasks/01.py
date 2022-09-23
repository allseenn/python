# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
number = int(input("Is a number weekend: "))
if number == 6 or number == 7:
    print("Yes")
elif number <= 0 or number > 7:
    print("No such weekday")
else:
    print("No")
