# 5. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
from math import sqrt
print("To find distance between 2 point\n Enter their coordinates (x; y)\n Two numbers inline seperated by comma")
a = [float(a) for a in input("Enter coordinates for A: ").split(sep=",")]
b = [float(b) for b in input("Enter coordinates for B: ").split(sep=",")]
print("%.2f" % (sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)))