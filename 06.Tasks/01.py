# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
import random
# generate random words from syllables
syllables = ["ма", "за", "ба", "ка", "ша", "бв"]
text = list(map(lambda x: "".join(random.sample(syllables,2)), range(random.randint(14,16))))
print(f' TEXT : {" ".join(text)}')
# search for syllable "абв" and delete it with whole word
parsed_text = list(x for x in text if "абв" not in x)
print(f'PARSED: {" ".join(parsed_text)}')