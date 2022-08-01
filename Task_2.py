# Задача_2
#  Найти сумму чисел списка стоящих на нечетной позиции

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 
# 3 и 9, ответ: 12
 
# def sum_of_elements():
#     list = [2,3,5,9,3]
#     print(list)
#     positions = f'на нечётных позициях элементы {list[1: :2]}'
#     s = f'ответ: {sum(list[1: :2])}'
#     return positions,s 
   
# print(sum_of_elements())

nums = [2, 3, 5, 9, 3]

res = sum(list(map(lambda nums: nums, nums[1::2])))
#res = sum(list(filter(lambda nums: nums, nums[1::2]))) # так тоже работает.

print(f'{nums} -> {nums[1::2]} -> {res}')



result = sum(nums[1::2])
print(result)
