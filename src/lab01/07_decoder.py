cipher = input('in: ')
big_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРТСУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'
og_message = ''
for x in cipher:
    if len(og_message) > 0 and og_message[-1] != '.':
        og_message += x
    if og_message == '' and x in big_letters:
        og_message += x
step = 0
for x in range(len(og_message)):
    if og_message[x] in '0123456789':
        step = x
        break
print(f'out: {og_message[::step+1]}')