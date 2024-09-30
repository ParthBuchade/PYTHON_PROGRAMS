import numpy as np

# Create a NumPy array
array = np.array([1, -2, 3, -4, 5])

print("Original Array:")
print(array)

# Unary Operations
# Negation
negated_array = -array
print("\nNegated Array:")
print(negated_array)

# Absolute value
absolute_array = np.abs(array)
print("\nAbsolute Value of Array:")
print(absolute_array)

# Square root (note: applying it to non-negative values)
sqrt_array = np.sqrt(absolute_array)
print("\nSquare Root of Absolute Values:")
print(sqrt_array)

# Exponential
exp_array = np.exp(array)
print("\nExponential of Array:")
print(exp_array)

sin_arr = np.sin(array)
print(sin_arr)

# Create two NumPy arrays of integers
array1 = np.array([10, 12, 14, 15])  # Binary: 1010, 1100, 1110, 1111
array2 = np.array([4, 8, 2, 1])      # Binary: 0100, 1000, 0010, 0001

print("Array 1:")
print(array1)
print("Array 2:")
print(array2)

# Bitwise AND
bitwise_and = array1 & array2
print("\nBitwise AND (array1 & array2):")
print(bitwise_and)

# Bitwise OR
bitwise_or = array1 | array2
print("\nBitwise OR (array1 | array2):")
print(bitwise_or)

# Bitwise XOR
bitwise_xor = array1 ^ array2
print("\nBitwise XOR (array1 ^ array2):")
print(bitwise_xor)

# Bitwise NOT
bitwise_not_array1 = ~array1
print("\nBitwise NOT (~array1):")
print(bitwise_not_array1)

# Bitwise NOT
bitwise_not_array2 = ~array2
print("\nBitwise NOT (~array2):")
print(bitwise_not_array2)

# Left Shift
left_shift = array1 << 1  # Shift bits to the left by 1
print("\nLeft Shift (array1 << 1):")
print(left_shift)

# Right Shift
right_shift = array1 >> 1  # Shift bits to the right by 1
print("\nRight Shift (array1 >> 1):")
print(right_shift)
