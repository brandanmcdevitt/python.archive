# a little program to help me memorise the planets in our galaxy

planets = {1:"Mercury",
           2:"Venus",
           3:"Earth",
           4:"Mars",
           5:"Jupiter",
           6:"Saturn",
           7:"Uranus",
           8:"Neptune"}

for i in range(len(planets)):
    user_input = ""

    while user_input.lower() != planets[i+1].lower():
        user_input = input("What is planet no. {} from the sun?\n".format(i+1))

    print("\n{} is Correct!\n".format(planets[i+1]))
