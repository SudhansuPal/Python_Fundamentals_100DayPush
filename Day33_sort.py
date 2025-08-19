l1 = [2,31,641,1,1,1,1,3,4,145,0,24,5]
sorted_list = []

while l1:
    smallest = l1[0]

    for i in l1:
        if i < smallest:
            smallest = i

    sorted_list.append(smallest)
    l1.remove(smallest)

print(sorted_list)
