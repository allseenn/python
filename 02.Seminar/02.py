# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.  
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
number = input("Введите число N: ")
result = []
for i in range(1, int(number)+1):    
    elem = [i, 3*i + 1]
    result.append(elem)
print(result)
print(dict(result))
