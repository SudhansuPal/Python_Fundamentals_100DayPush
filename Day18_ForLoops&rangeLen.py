word = "hack"
for i in range(len(word)):
    word = word[1:]+word[:1]  
    print(word, end=" ")

print()
print(range(len(word)))

for i in range(len(word)):
    word = word[i:]+word[:i]  # :i returns a substring from index 0 up to i (excluding i). More below.
    print(word, end=" ")

s = "hello"

for i in range(len(s) + 1):
    print(s[:i])
