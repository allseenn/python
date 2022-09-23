# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x = int(input("Give  X: "))
y = int(input("Give  Y: "))
if x > 0 and y > 0:
    print("Quarter: 1")
elif x < 0 and y > 0:
    print("Quarter: 2")
elif x < 0 and y < 0:
    print("Quarter: 3")
elif x > 0 and y < 0:
    print("Quarter: 4")
elif x == 0 or y == 0:
    print("Coordinate line")
elif x == 0 and y == 0:
    print("Coordinate center")