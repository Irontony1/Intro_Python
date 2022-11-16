from Writing import txt_write
from Writing import csv_write
from Writing import html_write
from Reading import open_csv
from Reading import open_txt
from Reading import open_html

def main_run():
    total_command = input('Введите "W", чтобы добавить контакт. Или "R", чтобы постотреть телефонную книгу: ')

    if total_command == 'W':
        command_write = input('Введите формат записи (.txt / .csv / .html): ')
        if command_write == 'txt':
            txt_write()
        elif command_write == 'csv':
            csv_write()
        elif command_write == 'html':
            html_write()

    elif total_command == 'R':
        command_read = input('Введите формат просмотра (.txt / .csv / .html): ')
        if command_read == 'txt':
            open_txt()
        elif command_read == 'csv':
            open_csv()
        elif command_read == 'html':
            open_html()
    else: 
        print('Неверная команда')

main_run()
