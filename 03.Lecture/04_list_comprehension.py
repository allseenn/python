# [exp for item in iterable] iterable - list, dict, range
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]
# make list from 1 to 100 with odd numbers
list = []
for i in range(1, 101):
    if i%2 == 0:
        list.append(i)
print(list)

list_comprehension = [i for i in range(1, 101) if i%2 == 0]
print(list_comprehension)

list_tuples = [(i, i) for i in range(1, 101) if i%2 == 0]
print(list_tuples)

f = lambda i: i**3
list_lambda = [(i, f(i)) for i in range(1, 101) if i%2 == 0]
print(list_lambda)