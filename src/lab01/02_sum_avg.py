a = input("a: ")
b = input("b: ")
a,b = float(a.replace(",",".")),float(b.replace(",","."))
print(f"sum={f'{a+b:.2f}'}; avg={f"{(a+b)/2:.2f}"}")