# Exercise

# Define the Character class, then define the NPC class which inherits from Character


class Character:

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):

    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return f"{self.name} says: 'I heard there were monsters running around last night!'"


cecil = Character("Cecil", 100, 27)
anya = NPC("Anya", 100, 75)

print(f"{cecil.name} approaches.")  # Cecil approaches.
print(anya.speak())
