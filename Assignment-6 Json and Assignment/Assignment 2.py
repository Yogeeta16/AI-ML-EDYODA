class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, energy_level):
        super().__init__(name, age, coat_color)
        self.energy_level = energy_level

    def unique_method(self):
        print(
            f"{self.name} is a Jack Russell Terrier with an energy level of {self.energy_level}.")

    def bark(self):
        print(f"{self.name} the Jack Russell Terrier barks enthusiastically!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def unique_method(self):
        print(f"{self.name} is a Bulldog with a strength level of {self.strength}.")

    def bark(self):
        print(f"{self.name} the Bulldog barks loudly!")


# Create Dog objects
dog1 = Dog("Fido", 3, "Brown")
dog2 = JackRussellTerrier("Jack", 2, "White and Brown", "High")
dog3 = Bulldog("Buddy", 4, "Gray", "Strong")

# Demonstrate Dog methods
print("Dog 1:")
dog1.description()
dog1.get_info()

# Demonstrate JackRussellTerrier methods
print("\nDog 2:")
dog2.description()
dog2.get_info()
dog2.unique_method()
dog2.bark()

# Demonstrate Bulldog methods
print("\nDog 3:")
dog3.description()
dog3.get_info()
dog3.unique_method()
dog3.bark()
