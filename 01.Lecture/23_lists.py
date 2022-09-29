numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers = list(range(1,4))
print(numbers)
numbers[0] = 10
print(numbers)

for i in numbers:
    i *= 2
    print(i)
print(numbers)