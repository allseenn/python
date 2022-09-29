# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.
size = int(input("Enter a natural number: "))
numbers_list = list(range(-size, size+1))
path = 'file.txt'
data = open(path, 'r')
sum = 1
for position in data:
    sum *= numbers_list[int(position)]
data.close()
print(numbers_list)
print(sum)