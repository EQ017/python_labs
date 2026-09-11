N = int(input('Введите количество студентов: '))
och = 0
zaoch = 0
for x in range(N):
    print(f'Сдудент под номером {x+1}: ', end = '')
    surname,name,age,format_of_taking_part = input().split()
    age = int(age)
    if format_of_taking_part == "True":
        format_of_taking_part = True
    else:
        format_of_taking_part = False
    if format_of_taking_part == True:
        och += 1
    else:
        zaoch += 1
print(f'out: {och} {zaoch}')