x = 0  

def add():
    global x  
    x += 21   
    print("Inside function:", x)

print("Before calling function:", x)
add()
print("After calling function:", x)
