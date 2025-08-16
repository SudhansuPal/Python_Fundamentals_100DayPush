#actually understood and grasped the concept of for loops. Kind of cleared my doubts about how the inner loop prints.
#Outer loop runs, inner loops is executed (prints) 1 time. 
#2nd iteration of the outer loop, inner loop executes (prints) 1 upto the second iteration (2)
#and so on..
for i in range(1,6):
    for j in range (1,i+1):
        print(j,end="")
    print()


