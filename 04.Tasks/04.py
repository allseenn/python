# Задача 4. Задана натуральная степень k. 
#  случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

def small_power(x):
    digit_power = ""
    unicode_numbers = {
        "0": "\u2070",
        "1": "\u00B9",
        "2": "\u00B2",
        "3": "\u00B3",
        "4": "\u2074",
        "5": "\u2075",
        "6": "\u2076",
        "7": "\u2077",
        "8": "\u2078",
        "9": "\u2079",
    }
    for i in str(x):
        digit_power += unicode_numbers[i]
    return digit_power

my_power = int(input("Enter any power number: "))
my_dict = {}
for i in range(my_power+1):
    my_dict[i] = randint(0,100)
count = len(my_dict)-1
print(f"Power: Coefficient list {my_dict}")
file_data = "k="
file_data += str(my_power) + " => "
while count >= 0:
    if my_dict[count] != 0 and count != 0  and count != 1:
        file_data += str(my_dict[count]) + "*x" + small_power(count) + " + "
    elif my_dict[count] == 0:
        file_data += ""
    elif count == 1:
       file_data += str(my_dict[count]) + "*x + "
    elif count == 0:
       file_data += str(my_dict[count]) + ""
    count -= 1
file_data += " = 0"
print(file_data)

with open('file.txt', 'a', encoding='utf-8') as file:
    file.writelines(file_data)
    file.writelines("\n")
print("Polynomial added to file.txt")