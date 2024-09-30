import numpy as np

# creating multi dimentional array
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

# Element-wise operations (squaring each element)
squared_array = array_1 ** 2
print("\nArray after squaring each element:")
print(squared_array)


# Dot product
dot_product = np.dot(array_1, array_2)
print("\nDot product of Array 1 and Array 2:", dot_product)

# Create a single NumPy array of zeros
array_zeros = np.zeros(5)  # 1D array with 5 zeros
print("Single Array of Zeros:")
print(array_zeros)

# Create a single NumPy array of ones
array_ones = np.ones(5)  # 1D array with 5 ones
print("\nSingle Array of Ones:")
print(array_ones)