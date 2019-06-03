# Exercises

# 1. Create a lambda expression that multiplies two numbers and set it equal to a variable.
multiple = lambda n1, n2: n1*n2
print(multiple(2,7))

# 2. Write a function that takes a function as a parameter. Call that function with and pass it a lambda.
def lambda_function_test(function, value):
    return function(value)

lambda_function_test(lambda n: n**2, 8)

# 3. Use the map() function along with a lambda to add each element in two lists.
print(list(map(lambda x, y: x+y, [1,4,7,9], [8,4,1,6])))

# 4. Write a function that accepts a single list of numbers as a parameter. It should return a list where each item has been decremented by 1.
def decrement(values):
    return list(map(lambda n: n - 1, values))
decrement([4,1,4,7,7,9])

# 5 Use the filter() function along with a lambda to test if each element in a list is odd.
print(list(filter(lambda x: x % 2 != 0, [1,8,9,12,4,5,7,11])))

# 6. Write a function that accepts a list of numbers and returns a copy of the list with all negative values removed
def remove_negatives(values):
    print(list(filter(lambda n: n >= 0, values)))
remove_negatives([-13,9,1,-3,-7,9,2,5,-5])