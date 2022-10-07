# 1. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# #     *Пример:* 
# # #     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# my_list = [9, 5, 2, 3, 4, 6, 1, 7]
# new_list = [my_list[i] for i in range(len(my_list)-1) if my_list[i] < my_list[i+1] ]
# if new_list[-1] == my_list[-2]:
#     new_list.append(my_list[-1])
# print(new_list)
# nums = [1, 5, 2, 3, 4, 6, 1, 1, 1, 7]
# lst = []
# for i in range(len(nums)):
#     if nums[i] > nums[i-1]:
#         lst = list + nums[i]
# print(lst)
num = [11, 5, 2, 3, 4, 6, 1, 7, 9, 8, 10]

def nextmax(listt):    
    max = listt[0]
    res = [listt[0]]
    for i in range(len(listt)):
        if listt[i] > max:
            max = listt[i]
            res.append(max)
    if len(res) == 1:
        nextmax(listt[1:])
    return res

print(nextmax(num))
