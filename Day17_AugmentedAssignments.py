x = 10
y = 3

print("Initial values:", "x =", x, ", y =", y)

x += y     # x = x + y
print("x += y →", x)

x -= y     # x = x - y
print("x -= y →", x)

x *= y     # x = x * y
print("x *= y →", x)

x /= y     # x = x / y (note: becomes a float)
print("x /= y →", x)

x = 2
y = 3
x **= y    # x = x ** y (exponentiation)
print("x **= y →", x)

x = 10
y = 3
x //= y    # x = x // y (floor division)
print("x //= y →", x)

x %= y     # x = x % y (modulus)
print("x %= y →", x)

x = 5      # binary: 0b0101
y = 1
x >>= y    # x = x >> y (bitwise right shift)
print("x >>= y →", x)

x <<= y    # x = x << y (bitwise left shift)
print("x <<= y →", x)

x &= y     # x = x & y (bitwise AND)
print("x &= y →", x)

x |= y     # x = x | y (bitwise OR)
print("x |= y →", x)

x ^= y     # x = x ^ y (bitwise XOR)
print("x ^= y →", x)

# Matrix multiplication requires NumPy
import numpy as np
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
x @= y     # x = x @ y (matrix multiplication)
print("x @= y →\n", x)
