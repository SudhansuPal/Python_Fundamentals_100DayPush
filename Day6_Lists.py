x = 10
my_list = [1,2,"three", 3, "k4,34234,123123",x]
my_list.append(432)
print(my_list[4])
print(my_list[4:])
my_list.pop(1)
print(my_list) #list is mutable, so the changes are reflected in the original list
print()


print(list(range(0,10,int(2.6)))) #range function creates a list of numbers from 0 to 10 with a step of 2.6 where int(2.6) converts 2.6 to an integer 2
print()

my_list2 = [1,2,3]
print(sum(my_list2))

