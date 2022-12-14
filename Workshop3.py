#-----------------------------------------Семинар 3 задание 1-----------------------------------------#
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

# some_list = []
# for _ in range(1,random.randint(2,10)):
#     some_list.append(random.randint(1,100))
#
# print(f'Исходный список - {some_list}')
# sum = 0
# for i in range(len(some_list)):
#     if i % 2 != 0:
#         sum += some_list[i]
# print(f'Сумма нечетных позиций = {sum}')

#-----------------------------------------Семинар 3 задание 2-----------------------------------------#
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# some_list = []
# output_list = []
# for _ in range(1,random.randint(2,10)):
#     some_list.append(random.randint(1,100))
# print(f'Исходный список - {some_list}')
#
# size = len(some_list)
# for i in range(size-(size//2)):
#     output_list.append(some_list[i]+some_list[size-i-1])
# print(f'Список сумм - {output_list}')

#-----------------------------------------Семинар 3 задание 3-----------------------------------------#
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов. Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# some_list = []
# min = 1
# max = 0
# for _ in range(1,random.randint(2,10)):
#     some_list.append(round(random.random()*100,random.randint(1,4)))
# print(f'Исходный список - {some_list}')
#
# for i in range(len(some_list)):
#     if (some_list[i] - int(some_list[i])) > max:
#         max = some_list[i] - int(some_list[i])
#
#     if (some_list[i] - int(some_list[i])) < min:
#         min = some_list[i] - int(some_list[i])
#
# print(f'Разница = {round(max-min,4)}')

#-----------------------------------------Семинар 3 задание 4-----------------------------------------#
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# dec_number = int(input('Введите десятичное число '))
#
# def dec_to_bin(dec_number):
#     if dec_number >= 1:
#         number = dec_number//2
#         ost = dec_number % 2
#         return dec_to_bin(number) + str(ost)
#     else:
#         return 'В двоичном формате '
#
# print(dec_to_bin(dec_number))

#-----------------------------------------Семинар 3 задание 5-----------------------------------------#
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# number = int(input('Введите индекс чисел Фибоначчи '))
# fibonacci_list = []
# def fibonacci(n):
#     if n >= 1:
#         if n in (1, 2):
#             return 1
#         return fibonacci(n - 1) + fibonacci(n - 2)
#     elif n <= -1:
#         return fibonacci(n + 2) - fibonacci(n + 1)
#     else:
#         return 0
# for i in range(-number,number+1):
#     fibonacci_list.append(fibonacci(i))
# print(fibonacci_list)
#-----------------------------------------Семинар 3 задание 6-----------------------------------------#
# Сгруппировать слова по общим буквам.["eat","tea","tan","ate","nat","bat"]
# [["eat","tea","ate"]["tan","nat"]["bat"]]

def group_words(words):
    result = []
    words_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if not sorted_word in words_dict.keys():
            words_dict[sorted_word] = []
        words_dict[sorted_word].append(word)
    for key, value in words_dict.items():
        result.append(value)
    return result


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_words(input_list)
print(f"input: {input_list}")
print(f"output: {output}")

