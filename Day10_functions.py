#Two functions that does the same thing (capitalize the entire string)
#Using return allows the result of a function to be stored in a variable or used in another operation. You can print it, store it, or manipulate it. In contrast, print() simply displays output to the screen and does not return a value. For example, the function prints "HERO" to the console but returns None, so the result cannot be reused in code. Using return is generally preferred when designing reusable functions, while print() is mainly used for displaying results or debugging.

def capitalization(x):
    return x.upper();

x = capitalization("data")
print(x)
print()


def capitalization2(x):
    print(x.upper())


capitalization2("hero")

