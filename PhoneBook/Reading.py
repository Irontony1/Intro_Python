import os
from os.path import exists
from Creating_head import creating_head
from style_xlsx import styling
from openpyxl import Workbook
# from Creating_head import creating_html
# import webbrowser

def open_xlsx():
    path = 'txt_PhoneBook.txt'
    valid = exists(path)
    data_row = []
    if valid != True: creating_head()
    else:
        with open (path, 'r', encoding = 'utf-8') as file:
            for line in file:
                data_row.append(line.strip())
    wb = Workbook()
    ws = wb.active    
    for item in data_row:
        ws.append(item.split(';'))
    
    wb.save('PhoneBook.xlsx')
    styling()
    
    osCommandString = f'start excel.exe PhoneBook.xlsx'
    os.system(osCommandString)


# def open_html():
#     path = 'html_PhoneBook.html'
#     valid = exists(path)
#     if valid != True:
#         creating_html()
    
#     webbrowser.open_new_tab(path)
