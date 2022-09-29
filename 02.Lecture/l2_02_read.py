path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
