# python -m venv .pip
# from os import system
# system('pip install -r requirements.txt')
# system('pip freeze > requirements.txt')

from isOdd import isOdd
print(isOdd(1)) # true
print(isOdd(5)) # true

print(isOdd(0)) # false
print(isOdd(4)) # false