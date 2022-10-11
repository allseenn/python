## Групповая работа [2]
# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.  
#     *Пример:*  
#     2+2 => 4; 
#     1+2*3 => 7; 
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.    
#         *Пример:*     
#         1+2*3 => 7;      
#         (1+2)*3 => 9;
Исправленный Итоговый вариант:
def calc(my_list):
    i = 1

    while '*' in my_list or '/' in my_list:
        if my_list[i] == '*':
            my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        elif my_list[i] == '/':
            my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        else: i += 1    

    i = 1

    while '+' in my_list or '-' in my_list:
        if my_list[i] == '+':
            my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        elif my_list[i] == '-':
            my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        else: i += 1
    print('Выводим из функции результат:', my_list)
    return my_list

my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
my_list_out = list(my_text)
print(my_list_out)

while '(' in my_list_out:
    bracket_left = my_list_out.index('(')
    bracket_right = my_list_out.index(')')
    my_list_out = my_list_out[:bracket_left] + calc(my_list_out[bracket_left + 1 : bracket_right]) + my_list_out[bracket_right + 1 :]

print(my_text + '=>' + str(calc(my_list_out)[0]))

