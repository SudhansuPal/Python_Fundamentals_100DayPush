def make_multiplier(factor):
    def multiplier(x):
        return x * factor  # <-- captures "factor" from outer scope
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  
print(triple(5))  
