# Задача_5
# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math
# Формирование списка целых чисел с проверкой на ввод чисел.

def get_number():
    while True:
        try:
            print('Введите несколько чисел через пробел')
            my_list = [int(i) for i in input() .split()]
            print(my_list)
            return my_list        
        except ValueError:
            print('Вы ввели не числа, повторите ввод')

#nums = get_number()
# # Произведение пар чисел списка.
# def pairs_of_numbers(list: list):
#     new_list = []
#     for i in range(0, (len(list) + 1) // 2):
#         new_list.append(list[i]*list[-i-1])
#     print(new_list)
    
# result = get_number()
#pairs_of_numbers(result)

'''
Решение не нашел. Так выдаёт ошибку, а в чем причина, я сам разобраться не смог.
'''
nums = get_number()
mult_list = list(lambda nums: (nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2)))) 
print(mult_list)








