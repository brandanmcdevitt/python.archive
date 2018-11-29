number_of_players = 0
names = {}
playing = True

print("\nHow to play:")
print("\nWhen prompted, input players name.")
print("When prompted, input how much they owe (-) or how much they gain (+).")
print("e.g. James")
print("e.g. +200\n")

while number_of_players < 2 or number_of_players > 6:
    number_of_players = int(input("How many players are there?\n"))

def play(players):
    for player in range(1, players + 1):
        names[raw_input("Enter Player {} name:\n".format(player))] = 1500

    print("\nYou each begin with $1500.")
    for key, value in names.items():
        print("{} = ${}".format(key, value))

    print("\nHave fun!\n\n")

    while playing:
        current_player = raw_input("Which player?\n")

        if current_player == "all":
            for key, value in names.items():
                print("{} = ${}".format(key, value))

            print("\n")
            current_player = raw_input("Which player?\n")

        money = raw_input("How much money?\n")

        if "+" in money:
            money = money.replace('+', '')
            names[current_player] += int(money)
            print("{} now has ${}\n".format(current_player, names[current_player]))
        elif "-" in money:
            money = money.replace('-', '')
            names[current_player] = names[current_player] - int(money)
            print("{} now has ${}\n".format(current_player, names[current_player]))
            if names[current_player] <= 0:
                global playing

                playing = False

    print("Game Over")
play(number_of_players)
