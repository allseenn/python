list1 = [1, 2, 3, 4, 5]
list2 = list1
list2[0] = 123
for e in list1:
    print(e)

print()

for e in list2:
    print(e)
