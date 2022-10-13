# Д/з 5, Задача 1. Улучшение 
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# import random
# # generate random words from syllables
# syllables = ["ма", "за", "ба", "ка", "ша", "бв"]
# count = 0
# text = []
# while count < random.randint(14,16):
#     text.append("".join(random.sample(syllables, 2)))
#     count += 1
# print(f' TEXT : {" ".join(text)}')
# # search for syllable "абв" and delete it with whole word
# parsed_text = []
# for x in text:
#     if "абв" not in x:
#         parsed_text.append(x)
# print(f'PARSED: {" ".join(parsed_text)}')
import random
syllables = ["ма", "за", "ба", "ка", "ша", "бв"]
text = list(map(lambda x: "".join(random.sample(syllables,2)), range(random.randint(14,16))))
print(*text)
print(*[x for x in text if "абв" not in x])
