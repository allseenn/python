# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
n = int(input("Give quarter number: "))
if n == 1:
    print("(x > 0; y > 0)")
elif n == 2:
    print("(x < 0; y > 0)")
elif n == 3:
    print("(x < 0; y < 0)")
elif n == 4:
    print("(x > 0; y < 0)")
else:
    print("No such quarter")