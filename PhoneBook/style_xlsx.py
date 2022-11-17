import openpyxl

def styling():
    filename = 'PhoneBook.xlsx'
    book = openpyxl.load_workbook(filename)
    sheet = book.active

    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 17
    sheet.column_dimensions['C'].width = 50

    book.save('PhoneBook.xlsx')
