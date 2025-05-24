class Pet:
    
    def __init__(self, species, health, happiness, hunger, name):
        self.species = species
        self.name = name
        self.health = health
        self.happiness = happiness
        self.hunger = hunger
        self.energy = 100

    def feed(self, amount: int) -> bool:
        if not(1 <= amount <= 25):
            print("Invalid feed amount! Please enter a value between 1 and 25.")
            return False
        extra_food = 5
        max_feed = self.hunger + extra_food
        if amount > max_feed:
            print(f"{self.name} is overfed and feels sick.")
            self.health = max(0, self.health - 10)
            return False
        self.hunger = max(0, self.hunger - amount)
        self.health = min(100, self.health + amount * 2)
        self.energy = min(100, self.energy + amount)
        print(f"You fed {self.name} {amount} units of food and restored {amount} energy.")
        return True

    def play(self) -> bool:
        if self.energy < 10:
            print(f"{self.name} is too tired to play.")
            return False
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        print(f"You played with {self.name}!")
        return True

    def heal(self, amount: int) -> bool:
        if not (1 <= amount <= 10):
            print("Invalid heal amount! Please enter a value between 1 and 10.")
            return False
        self.health = min(100, self.health + amount * 3)
        self.happiness = min(100, self.happiness + amount)
        self.energy = min(100, self.energy + amount)
        print(f"You healed {self.name} with {amount} units of medicine and restored {amount} energy.")
        return True

    def status(self):
        print(f"--- {self.name}'s Status ({self.species}) ---")
        print(f"Health   : {self.health}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Hunger   : {self.hunger}/100")
        print(f"Energy   : {self.energy}/100\n")
