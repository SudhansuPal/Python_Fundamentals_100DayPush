print(hash("hello"))   # consistent hash for this run
print(hash(42))        # integers hash to themselves
print(hash((1, 2, 3))) # tuples are hashable if all elements are
