# Exercise
from csv import reader, writer, DictReader

# 1. Write a function that takes in a first name and a last namea and adds it to
#    the users.csv file


def add_user(first, last):
    with open('Udemy/Modern_Python3_Bootcamp/users.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])

add_user("Brandan", "McDevitt")

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


# 4. write a function that takes in an old first and last name and a new first
#    and last name. For any matches within the users.csv file update the old
#    names with the new names.
def update_users(old_first, old_last, new_first, new_last):
    count = 0
    with open('Udemy/Modern_Python3_Bootcamp/users.csv') as file:
        csv_reader = reader(file)
        rows = list(csv_reader)

    
    with open('Udemy/Modern_Python3_Bootcamp/users.csv', 'w') as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
    
    return f"Users updated: {count}"

update_users("Brandan", "McDevitt", "David", "Tennant")


# 5. write a function that takes in a first name and a last name and removes
#    those names from the users.csv file.
def delete_users(first, last):
    with open('Udemy/Modern_Python3_Bootcamp/users.csv') as file:
        csv_reader = reader(file)
        rows = list(csv_reader)

    count = 0
    with open('Udemy/Modern_Python3_Bootcamp/users.csv', 'w') as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == first and row[1] == last:
                count += 1
            else:
                csv_writer.writerow(row)
    
    return f"Users deleted: {count}"

delete_users("Colt", "Steele")