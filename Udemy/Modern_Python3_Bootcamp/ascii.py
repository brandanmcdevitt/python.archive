# Exercise on importing external modules

from termcolor import colored
from pyfiglet import figlet_format

# Write a function that takes in two arguments for a phrase and colour


def print_colour(phrase, colour):
    valid_colours = ("red", "green", "yellow", "blue",
                     "magenta", "cyan", "white")

    if colour not in valid_colours:
        colour = "red"

    ascii_art = colored(figlet_format(phrase), color=colour)
    print(ascii_art)


phrase = input("What would you like to print?\n")
colour = input("What colour?\n")

print_colour(phrase, colour)
