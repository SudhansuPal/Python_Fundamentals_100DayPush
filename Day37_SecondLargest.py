nums = [1,2312,4232,12,32,42,423,25,23,12,33,4,2]
largest = nums[0]
second_largest = nums[0]

for i in nums:
    if i > largest:
        largest = i 

for j in nums:
    if largest>j>second_largest:
        second_largest = j

print("Second Largest:", second_largest)
