# Задача 5. Реализуйте алгоритм перемешивания списка.
size = int(input("Enter a list size: "))
numbers = list(range(size))
print(numbers, end = " ")
temp = 0
for i in numbers:
    temp = numbers[i]
    numbers.pop(i)
    numbers.append(temp)
print(numbers, end=" ")