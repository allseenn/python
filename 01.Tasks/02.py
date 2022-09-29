# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
# print("Lets check for truth ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
# x = input("Give X: ")
# y = input("Give Y: ")
# z = input("Give Z: ")
# if not(x or y or z) == (not x and not y and not z):
#     print(True)
# else:
#     print(False)
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)
