try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Please type a valid number.")
