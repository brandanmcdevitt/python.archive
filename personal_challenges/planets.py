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
        user_input = input("What is planet no. {} from the sun?\n".format(i+1))

    print("\n{} is Correct!\n".format(planets[i+1][0]))

    try:
        if planets[i+1][1]:
            print("Fun fact: {} was named after the Greek God {}, who is the {}.\n".format(planets[i+1][0],
                                                                                           planets[i+1][1],
                                                                                           planets[i+1][2]))
    except:
        print()