def sum(x, y):
    return x + y

def mult(x, y):
    return x * y

def calc(op, x, y):
    return op(x, y)

print(calc(sum, 2, 2))
print(calc(mult, 2, 2))