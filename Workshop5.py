#-----------------------------------------Семинар 5 задание 1-----------------------------------------#
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

some_text = "sometext абв 321 текст абв112122 оовыфащшабввыф"
words = some_text.split(" ")
words = [word for word in words if not 'абв' in word]
text_without_word = " ".join(words)
print(text_without_word)

#-----------------------------------------Семинар 5 задание 2-----------------------------------------#
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# import random as r
# player_1 = input("Введите имя первого игрока: ")
# player_2 = input("Введите имя второго игрока: ")
# queue_turn = r.randint(1,3)
# total_candys = 121
# candys_in_turn = 28
# if queue_turn == 1: print(f'Первый ход делает {player_1}. Нельзя брать больше 28 конфет!')
# else: print(f'Первый ход делает {player_2}. Нельзя брать больше 28 конфет!')
#
# while total_candys > 0:
#     if queue_turn == 1:
#         candys_in_turn = int(input(f'Осталось {total_candys} конфет. {player_1}, сколько конфет ты возьмешь? :'))
#         if candys_in_turn <= 28:
#             total_candys -= candys_in_turn
#             queue_turn = 2
#         else:
#             print(f'{player_1}, можно брать не больше 28 конфет!')
#             candys_in_turn = 1
#     if queue_turn == 2:
#         candys_in_turn = int(input(f'Осталось {total_candys} конфет. {player_2}, сколько конфет ты возьмешь? :'))
#         if candys_in_turn <= 28:
#             total_candys -= candys_in_turn
#             queue_turn = 1
#         else:
#             print(f'{player_1}, можно брать не больше 28 конфет!')
#             candys_in_turn = 1
#     if total_candys <= 28:
#         if queue_turn == 1:
#             print(f'Осталось {total_candys} конфет. {player_1} забирает их и выигрывает!')
#             break
#         else:
#             print(f'Осталось {total_candys} конфет. {player_2} забирает их и выигрывает!')
#             break

#-----------------------------------------Семинар 5 задание 3-----------------------------------------#
# Создайте программу для игры в ""Крестики-нолики"".

#       0_o

#-----------------------------------------Семинар 5 задание 4-----------------------------------------#
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('text_words.txt', 'r') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()

print(my_txt)

def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond

txt_compr = file_encod(my_txt)
with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')
print(txt_compr)