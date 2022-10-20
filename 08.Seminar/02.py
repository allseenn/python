my_dict = {3:'Иванов', 1: 'Васльев', 4:'Петров'}


for elem in sorted(my_dict):
    print(elem)
    print(elem, my_dict[elem])
    
for key, value in sorted(my_dict.items()):
    print(key, value)

print(my_dict)
print(sorted(my_dict))
print(my_dict.items())
print(type(my_dict.items()))
print(sorted(my_dict.items()))
print(my_dict.keys())
print(sorted(my_dict.keys()))
print(my_dict.values())
print(sorted(my_dict.values()))

my_list = [(1, 'a', True),(2, 'b', False),(3, 'x', True)]
for first, second, third in my_list:
    print(first)
    print(second)
    print(third)
    print()
    print('Следующй цилк')
