class Classmate:
    def __init__(self, name, section, favorite_film):
        self.name = name
        self.section = section
        self.favorite_film = favorite_film

    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I belong to section {self.section}.")
        print(f"My favorite film is {self.favorite_film}.")
        print("-" * 40)


classmates = [
    Classmate("Yanna Moya", "10-Sapphire", "Fight Club"),
    Classmate("Ac Mactal", "10-Sapphire", "Girl, Boy, Bakla, Tomboy"),
    Classmate("Kleiser Fermocil", "10-Sapphire", "The Hows of Us"),
    Classmate("Zoe Mutia", "10-Sapphire", "Pride and Prejudice"),
    Classmate("Radhika Evangelio", "10-Sapphire", "Girl, Boy, Bakla, Tomboy")
]

print("\n=== CLASSMATE INTRODUCTIONS ===\n")
for student in classmates:
    student.introduce()

print("\n=== ADD A NEW CLASSMATE ===\n")
name = input("Enter name: ")
section = input("Enter section: ")
favorite_film = input("Enter favorite film: ")

new_classmate = Classmate(name, section, favorite_film)
classmates.append(new_classmate)

print("\n=== UPDATED CLASSMATE LIST ===\n")
for student in classmates:
    student.introduce()