# checking if string is the same from the back and front
string = input("Enter a string>>>")

if string == string[::-1]:
    print("The String is a palindrome.")
else:
    print("The String is NOT a palindrome.")


print(string[::-1])
