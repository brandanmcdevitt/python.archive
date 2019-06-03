# a little program to help me memorise the planets in our galaxy

planets = {1:["Mercury", "Hermes", "Messenger God"],
           2:["Venus", "Aphrodite", "God of Love"],
           3:["Earth"],
           4:["Mars", "Ares", "God of War"],
           5:["Jupiter", "Zues", "Chief God - God of Sky and Thunder"],
           6:["Saturn"],
           7:["Uranus"],
           8:["Neptune", "Poseidon", "God of Sea"]}

for i in range(len(planets)):
    user_input = ""

    while user_input.lower() != planets[i+1][0].lower():
        user_input = input(f"What is planet no. {i+1} from the sun?\n")
        
        if user_input.lower() != planets[i+1][0].lower():
            print(f"\nSorry, {user_input} is not correct.\n")

    print(f"\n{planets[i+1][0]} is Correct!\n")

    try:
        if planets[i+1][1]:
            print(f"Fun fact: {planets[i+1][0]} was named after the Greek God {planets[i+1][1]}, who is the {planets[i+1][2]}.\n")
    except:
        print()