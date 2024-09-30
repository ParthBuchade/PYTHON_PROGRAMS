# A simple lambda function to add two numbers
add = lambda x, y: x + y
print("Addition of 5 and 3:", add(5, 3))


# Using lambda with map to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("\nSquared Numbers:", squared_numbers)