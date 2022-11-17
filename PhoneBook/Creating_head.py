
def creating_head():
    file = 'txt_PhoneBook.txt'
    name = 'Имя'
    phone = 'Номер телефона'
    about = 'Описание'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'{name};{phone};{about}\n')


# def creating_html():
#     file = 'html_PhoneBook.html'
#     name = 'Имя'
#     phone = 'Номер телефона'
#     about = 'Описание'
#     with open (file, 'w', encoding = 'utf-8') as data:
#         data.write(f'{name:<30} {phone:<15} {about:<50}<br />')