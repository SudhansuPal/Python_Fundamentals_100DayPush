#Nested IF statements checks one conditions only if the other condition is true
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("You passed!")
    
    if marks > 80:
        print("Congratulations! You got a distinction.")
else:
    print("You failed. Try again!")
