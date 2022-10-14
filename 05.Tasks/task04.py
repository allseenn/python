# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.  


import pickle
# Сжимает файл по алгоритму RLE и сохраняет его в бинарном формате
# сохраняется два списка (1-список символов 2-сколько раз этот символ подряд повторяется)
def compression_rle (in_file: str,  out_file: str):
    with open(in_file, 'r') as file_read_bin, open(out_file, 'wb') as file_write_bin:
        not_compress_file = file_read_bin.readlines()
        compress_file_list = []
        repeat_char_list= []
        for i in range(len(not_compress_file)):
            repeat_char_index = 0
            count_repeat_char = 0
            for j in range(len(not_compress_file[i])):            
                if not_compress_file[i][repeat_char_index] == not_compress_file[i][j]:
                    count_repeat_char += 1
                else:
                    compress_file_list.append(not_compress_file[i][repeat_char_index])
                    repeat_char_list.append(count_repeat_char)
                    repeat_char_index = j
                    count_repeat_char = 1
            else:
                compress_file_list.append(not_compress_file[i][repeat_char_index])
                repeat_char_list.append(count_repeat_char)
        pickle.dump(compress_file_list, file_write_bin)
        pickle.dump(repeat_char_list, file_write_bin)

# Распаковывает файл по алгоритму RLE и сохраняет его в оригинальном виде
# распаковывается два списка (1-список символов 2-сколько раз этот символ подряд повторяется)
def extract_rle (in_file: str, out_file: str):
    with open(in_file, "rb") as file_read_bin, open(out_file, 'w') as file_write:
        compress_list = pickle.load(file_read_bin)
        repeat_list = pickle.load(file_read_bin)
        result_str = ''
        for i in range(len(compress_list)):
            if repeat_list[i] != '\n':
                for j in range(int(repeat_list[i])):
                    result_str += compress_list[i]
            else:
                result_str += '\n'
        file_write.writelines(result_str)


# Заполняем тестовый файл записями 
with open("original.txt", "w") as file:
    file.write('TEST                                                        ' + '\n')
    file.write('     TEST                                                   ' + '\n')
    file.write('          TEST                                              ' + '\n')
    file.write('               TEST                                         ' + '\n')
    file.write('                    TEST                                    ' + '\n')
    file.write('                         TEST                               ' + '\n')
    file.write('WWWWWWWWWWWWWWWWWWWWWWWWW00000000000000000000000000000000000' + '\n')
    file.write('SSSSSSSSSSSSSSSSSS111111111111111111111111TTTTTTTTTTTTTTTTTT' + '\n')
    file.write('444444444444444444444444433333333333333333333333333333333333' + '\n')
    file.write('999999999999999988888888888888888888888877777777777777777777' + '\n')
    file.write('5555555          666666666666             777777777777777777' + '\n')


# Сжимаем файл по алгоритму RLE
compression_rle('original.txt', 'compress.bin')
# Восстанавливаем файл по алгоритму RLE
extract_rle('compress.bin', 'extract.txt')

# Результатом работы программы являются 3 файла: original.txt, compress.bin, extract.txt
