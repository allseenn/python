def f(x):
    return (1 + 1 / x)**x
i = 1
summa = 0
while(i < 10):
    summa += round(f(i))
    print(summa, end=" ")
    i += 1
