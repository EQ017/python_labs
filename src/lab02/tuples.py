def format_record(student):
    if type(student) != tuple:
        raise TypeError("Входные данные должны являться кортежем")
    if len(student) != 3:
        raise ValueError("Неверное количество элементов")
    if type(student[0]) != str or len(student[0]) <= 0:
        raise TypeError("Неверное ФИО")
    if type(student[1]) != str:
        raise TypeError("Неверная группа")
    if type(student[2]) != float:
        raise TypeError("Неверная GPA")
    if student[2] > 5 or student[2] < 0:
        raise ValueError("GPA вне диапазона")
    
    if len(student[0].split()) == 2:
        fio = student[0].split()[0][0].upper() + student[0].split()[0][1:] + ' ' + student[0].split()[1][0].upper() + '.'
    elif len(student[0].split()) == 3:
        fio = student[0].split()[0][0].upper() + student[0].split()[0][1:] + ' ' + student[0].split()[1][0].upper() + '.' + student[0].split()[2][0].upper() + '.'
    group = student[1]
    gpa = student[2]
    return f"{fio}, гр. {group}, GPA {gpa:.2f}"

# print(f"{("Иванов Иван Иванович", "BIVT-25", 4.6)} -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}")
# print(f"{("Петров Пётр", "IKBO-12", 5.0)} -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}")
# print(f"{("Петров Пётр Петрович", "IKBO-12", 5.0)} -> {format_record(("Петров Пётр Петрович", "IKBO-12", 4.6))}")
# print(f"{("  сидорова  анна   сергеевна", "ABB-01", 3.999)} -> {format_record(("  сидорова  анна   сергеевна", "ABB-01", 3.999))}")
# print(f"{("Иванов Иван Иванович", "BIVT-25", "4.6")} -> {format_record(("Иванов Иван Иванович", "BIVT-25", "4.6"))}")