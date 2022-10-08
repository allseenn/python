# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤ 10^{-10}$
#
def decimal(x):
    count = 0
    while (x != 1):
        x *= 10
        count += 1
    return count

MY_PI = 104348/33215
accuracy = float(input("Enter accuracy from 0.1 till 0.0000000001: "))
print(f"if d = {accuracy:.{decimal(accuracy)}f}, π = {MY_PI:.{decimal(accuracy)}f}")