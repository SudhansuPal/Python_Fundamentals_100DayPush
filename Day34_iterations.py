nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 != 0]

print("Evens:", evens)   
print("Odds:", odds)     
