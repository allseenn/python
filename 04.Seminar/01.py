# 1. Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
from sympy import *
from sympy.plotting import plot
from sympy.solvers.inequalities import solve_univariate_inequality
# init_printing(use_unicode=False, wrap_line=False, no_global=True)

x = Symbol('x')
y = Symbol('y')
# x = -1.038
# y = 3**0.5
t = (2*x + 3*y)**2 - 3*x*(4/3*x+4*y)
simplify(t)
f = 4*x**4-65*x**2+16
solve(f)
