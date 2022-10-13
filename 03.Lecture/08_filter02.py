# def f(x)
#     if x%2:
#         return x

# filter(f, [1, 2, 3, 4, 5])
# [2,4]
data = [x for x in range(10)]
res = list(filter(lambda x: x%2==0, data))
print(*res)
