def concantinatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res


print(concantinatio('a', 's', 'd', 'w'))
print(concantinatio('a', '1'))
#print(concantinatio(1, 2, 3, 4))
