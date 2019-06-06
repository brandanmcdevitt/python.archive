# Exercises

# 1. Write a funcion that takes in two strings. Raise errors if the strings are
#    not given as arguments.


def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(color) is not str:
        raise TypeError("color must be instance of string")
    if type(text) is not str:
        raise TypeError("text must be an instance of string")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}.")


colorize("Hello", "blue")  # Printed Hello in blue.

# 2. Write a function that accepts a dictionary and key and returns None if
#    there is a KeyError


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {"name": "Ricky"}
print(get(d, "city"))  # None

# 3. Create a function that takes in two numbers, a and b. Return the result of
#    a/b and raise an error if the user tries to divide by zero or enters a string


def divide(a, b):
    try:
        import pdb
        pdb.set_trace()  # Using pdb to step through code
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong.")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


divide(2, 0)  # Something went wrong. Division by zero
