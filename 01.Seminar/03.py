# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
n = int(input("Enter number: "))
r = list(range(-n,n+1))
print(r)