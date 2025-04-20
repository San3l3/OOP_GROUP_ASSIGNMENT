class Pet:
  def __init__(self, name):
    self.name = name
    self.hunger = 5
    self.energy = 5
    self.happiness = 5
    self.tricks = []
  
  # eat(): reduces hunger by 3 points (but not below 0), and increases happiness by 1.
  def eat(self):
    self.hunger = max(0, self.hunger - 3)
    self.happiness = min(10, self.happiness + 1)
    print(f"{self.name} is eating.")

  # sleep(): increases energy by 5 points (but not above 10).
  def sleep(self):
    self.energy = min(10, self.energy + 5)
    print(f"{self.name} is sleeping.")

  # play(): decreases energy by 2, increases happiness by 2, and increases hunger by 1.
  def play(self):
    self.energy = max(0, self.energy - 2)
    self.happiness = min(10, self.happiness + 2)
    self.hunger = min(10, self.hunger + 1)
    print(f"{self.name} is playing.")

  # get_status(): prints the current state of the pet.
  def get_status(self):
    print(f"{self.name}'s status:")
    print(f"hunger: {self.hunger}")
    print(f"energy: {self.energy}")
    print(f"happiness: {self.happiness}")

  # method train(trick) that teaches your pet a new trick and stores it in a list.
  def train(self, trick):
    self.tricks.append(trick)
    print(f"{self.name} has learned {trick}!")

  # method show_tricks() that prints all learned tricks.
  def show_tricks(self):
    if not self.tricks:
      print(f"{self.name} has not learnt any tricks yet.")
    else:
      print(f"{self.name} has learned:")
      for trick in self.tricks:
        print(trick)

# INPUTS
# pet = Pet("Fido")
# pet.get_status()
# pet.eat()
# pet.sleep()
# pet.play()
# pet.get_status()
# pet.train("Sit")
# pet.train("Stay")
# pet.show_tricks()