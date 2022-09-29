colors = {'red', 'green', 'blue'}
print(colors)
# {'red', 'green', 'blue'}
colors.add('red')
print(colors)
# {'red', 'green', 'blue'}
colors.add('gray')
print(colors)
# {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)
# {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red')
# ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()
