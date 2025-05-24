from Pet import Pet

class VirtualPetGame:
    
    def __init__(self):
        self.pets = []
        self.initial_health = {}
        self.cycle_count = 0
        self.multi_pet_asked = False
        self.improper_care_counts = {}

    def choose_species_and_name(self):
        species_data = {
            'lizard': {'health': 80, 'happiness': 50, 'hunger': 20},
            'cat':    {'health': 60, 'happiness': 70, 'hunger': 40},
            'puppy':  {'health': 40, 'happiness': 80, 'hunger': 60}}
        while True:
            choice = input("Choose your pet (lizard/cat/puppy): ").strip().lower()
            if choice in species_data:
                name = input(f"What would you like to name your {choice}? ").strip()
                data = species_data[choice]
                pet = Pet(choice, data['health'], data['happiness'], data['hunger'], name)
                return pet
            print("Invalid species! Please choose from lizard, cat, or puppy.\n")

    def offer_second_pet(self):
        while True:
            choice = input("Would you like to adopt a second pet? (yes/no): ").strip().lower()
            if choice == 'yes':
                return True
            elif choice == 'no':
                return False
            else:
                print("Please answer 'yes' or 'no'.")

    def feed(self, pet):
        feed_amt = int(input(f"How much food to give {pet.name}? (1-25): ").strip())
        pet.feed(feed_amt)

    def play(self, pet):
        pet.play()

    def heal(self, pet):
        heal_amt = int(input(f"How much medicine to give {pet.name}? (1-10): ").strip())
        pet.heal(heal_amt)

    def cycle_decay(self):
        for pet in self.pets:
            if len(self.pets)== 2 and self.pets[0].species ==  self.pets[1].species:
                same_species = True
            else:
                same_species = False
            if same_species and pet.species != 'lizard':
                pet.health = max(0, pet.health - 2)
                pet.happiness = max(0, pet.happiness - 2)
                pet.hunger = min(100, pet.hunger + 15)
            else:
                pet.health = max(0, pet.health - 5)
                pet.happiness = max(0, pet.happiness - 5)
                pet.hunger = min(100, pet.hunger + 10)

    def check_improper_care(self, pet):
        if pet.hunger > 90 or pet.happiness < 40 or pet.health < 30:
            self.improper_care_counts[pet] += 1
        else:
            self.improper_care_counts[pet] = 0
        if self.improper_care_counts[pet] > 3:
            print(f"{pet.name} has left home due to improper care.")
            return True
        return False

    def run(self):
        print("\nWelcome to the Virtual Pet Game!\n")
        print("Each pet has four attributes (0—100):")
        print(" - Health   : higher means healthier")
        print(" - Happiness: higher means happier")
        print(" - Hunger   : higher means hungrier (100 is starving)")
        print(" - Energy   : higher means more energetic\n")
        print("Feeding rule: up to hunger +5 units (max 25), else overfeed.")
        print("Feeding and healing also restore energy equal to amount used.\n")
        print("Available commands: feed, play, heal, skip, quit.\n")

        print("Select your first pet:")
        first = self.choose_species_and_name()
        self.pets.append(first)
        self.initial_health[first] = first.health
        self.improper_care_counts[first] = 0
        print(f"\nGreat! You adopted {first.name}.\n")
        first.status()

        while True:
            if self.cycle_count >= 6 and not self.multi_pet_asked:
                if first.health >= 0.8 * self.initial_health[first]:
                    if self.offer_second_pet():
                        second = self.choose_species_and_name()
                        self.pets.append(second)
                        self.initial_health[second] = second.health
                        self.improper_care_counts[second] = 0
                        print(f"\nGreat! You adopted {second.name}.\n")
                self.multi_pet_asked = True

            for pet in list(self.pets):
                action = input(f"What would you like to do with {pet.name}? (feed/play/heal/skip/quit): ").strip().lower()
                if action == 'quit':
                    print("Thanks for playing! Goodbye.")
                    return
                elif action == 'feed':
                    self.feed(pet)
                elif action == 'play':
                    self.play(pet)
                elif action == 'heal':
                    self.heal(pet)
                else:
                    print(f"You skipped interaction with {pet.name}.")

                if pet.health <= 0:
                    print(f"{pet.name} has passed away. Game over.")
                    return

            self.cycle_decay()
            for pet in list(self.pets):
                pet.status()
                if self.check_improper_care(pet):
                    self.pets.remove(pet)
                    if not self.pets:
                        print("No pets left. Game over.")
                        return
            self.cycle_count += 1

if __name__ == "__main__":
    game = VirtualPetGame()
    game.run()
