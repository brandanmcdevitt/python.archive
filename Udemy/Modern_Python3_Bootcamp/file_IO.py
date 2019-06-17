# Exercise

# 1. write a function that takes in a file name and a new file name and copies
#    the contents of the first file to the second file.
def copy(file_1, file_2):
    with open(file_1) as file:
        text_to_copy = file.read()
        
    with open(file_2, 'w') as file_copy:
        file_copy.write(text_to_copy)

copy('Udemy/Modern_Python3_Bootcamp/story.txt', 'Udemy/Modern_Python3_Bootcamp/story_copy.txt')


# 2. write a function that takes in a file name and a new file name and writes
#    the contents of the first file to the second file in reverse.
def copy_and_reverse(file_1, file_2):
    with open(file_1) as file:
        text_to_reverse = file.read()
    
    with open(file_2, 'w') as file_copy:
       file_copy.write(text_to_reverse[::-1])

copy_and_reverse('Udemy/Modern_Python3_Bootcamp/story.txt', 'Udemy/Modern_Python3_Bootcamp/story_reversed.txt')

# 3. write a function that takes in a file name and returns a dictionary with
#    the number of lines, words and characters in the file.
def statistics(file_name):
    with open(file_name) as file:
        text = file.readlines()

    return {"lines" : len(text),
            "words": sum(len(t.split()) for t in text),
            "characters": sum(len(char) for char in text)}

statistics('Udemy/Modern_Python3_Bootcamp/story.txt')


# 4. write a function that takes in a file name, a word and a replacement word.
#    Read the file and replace all instances of word with replacement word.
def find_and_replace(file_name, word, replacement):
    with open(file_name, 'r+') as file:
        text = file.read()
        text_updated = text.replace(word, replacement)
        file.seek(0)
        file.write(text_updated)

find_and_replace('Udemy/Modern_Python3_Bootcamp/story.txt', 'Alice', 'Brandan')