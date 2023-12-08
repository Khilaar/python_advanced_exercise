from animal import Animal

class Fish(Animal):
    def __init__(self, name, color, speed):
        super().__init__(name, color)
        self.speed = speed

    def swim(self):
        print(f"{self.name}, the {self.color} fish, is swimming at a speed of {self.speed} km/h")


class Salmon(Fish):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def swim(self):
        print(f"{self.name}, the {self.color} fish, is swimming at a speed of {self.speed} km/h against the current")


class Shark(Fish):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def bite(self):
        print("nham nham nham")