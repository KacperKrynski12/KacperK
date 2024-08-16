# class Animal:

#     owner = "Jack"

#     def __init__(self, given_name, given_species, animal_age):
#         self.name = given_name
#         self.species = given_species
#         self.age = animal_age

#     def make_sound(self):
#         print(f"I'm {self.name} and I'm a {self.species}")


# our_animal = Animal("Rex", "Dog", 5)

# our_animal2 = Animal("Barbara", "Cat", 8)

# if our_animal.species == our_animal2.species:
#     print("They are the same species")
# else:
#     print("They are different species")

# print(our_animal.age + our_animal2.age)
# print("-----------------")
# print(our_animal.owner)
# print(our_animal2.owner)
# print("-----------------")
# our_animal.owner = "Kacper"
# print(our_animal.owner)
# print(our_animal2.owner)
# print("-----------------")
# Animal.owner = "Piotr"
# print(our_animal.owner)
# print(our_animal2.owner)
# new_animal = Animal("Kuba", "Horse", 10)
# print(new_animal.owner)

# class samochod2:
#     owner = "Kacper"
#     def __init__(self, nazwa, przebieg):
#         self.nazwa = nazwa
#         self.przebieg = przebieg

#     def metoda(self):
#         print(f"Moja marka to {self.nazwa}")
#         print(f"Przebieg to {self.przebieg}")
        

# mycar = samochod2("Opel", 138000)


# print(mycar.przebieg)
# print(mycar.nazwa)
# samochod2.owner = "Filip"
# print(samochod2.owner)
# print(samochod2.metoda)
# mycar = samochod2("Opel", 138000)
# print(mycar.metoda)

class Animal:

    owner = "Jack"

    def __init__(self, given_name, given_species, animal_age):
        self.name = given_name
        self.species = given_species
        self.age = animal_age

    def make_sound(self):
        print(f"I'm {self.name} and I'm a {self.species}")


    def __repr__(self) -> str:
        return f"This is an object of Animal class with name {self.name}, species {self.species} and age {self.age}. Owner is {self.owner}"
    
    def __str__(self) -> str:
        return f"{self.name}, {self.species}"

our_animal = Animal("Rex", "Dog", 5)

print(our_animal)

animal_representation_string = str(our_animal)

print(animal_representation_string)
our_animal2 = Animal("Barbara", "Cat", 8)

# if our_animal.species == our_animal2.species:
#     print("They are the same species")
# else:
#     print("They are different species")
#
# print(our_animal.age + our_animal2.age)
# print("-----------------")
# print(our_animal.owner)
# print(our_animal2.owner)
# print("-----------------")
# our_animal.owner = "Kacper"
# print(our_animal.owner)
# print(our_animal2.owner)
# print("-----------------")
# Animal.owner = "Piotr"
# print(our_animal.owner)
# print(our_animal2.owner)
# new_animal = Animal("Kuba", "Horse", 10)
# print(new_animal.owner)

# new_animal.make_sound()


class Dog(Animal):

    species = "Dog"

    def __init__(self, given_name, animal_age, given_breed):
        super().__init__(given_name, self.species, animal_age)
        self.breed = given_breed

    def make_sound(self):
        super().make_sound()
        print(f"I'm {self.name} and I'm a {self.species}, of a {self.breed} breed and I bark")

    def bark(self):
        print(f"Bark bark {self.name}")


new_dog = Dog("Rex", 5, "Labrador")
new_dog.make_sound()


def allow_only_animals(animal: Animal):
    animal.make_sound()


def allow_only_dogs(dog: Dog):
    dog.bark()


allow_only_animals(new_dog)
allow_only_dogs(our_animal2)


    
