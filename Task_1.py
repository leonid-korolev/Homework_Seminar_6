# Задача_1
# Определить, присутствует ли в заданном списке строк, некоторое число


txt = 'Мама сшила м0не штаны и7з бере9зовой кор45ы 893.'
print(txt)
txt = txt.split()
txt_1  = list(filter(lambda txt: txt.isalpha(), txt))
print(' '.join(txt_1))