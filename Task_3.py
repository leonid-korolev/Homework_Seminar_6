# Задача_3
# Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from functools import reduce

def get_number():
    while True:
        try:
#            print('Введите координаты первой точки через пробел')
#            A = print(f'A(x,y) =  {map([float(i) for i in input() .split()])}')
#            A = print(f'A(x,y) =  {list(map(float,input().split()))}')
            print('Введите координаты первой точки: ')
            A = list(map(float,input('A(x,y) = ').split()))
            print('Введите координаты второй точки: ')
            B = list(map(float,input('B(x,y) = ').split()))
            return A, B 
                  
        except ValueError:
            print('Некорректный ввод')

A,B = get_number()
AB = reduce(lambda A, B: (A + B)**(1/2),(map(lambda A: (A[1] - A[0])**2, zip(A, B))))

print(f'Расстояние между точками А и В = {round(AB,2)}')
