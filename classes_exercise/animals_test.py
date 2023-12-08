#Classes

from animal import Animal
from birds import Bird
from birds import Woodpecker
from birds import Owl
from fishes import Fish
from fishes import Salmon
from fishes import Shark




woodpecker = Bird("Woodpecker", "white", "pagack")
owliboi = Owl("owliboi", "brown", "Guguuu", 360)
peckerson = Woodpecker("Peckerson", "red", "PickPick", 9)
nemo = Fish("Nemo", "red", 10)
sally = Salmon("Sally", "pink", 15)
sharky = Shark("Sharky", "grey", 50)

woodpecker.introduce()
woodpecker.fly()
woodpecker.sing()

owliboi.introduce()
owliboi.fly()
owliboi.sing()

owliboi.neck_twist()

peckerson.make_hole()
nemo.swim()

sally.swim()
sally.introduce()

sharky.bite()
sharky.introduce()
sharky.swim()