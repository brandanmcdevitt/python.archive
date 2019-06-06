# Exercises

# 1. Make use of http requests to pull data from a website
import requests
from pyfiglet import figlet_format

choice = True

print(figlet_format("Dad Jokes"))


def tell_dad_joke():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "text/plain"})
    print("\n" + "="*60)
    print(response.text)
    print("="*60 + "\n")


while choice:
    choice = input("Would you like to hear a dad joke? (y/n) ")
    if choice[0].lower() == "y":
        tell_dad_joke()
    elif choice[0].lower() == "n":
        print("\nHope you had fun. Bye!")
        break
    else:
        print("\nPlease enter yes or no.\n")
