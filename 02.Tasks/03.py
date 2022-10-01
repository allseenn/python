# Задача 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
number = int(input('Enter a number: '))
mylist = []
dictionary = {}
n = 1
for i in range(number + 1):
    mylist.append(round((1 + 1 / n)**n, 4))
    summa = 0
    for j in mylist:
        summa += round(j)
    dictionary[i] = summa
    n += 1
print(f"List for n = {number}: {mylist}")
print(f"Sums for n = {number}: {dictionary}")
