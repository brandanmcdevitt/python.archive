# # Exercise

from functools import wraps

# 1. Write a function that accepts a function and returns another function
def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper

@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3, a = "hi", b = "bye")

# 2. Write a function that ensures that no kwargs have been passed in
def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed, sorry!")
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"Hi there, {name}")

greet(name="tony")

# 3. Write a function that accepts only ints 
def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner


# 4. Write a function that returns "unauthorized" if the keyword argument does
#    not contain "admin"
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "admin" in kwargs.values():
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody")) # "Unauthorized"