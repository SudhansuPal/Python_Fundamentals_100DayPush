tuple = (1,2,"3","Three",4)
print(len(tuple))
print(tuple+("four","five",5))
print(tuple) #tuple doesnt change beacause it is immutable
print(tuple.index(2))
print(tuple.index(5)) #this doesnt work because the int 5 isnt in the original tuple
