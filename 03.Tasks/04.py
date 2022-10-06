# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
number = int(input("Enter a number: "))
my_binary = ""
print(f"{number} -> ", end="")
if number == 0:
    my_binary = "0"
while (number > 0):
    if number % 2 == 0:
        my_binary = "0"+ my_binary
    else:
        my_binary = "1"+ my_binary
    number //= 2
print(my_binary)