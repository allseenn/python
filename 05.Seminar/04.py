# # 4. Задана натуральная степень k. 
# # Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# #  многочлена и записать в файл многочлен степени k.
# #     *Пример:* 
# #     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k=int(input("введите   k:"))
# res=open("rezout.txt","w")
# for i in range(3): # в файл повторить так 3 раза...
#   rezstr=""# пустая строка для строки в файл.
#   for j in range(0,k): # строим многочлен
#     koef=randint(0,10)
#     if koef>0: # т.е. множитель не равен 0
#       #собираем строку согласно "правописанию"
#       if j==0: # это на тот случай если степень равна 0
#           rezstr=str(koef)
#       elif j==1:#когда степень равна 1
#           if koef>1:
#             rezstr=str(koef)+"*x" +rezstr
#           else:
#             rezstr="x" +rezstr
#       else:#в остальных случаях
#           if koef>1:
#              rezstr=str(koef)+"*x**"+str(j)+rezstr
#           else:
#              rezstr="x**"+str(j)+rezstr
#       rezstr="+"+rezstr
#       # в принципе этот фрагмент можно было положить в функцию, но слишком эта простая ...
#   if rezstr[0]=="+":#убираем слева плюс в строке
#         rezstr=rezstr[1:]
#   res.writelines(rezstr+"\n");     print(rezstr)
# res.close
import random

def generate_superscript(x, n):
    if n == 0:
        return str(x)
    if n == 1:
        return str(x)+"x"
    superscript = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    result = str(x)
    if x != 0:
        result += "x"
    for i in str(n):
        result += superscript[int(i)]
    return result

def generate_polynomial(k):
    result = []
    for i in range(k, -1, -1):
        coefficient = random.randint(0, 100)
        if coefficient != 0:
            result.append(generate_superscript(coefficient, i))
    return "+".join(result)


print(generate_polynomial(10))
