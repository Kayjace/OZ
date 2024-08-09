class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def sound(self):
        return f"{self.name} says: Woof!"

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"

class Cat:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
    def sound(self):
        return f"{self.name} says: Meow!"

    def __str__(self):
        return f"Cat(name={self.name}, breed={self.breed})"