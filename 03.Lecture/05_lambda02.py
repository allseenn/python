# open file.txt read 1 2 3 5 8 15 23 38
# calculate end print tuples with number and its power 2
with open('file.txt', 'r', encoding='utf-8') as file:
    data = file.read().split()

print([(int(i), (lambda i: i**2)(int(i))) for i in data if int(i) % 2 == 0])
