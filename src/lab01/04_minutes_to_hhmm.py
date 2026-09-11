m = int(input("Минуты: "))
hours = m//60
minutes = m - hours*60
if minutes >= 10:
    print(f"{hours}:{minutes}")
else:
    print(f"{hours}:0{minutes}")