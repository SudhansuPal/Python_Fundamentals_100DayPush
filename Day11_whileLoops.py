x = int(input("Enter a whole number>>>"))
y = float(input("Enter a decimal>>>"))
z = x+y
while x<=11:
    if x<z:
        print(f"{x} is your current number.")
    else:
        print(f"{x} is your new number.")
    x = x+y        