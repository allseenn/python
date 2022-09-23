colors = ["red", "green", "blue"]
for e in colors:
    print(e)
for e in colors:
    print(e*2)

colors.append("gray")
print(colors == ["red", "green", "blue", "gray"])
colors.remove("red")    