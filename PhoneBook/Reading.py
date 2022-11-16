import os
from os.path import exists
from Creating_head import creating_txt
from Creating_head import creating_csv
from Creating_head import creating_html
import webbrowser

def open_txt():
    path = 'txt_PhoneBook.txt'
    valid = exists(path)
    if valid != True:
        creating_txt()
    
    osCommandString = f'notepad.exe {path}'
    os.system(osCommandString)


def open_csv():
    path = 'csv_PhoneBook.csv'
    valid = exists(path)
    if valid != True:
        creating_csv()
    
    osCommandString = f'notepad.exe {path}'
    os.system(osCommandString)


def open_html():
    path = 'html_PhoneBook.html'
    valid = exists(path)
    if valid != True:
        creating_html()
    
    webbrowser.open_new_tab(path)
