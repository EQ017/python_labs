fio = input('ФИО: ')
lenghstr = 0
initials = ''
big_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРТСУФХЦЧШЩЪЫЬЭЮЯ'
for x in fio:
    if x != ' ':
        lenghstr += 1
    if x in big_letters:
        initials += x
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {lenghstr+2}')