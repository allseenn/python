# zip ([1, 2, 3], [a, b, c], [а, б, в])
# [(1, a, a), (2, b, б), (3, c, в)]
user = ["user1", "user2", "user3"]
id = [1,2,3]
print(list(zip(user, id)))