def square(x):
    return x*x

square_lambda = lambda x: x * x

nums = [1,2,3,4,5]
squared_nums = list(map(lambda n: n*n, nums))

print(square(5))
print(square_lambda(5))
print(squared_nums)