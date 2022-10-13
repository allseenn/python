# def f(x):
#     return x + 10
# map(f, [1, 2, 3 , 4, 5])
# [11, 12, 13, 14, 15]
li = [x for x in range(1, 20)]
print
list = map(lambda x:x+10, li)
print(*list)

print(*map(lambda x:x+10, [x for x in range(1,20)]))
