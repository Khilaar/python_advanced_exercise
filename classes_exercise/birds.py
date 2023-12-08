from animal import Animal

class Bird(Animal):
    def __init__(self, name, color, melody):
        super().__init__(name, color)
        self.melody = melody
        self.wings = 2

    def fly(self):
        print(f"{self.name} is flying with {self.wings} {self.color} wings!")

    def sing(self):
        print(f"{self.melody} {self.melody} {self.melody}")


class Owl(Bird):
    def __init__(self, name, color, melody, degree):
        super().__init__(name, color, melody)
        self.degree = degree

    def neck_twist(self):
        print(f"{self.name} is doing a {self.degree} degree neck twist")

class Woodpecker(Bird):
    def __init__(self, name, color, melody, strength):
        super().__init__(name, color, melody)
        self.strength = strength

    def make_hole(self):
        for x in range(0, self.strength):
            print(self.melody)

