from Writing import txt_write
from Reading import open_xlsx
from Reading import open_html

def main_run():
    total_command = input('Чтобы добавить новый контакт - введите "add", чтобы посмотреть справочник - введите "view" ')

    if total_command == 'add':
        txt_write()

    elif total_command == 'view':
        command_read = input('Введите формат просмотра (.xlsx / .html): ')
        if command_read == 'xlsx':
            open_xlsx()
        elif command_read == 'html':
            open_html()
    else: 
        print('Неверная команда')

main_run()
