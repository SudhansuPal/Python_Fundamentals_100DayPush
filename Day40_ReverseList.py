l1 = [1,23,2123,"Hello","iteration"]
# print(l1[-5])
reverse_l1 = []

for i in range(len(l1)):
    reverse_l1.append(l1[-(i+1)])

print(reverse_l1)
# a = l1[4:2:-1]
# a[0] = 5

# print(l1)