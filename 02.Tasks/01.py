# Задача 1. Напишите программу, которая принимает
# на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
summa = 0
number = str(input("Enter a real number: "))

if number[0] == "-":
    number.pop(0)
for digit in number:
    if (digit == "," or digit == "."):
        digit = 0
    summa = summa + int(digit)

print(f"{number} -> {summa}")
