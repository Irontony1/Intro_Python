#-----------------------------------------Семинар 2 задание 1-----------------------------------------#
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# float_value = input('Введите число с плавающей запятой: ')
# sum_elements = 0
# for i in float_value:
#     if i != ',' and i != '.':
#         sum_elements += int(i)
#
# print(f'Сумма элементов введенного числа = {sum_elements}')

#-----------------------------------------Семинар 2 задание 2-----------------------------------------#
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число: '))
# mul = 1
# factorial_list = []
# for i in range(1, number+1):
#     mul *= i
#     factorial_list.append(mul)
# print(factorial_list, sep=',')

#-----------------------------------------Семинар 2 задание 3-----------------------------------------#
# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

number = int(input('Введите число: '))
result = 0
sum_value = 0
output_list = []
for i in range(1, number+1):
    result = (1 + (1 / i)) ** i
    sum_value += result
    output_list.append(f'{i}: {round(result,2)}')
print(output_list, sep=',')
print(f'Сумма последовательности чисел равна = {round(sum_value,2)}')