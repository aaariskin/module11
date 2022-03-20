print('Задача 9. Уравнение')

# Даны действительные коэффициенты a, b, c,
# при этом a≠0.
# Решите квадратное уравнение ax^2+bx+c=0 и выведите все его корни.
#
# Если уравнение имеет два корня,
# выведите два корня в порядке возрастания,
# если один корень — выведите одно число,
# если нет корней — не выводите ничего

import math

while True:
    a = float(input('Введите a: '))
    if a != 0:
        break
b = float(input('Введите b: '))
c = float(input('Введите c: '))

discr = math.pow(b, 2) - 4 * a * c
if discr >= 0:
    print(f'x1 = {round((-b+math.sqrt(discr))/(2*a), 2)}')
if discr > 0:
    print(f'x2 = {round((-b-math.sqrt(discr))/(2*a), 2)}')
