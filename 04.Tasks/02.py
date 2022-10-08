# Задача 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
number = int(input("Enter natural number: "))
if number == 0:
    print("You entered not natural number!")
    exit()
elif number == 1:
    full_list = []
elif number > 1:
    full_list = [2] 
count = 2
simple = 1
while count <= number:
    simple = 1
    for i in full_list:
        if count % i == 0:
            simple = 0
    if simple == 1:
        full_list.append(count)
    count += 1
full_list.insert(0,1)
print(full_list)

multipliers = ""
divided = number
for i in full_list:
    if i == 1:
        multipliers += str(i)
    else:
        while divided % i == 0:
            multipliers += " * "+str(i)
            divided /= i
print(f"{multipliers} = {number}")