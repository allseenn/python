# 34. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
with open('rez01.txt', 'w') as file:
    file.write('3*x**8+9*x**7+3*x**6+3*x**5+8*x**4+3*x**3+10*x**2+2*x+4')
with open('rez02.txt', 'w') as file:
    file.write('6*x**8+10*x**7+7*x**5+10*x**4+7*x**3+5*x**2+10')
with open('rez01.txt','r') as file:
    o_1 = file.readline()
    l_1 = o_1.split()
with open('rez02.txt','r') as file:
    o_2 = file.readline()
    l_2 = o_2.split()
print(f'{l_1} + {l_2}')
sum_poly = l_1 + l_2
with open('sum_rez.txt', 'w') as file:
    file.write(f'{l_1} + {l_2}')

