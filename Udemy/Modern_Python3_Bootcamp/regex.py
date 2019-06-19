# Exercises

# https://pythex.org

import re

# 1. Write two functions. One to extract a phone number from a user input and
#    another to return all instances of the number being found
def extract_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)


# print(extract_phone("123 456-7891"))
# print(extract_all_phones("123 456-7891 p24po2po42p3po2p3jpj3"))


# 2. Write a function that takes in a time in string format and returns True if
#    the time is valid or False if the time is invalid
def is_valid_time(input):
    time_regex = re.compile(r'^\d\d?:\d{2}$')
    match = time_regex.search(input)
    if match:
        return True
    return False

print(is_valid_time("11:23")) # True 
print(is_valid_time("It is 15:43")) # False


# 3. write a function that accepts a string. It should return a list of the
#    binary bytes contained in the string
def parse_bytes(input):
    byte_regex = re.compile(r'\b[10]{8}\b')
    return byte_regex.findall(input)

print(parse_bytes("11001010 dsd sd sds ds 01010100")) # ['11001010', '01010100']


# 4. write a function that takes in a string and if it matches a date, return a
#    dictionary in the format of {d: xx, m: xx, y:xxx }
def parse_date(input):
    date_regex = re.compile(r'^(\d{2}).(\d{2}).(\d{4})$')
    match = date_regex.search(input)
    if match:
        return {
            'd': match.group(1),
            'm': match.group(2),
            'y': match.group(3)
        }
    return None


print(parse_date("23/07/1992"))


# 5. write a function that takes in a string and returns a censored version of
#    the string if the input matches the profanity filter
def censor(input):
    censor_regex = re.compile(r'\bfrack\w*\b', re.I)
    censored = censor_regex.sub("CENSORED", input)
    return censored


print(censor("Frack you"))