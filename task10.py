print('Задача 10. За что?')

# Вы встретились со своим старым другом,
# который тоже изучает программирование, правда, в другом учебном заведении.
# За чашкой кофе он пожаловался вам,
# что сумасбродный препод дал им задание написать программу,
# которая из двух введённых чисел определяет наибольшее,
# не используя при этом условных операторов, циклов и встроенную функцию max.
#
# Радуясь, что на вашем курсе такого не требуют,
# вы всё-таки решаете помочь своему другу.
#
# Напишите для него эту программу.
#
# Пример:
#
# Введите первое число: 10
# Введите второе число: 5
#
# Наибольшее число: 10

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второее число: '))

lst = [first_number, second_number]
lst_num = list(enumerate(lst, 0))

result = first_number + second_number - (min(lst_num, key=lambda i: i[1]))[1]
print('Наибольшее число: ', result)
