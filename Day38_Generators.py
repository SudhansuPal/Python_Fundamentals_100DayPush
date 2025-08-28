#Generators in Python are like functions that remember their state between calls. Instead of returning everything at once (like lists), they yield values one at a time — great for efficiency and lazy evaluation.
def count_up_to(n):
    """Generator that yields numbers from 1 to n."""
    x = 1
    while x <= n:
        yield x   # pause here and return value
        x += 1

# Using the generator
for num in count_up_to(5):
    print(num)
