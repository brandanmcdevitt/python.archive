# Exercise
from csv import reader, writer, DictReader

# 1. Write a function that takes in a first name and a last namea and adds it to
#    the users.csv file


def add_user(first, last):
    with open('Udemy/Modern_Python3_Bootcamp/users.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])

# add_user("Brandan", "McDevitt")

# 2. Write a function that prints out all the first and last names in the
#    users.csv file


def print_users():
    with open('Udemy/Modern_Python3_Bootcamp/users.csv') as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            print(f"{row['First Name']} {row['Last Name']}")


print_users()


# 3. write a function that takes in a first name and a last name and searches
#    the users.csv file for a match. if a match is found return the index of the
#    row. Else return not found.
def find_user(first, last):
    with open('Udemy/Modern_Python3_Bootcamp/users.csv') as file:
        csv_reader = reader(file)
        for (index, row) in enumerate(csv_reader):
            first_match = first == row[0]
            last_match = last == row[1]
            if first_match and last_match:
                return index
            return f"{first} {last} not found."


find_user("Brandan", "McDevitt")
