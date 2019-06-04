# Exercises

# 1. Write a function that takes in one parameter (a list) and returns the last value in the list
def return_last(l):
    if len(l) != 0:
        return l[len(l) -1]
    return None

return_last([1, 2, 41, 1, "hello", 4, 1, "world", 41, 7.63, 9]) # 9

# 2. Write a function that takes in two strings (a word/phrase and a letter) and return the number of times that the letter appears in the word/phrase
def letter_count(word, letter):
    return word.lower().count(letter)

letter_count("Winter is Coming", "i") # 3

# 3. Write a function that takes in a string and returns a dictionary with the
#    keys being each letter in the word and the values being the number of times
#    that letter appears
def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}

multiple_letter_count("Paradox")

# 4. Write a function that takes in a string and returns True if the word is a palindrome
def is_palindome(word):
    if word == word[::-1]:
        return True
    return False

is_palindome("racecar") #True

# 5. Write a function that takes in a number and prints out each number in the fibonacci sequence up until the number specified
def fibonacci(max):
    current_num = 1
    previous_num = 1
    fibonacci_num = 0

    for i in range(0, max):
        fibonacci_num = current_num + previous_num
        current_num = fibonacci_num
        previous_num = current_num
        print(fibonacci_num)

fibonacci(101)