class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age, health=120, happiness=90):
        super().__init__(name, age, health, happiness)

    def roar(self):
        print(f"{self.name} is roaring! It sounds majestic!")

class Tiger(Animal):
    def __init__(self, name, age, health=110, happiness=95):
        super().__init__(name, age, health, happiness)

    def hunt(self):
        print(f"{self.name} is hunting! It's so stealthy!")

class Bear(Animal):
    def __init__(self, name, age, health=100, happiness=80):
        super().__init__(name, age, health, happiness)
        self.hibernating = False

    def hibernate(self):
        self.hibernating = True
        print(f"{self.name} is hibernating for the winter!")

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_animal(Lion("Nala", 5))
zoo1.add_animal(Lion("Simba", 4))
zoo1.add_animal(Tiger("Rajah", 3))
zoo1.add_animal(Tiger("Shere Khan", 7))
zoo1.add_animal(Bear("Baloo", 10))

zoo1.print_all_info()

# Let's feed all the animals
print("\nFeeding all the animals...")
for animal in zoo1.animals:
    animal.feed()

zoo1.print_all_info()

