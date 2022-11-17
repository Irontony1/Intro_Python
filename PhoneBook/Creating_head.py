
def creating_head():
    file = 'txt_PhoneBook.txt'
    name = 'Имя'
    phone = 'Номер телефона'
    about = 'Описание'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'{name};{phone};{about}\n')
