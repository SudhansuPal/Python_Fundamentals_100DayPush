x = 21
y = 0

def function():
    x = 12
    y = 13
    print(f'Local scope: {x,y}')


function()
print(f"Global scope: {x,y}")
