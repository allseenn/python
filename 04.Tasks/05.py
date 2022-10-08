# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
from random import randint
# Function reads given file
def cat_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        big_data = file.read()
    return big_data
# Function reads given file and parse it to dict
def read_file(filename):
    file_data = ""
    with open(filename, 'r', encoding='utf-8') as file:
        file_data = file.read()
    file_data = file_data.split(" + ")
    my_dict = {}
    for i in file_data:
        if i.isdigit():
            my_dict[""] = int(i)
        elif i.__contains__("x"):
            my_dict[i[1:]] = int(i[0:1])
    return my_dict
# Function makes powers sign as in algebra = x⁴
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
# Function generate random polynomial from 2 till 9
def polynomial():
    my_power = randint(2, 9)
    my_dict = {}
    for i in range(my_power+1):
        my_dict[i] = randint(0,9)
    count = len(my_dict)-1
    file_data = ""
    while count >= 0:
        if my_dict[count] != 0 and count != 0  and count != 1:
            file_data += str(my_dict[count]) + "x" + small_power(count) + " + "
        elif my_dict[count] == 0:
            file_data += ""
        elif count == 1:
            file_data += str(my_dict[count]) + "x + "
        elif count == 0:
            file_data += str(my_dict[count]) + ""
        count -= 1
    return file_data
# Creating 2 files with random polynomials
with open('file1.txt', 'w', encoding='utf-8') as file:
    file.writelines(polynomial())
with open('file2.txt', 'w', encoding='utf-8') as file:
    file.writelines(polynomial())
# read and parse 2 files
data1 = read_file("file1.txt")
data2 = read_file("file2.txt")
# make set of powers from 2 files
power_set=sorted(set(list(data1.keys())+list(data2.keys())), reverse=1)
# combine and calculate all sets
data3 = {}
for i in power_set:
    try:
        data3[i] = data1[i]+data2[i]
    except KeyError:
        try:
            data3[i] = data1[i]
        except KeyError:
            data3[i] = data2[i]
# from dictionary to string for file3.txt
data3_string = ""
for i in data3:
    if i == "":
        data3_string += str(data3[i]) + str(i) + " = 0"
    else:
        data3_string += str(data3[i]) + str(i) + " + "
# write last file3.txt with sum of polynomials
with open('file3.txt', 'w', encoding='utf-8') as file:
    file.writelines(data3_string)
# Print contents of three files for Reviewer performance :))
print(f'file1.txt: {cat_file("file1.txt")}')
print(f'file2.txt: {cat_file("file2.txt")}')
print(f'file3.txt: {cat_file("file3.txt")}')