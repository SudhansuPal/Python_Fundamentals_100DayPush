#Check if a number is a prime number
#Prime numbers are numbers that are only divisible by 1 and itself and greater than 1 so 1 cannot be a prime number


x = int(input("Enter a number>>>")) #takes input from user
if x <=1:
    print(f"{x} is not a prime number.") #if the number is less than or equal to 1, it is not a prime number
else:
    for i in range(2,int(x)): #for loop checks if the number "x" is divisible by any number ranging from 2 to the number itself (2,x)
        if x%i == 0: #if the number is divisible by any number from 2 to the number itself, it is not a prime number
            print(f"{x} is not a prime number and is a composite number.") 
            break #break out of the loop if the number is divisible by any number from 2 to the number itself
    else:
        print(f"{x} is a prime number.") #if the number is not divisible by any number from 2 to the number itself, it is a prime number