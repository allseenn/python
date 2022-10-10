# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Function to encode given text
def encoding(text):
    code_text = ""
    count = 0
    repetitions = 1
    while count < len(text):
        try:
            if text[count] == text[count+1]:
                repetitions += 1
            elif repetitions == 1:
                code_text += text[count]
            elif repetitions > 1:
                code_text += str(repetitions) + text[count]
                repetitions = 1
        except IndexError:
            if repetitions == 1:
                code_text += text[count]
            elif repetitions > 1:
                code_text += str(repetitions) + text[count]
        count += 1
    return code_text
# Function to decode given cipher
def decoding(cipher):
    decoded_text = ""
    count = 0
    repetitions = 0
    while count < len(cipher):
        if str(cipher[count]).isdigit():
            repetitions = int(cipher[count])
        elif repetitions > 0:
            for x in range(repetitions):
                decoded_text += cipher[count]
                repetitions = 0
        elif repetitions == 0:
            decoded_text += cipher[count]
        count +=1
    return decoded_text
# Text input  
text = input("Enter a text: ")
# Decides encode or decode
numbers_in_text = 0
for num in text:
    if num.isdigit():
        numbers_in_text += 1
# If any digits exists it mean coded text, decoding
if numbers_in_text > 0:
    print(f"Decoding: {decoding(text)}")
# If no digits exists it mean pure text, encoding
else:
    print(f"Encoding: {encoding(text)}")
