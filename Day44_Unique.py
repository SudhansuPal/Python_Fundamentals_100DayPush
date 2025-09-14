dupes = [1,22,3,12,1,22,34,5,3,3]
unique = []

for i in dupes:
    if i not in unique:
        unique += [i] or unique.append(i)


print(unique)
                