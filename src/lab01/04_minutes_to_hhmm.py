m = int(input("Минуты: "))
hours = m//60
minutes = m - hours*60
print(f"{hours}:{minutes:02d}")
