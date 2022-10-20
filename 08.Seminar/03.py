my_dict = {'три':'Иванов', 'один': 'Васильев', 'четыре':'Петров', 'шесть': 'Иванов'}
print(my_dict)

my_dict['два'] = my_dict.pop('четыре')
print(my_dict)

my_dict['три'] = my_dict['три'] + ' ' + my_dict.pop('один')
print(my_dict)

my_dict[0] = 'Привет)'
print(my_dict)

print(my_dict[1])
