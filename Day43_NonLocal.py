def outer(start):
    state = start
    def inner(label):
        print(label, state)   
    return inner

f = outer(10)
f("First call")   
f("Second call")  
