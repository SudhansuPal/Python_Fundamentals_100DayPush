x = 99 

def scope():
    x = 22
    def nested_scope():
        print(x+1)
    
    nested_scope()

scope()
print(x)