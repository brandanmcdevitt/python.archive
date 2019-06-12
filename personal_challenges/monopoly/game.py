from pyfiglet import figlet_format
from players import Players, Banker
from board import Board
from random import randint
from termcolor import colored

print(figlet_format("Monopoly"))

game_over = False
all_players = []
num_of_players = 0

# A loop to determine the number of players
while num_of_players < 2 or num_of_players > 6:
    try:
        num_of_players = int(input("Enter the number of players: "))
        if num_of_players < 2 or num_of_players > 6:
            print("\nPlayers must be between 2 and 6 to play.\n")
    except ValueError as err:
        print("\nPlease enter a valid number.\n")

# Loop through the number of players and gather the player name and player token
for i in range(1, num_of_players+1):
    player_name = input(f"\nEnter player {i} name: ").lower()
    player_token = input(f"Enter player {i} token: ")

    all_players.append(Players(player_name, player_token))

    print(f"\nNew Player {all_players[i-1].name.upper()} created. Your token is a {all_players[i-1].token.upper()}.")

the_banker = input("\nWhich player is the banker? ").lower()

for player in all_players:
    if player.name.lower() == the_banker:
        banker_token = player.token
        all_players.remove(player)
        all_players.append(Banker(the_banker, banker_token))

while game_over is False:
    # Begin game
    for player in all_players:

        incorrect_format = True
        in_jail = False

        dice_1 = randint(1, 6)
        dice_2 = randint(1, 6)
        print(colored(f"\nCurrent player: {player.name.upper()}", "cyan"))
        print(f"You rolled a {dice_1} and {dice_2}. Move {dice_1 + dice_2} spaces.\n")
        while incorrect_format:
            balance_update = input("Enter how much you have lost/gained: ")
            if "+" in balance_update:
                incorrect_format = False
                balance_update = balance_update.replace("+", "")
                player.add_money(int(balance_update))
                if player.get_balance() < 500:
                    print(colored(f"Your new balance is ${player.get_balance()}", "red"))
                else:
                    print(colored(f"Your new balance is ${player.get_balance()}", "green"))
            elif "-" in balance_update:
                incorrect_format = False
                balance_update = balance_update.replace("-", "")
                player.remove_money(int(balance_update))
                if player.get_balance() <= 0:
                    print(
                        colored(f"{player.name.upper()} has been removed from the game.", "yellow"))
                    all_players.remove(player)
                    if len(all_players) is 1:
                        print(colored(f"GAME OVER. {all_players[0].name.upper()} has won the game!", "yellow"))
                        game_over = True
                elif player.get_balance() < 500:
                    print(
                        colored(f"Your new balance is ${player.get_balance()}", "red"))
                else:
                    print(
                        colored(f"Your new balance is ${player.get_balance()}", "green"))
            else:
                print("\nIncorrect format.")
                print("Example: '+200', '-140'\n")
                incorrect_format = True


def view_properties():
    b = Board()
    return b.list_properties()

def view_stations():
    b = Board()
    return b.list_stations()

def view_utilities():
    b = Board()
    return b.list_utilies()
