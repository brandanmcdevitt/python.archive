# Exercises

# 1. Define a function that accepts any number of arguments. It should return True if any of the arguments are "purple"
def contains_purple(*args):
    return "purple" in args

contains_purple(1, 2, 4, 7, "hello", 9.1, "white") # False
contains_purple("red", 9, 1.3, False, "purple") # True

# 2. Write a function which accepts a word and any number of additional keyword arguments.
#    if a prefix is provided, return the prefix followed by the word. If a suffix is provides, return the word followed by the suffix
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word

combine_words("child") # child
combine_words("child", prefix="man") # manchild
combine_words("child", suffix="ish") # childish

# 3. Create a function that counts how many times the number 7 appears in an unpacked list passed through as an argument
nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,
        34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,
        14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,
        56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,
        8,7,6,5,4,3,2,1,7]

def count_sevens(*args):
    return args.count(7)

count_sevens(*nums) # 14