l1 = [[1, 2], [3, 4], [5]] 
# → [1, 2, 3, 4, 5]
l2 = []

for i in l1:
        for j in i:
            l2 += [j]

print(l2)

       