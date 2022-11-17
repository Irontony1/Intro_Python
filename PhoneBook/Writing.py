from os.path import exists
from Creating_head import creating_head
from User_input import get_info as gi
# from Creating_head import creating_html

def txt_write():
    path = 'txt_PhoneBook.txt'
    valid = exists(path)
    if valid != True: creating_head()

    data = gi()
    with open (path, 'a', encoding = 'utf-8') as file:
        file.write(f'{data[0]};{data[1]};{data[2]}\n')


# def html_write():
#     path = 'html_PhoneBook.html'
#     valid = exists(path)
#     if valid != True: creating_html()
    
#     data = gi()
#     with open (path, 'a', encoding = 'utf-8') as file:
#         file.write(f'{data[0]:<30} {data[1]:<15} {data[2]:<50}<br />')
