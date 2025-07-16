#program that checks if the user is eligible to vote in USA

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your Nationality: ")

if age >= 18 and nationality == "American":
    print(f" {first_name} {last_name}, you are eligible to vote in the USA")
else:
    print(f" {first_name} {last_name}, you are not eligible to vote in the USA")