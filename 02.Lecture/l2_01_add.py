color = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(color)
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
