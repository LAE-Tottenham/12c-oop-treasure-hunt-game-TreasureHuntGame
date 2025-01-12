import random
import time
from item import Item  # Ensure Item is imported

class Player:
    def __init__(self, name, secret_room, castle):
        self.name = name
        self.rucksack = []
        self.current_place = None
        self.health = 100
        self.max_items = 5  # Default max items
        self.has_statue_of_immortality = False
        self.instant_kill = False
        self.undetectable_timer = 0
        self.secret_room = secret_room
        self.castle = castle
    def move(self, place):
     if place:
        self.current_place = place
        print(f"You have moved to {self.current_place.name}")

        # Toxic Town health depletion logic
        if self.current_place.name == "Toxic Town" and not any(item.name == "Gas Mask" for item in self.rucksack):
            print("You have entered Toxic Town without a Gas Mask! The toxic gas is draining your health.")
            for seconds in range(10, 0, -1):
                if self.health <= 0:
                    print("You have succumbed to the toxic gas. Game over!")
                    exit()  # Ends the game
                print(f"Health: {self.health} | Time left: {seconds} seconds")
                self.health -= 10  # Lose 10 health every second
                time.sleep(1)  # Simulate real-time health depletion
            print("You have survived Toxic Town, but barely! Find a Gas Mask next time.")
        elif self.current_place.name == "Toxic Town":
            print("Your Gas Mask protects you from the toxic gas. You can safely explore Toxic Town.")

        # Handle instant kill or undetectable timer mechanics
        if self.instant_kill:
            self.instant_kill_enemy()
            self.instant_kill = False
        if self.undetectable_timer > 0:
            self.undetectable_timer -= 1
            print("You are moving undetected.")
     else:
        print("You can't go that way.")


   


    def pick_up(self, item):
        if len(self.rucksack) < self.max_items:
            self.rucksack.append(item)
            print(f"You picked up {item.name}")
            self.describe_item(item)
        else:
            print("Your rucksack is full. Use or drop an item before picking up new ones.")

    def describe_item(self, item):
        descriptions = {
            "Health Potion": "This potion will restore 50 health when used.",
            "Larger Backpack": "This backpack allows you to carry more items.",
            "Fireball": "This spell will instantly kill an enemy when used.",
            "Statue of Immortality": "This statue will allow you to avoid death once.",
            "Gas Mask": "This mask protects you from toxic gas.",
            "Silent Step Shoes": "These shoes make you undetectable by enemies.",
            "Damage Potion": "This potion deals 50 damage to an enemy when used.",
            "Magic Orb": "This orb reveals information about monsters and their locations.",
            "Unknown Food Item": "This food has unpredictable effects. Be cautious!",
            "Mysterious Ring": "This ring helps you find hidden treasures nearby.",
            "Ancient Scroll": "This scroll contains clues to help you navigate.",
            "Dagger Sharpener": "This sharpener improves the effectiveness of your daggers."
        }
        print(descriptions.get(item.name, "You picked up an item."))

    def use_item(self, item_name):
        item = next((item for item in self.rucksack if item.name.lower() == item_name), None)
        if item:
            if item.name == "Health Potion":
                self.health += 50
                print(f"You used a Health Potion. Your health is now {self.health}.")
            elif item.name == "Larger Backpack":
                self.max_items += 5
                print("You used a Larger Backpack. You can now carry more items.")
            elif item.name == "Fireball":
                print("You used a Fireball! The next enemy encounter will be an instant kill.")
                self.instant_kill = True
            elif item.name == "Statue of Immortality":
                self.has_statue_of_immortality = True
                print("You used the Statue of Immortality. You can avoid death once.")
            elif item.name == "Gas Mask":
                print("You are now protected from toxic gas and can enter Toxic Town without losing health.")
            elif item.name == "Silent Step Shoes":
                print("You used the Silent Step Shoes. You can now move around without being detected by enemies.")
                self.undetectable_timer = 10  # Undetectable for 10 moves
            elif item.name == "Damage Potion":
                print("You used the Damage Potion. The next enemy you encounter will take 50 damage.")
                self.deal_damage_next_enemy()
            elif item.name == "Magic Orb":
                print("You used the Magic Orb. It reveals information about monsters and their locations.")
                self.reveal_monster_info()
            elif item.name == "Unknown Food Item":
                if random.choice([True, False]):
                    self.health += 50
                    print(f"You ate the Unknown Food Item. Your health is now {self.health}.")
                else:
                    self.health -= 50
                    print(f"You ate the Unknown Food Item and it was poisoned! Your health is now {self.health}.")
            elif item.name == "Mysterious Ring":
                print("The Mysterious Ring is vibrating. You're near a town with hidden treasures.")
                self.detect_hidden_treasure()
            elif item.name == "Ancient Scroll":
                print("The Ancient Scroll reveals clues that help you navigate the world more effectively.")
                self.reveal_navigation_clues()
            elif item.name == "Dagger Sharpener":
                print("You used the Dagger Sharpener. Your daggers are now sharper and more effective in combat.")
                self.sharpen_daggers()
            else:
                print(f"You used the {item.name}.")
            self.rucksack.remove(item)
        else:
            print("Item not in your rucksack.")

    def instant_kill_enemy(self):
        if self.current_place.enemies:
            enemy = self.current_place.enemies.pop(0)
            print(f"The {enemy.name} was instantly killed by the Fireball!")
        else:
            print("No enemies to use the Fireball on.")

    def deal_damage_next_enemy(self):
        if self.current_place.enemies:
            enemy = self.current_place.enemies[0]
            enemy.strength -= 50
            print(f"The {enemy.name} took 50 damage! Its strength is now {enemy.strength}.")
            if enemy.strength <= 0:
                print(f"The {enemy.name} has been defeated!")
                self.current_place.enemies.remove(enemy)
        else:
            print("No enemies to use the Damage Potion on.")

    def reveal_monster_info(self):
        print("The Magic Orb reveals: The dragon is in the mountains, the thief is in the desert, and the monster is in the cave.")

    def detect_hidden_treasure(self):
        hidden_treasure_towns = ["Village", "Castle", "Mountain"]
        if any(town in self.current_place.name for town in hidden_treasure_towns):
            print("The Mysterious Ring vibrates more intensely as you are near hidden treasures.")

    def reveal_navigation_clues(self):
        print("The Ancient Scroll reveals: Follow the river to the swamp and find the secret entrance to the hidden village.")

    def sharpen_daggers(self):
        for item in self.rucksack:
            if "Dagger" in item.name:
                print(f"Your {item.name} is now sharper and more effective in combat.")

    def check_rucksack(self):
        if self.rucksack:
            print("Items in your rucksack:")
            for item in self.rucksack:
                print(f"- {item.name} (Weight: {item.weight})")
        else:
            print("Your rucksack is empty.")

    def display_status(self):
        print(f"Name: {self.name}, Health: {self.health}")
        print(f"Rucksack: {', '.join([item.name for item in self.rucksack])}")
        print(f"Max items you can carry: {self.max_items}")

    def solve_riddle(self):
        riddle_answer = input("Solve this riddle to unlock the treasure. What has keys but can't open locks?: ").lower()
        if riddle_answer == "piano":
            print("Correct! A hidden treasure chest appears before you containing a Gas Mask.")
            gas_mask = Item("Gas Mask", 2)
            self.rucksack.append(gas_mask)
            print(f"A Gas Mask has been added to your rucksack.")
        else:
            print("Wrong answer. Try again.")

    def interact(self, person):
        print(f"You interacted with {person.name}. They said: '{person.dialogue}'")
        if person.name.lower() == "guard" and "Key" in [item.name for item in self.rucksack]:
            print("You showed the Key to the guard and entered the Secret Room in the Castle.")
            self.move(self.secret_room)
            self.solve_riddle()
            move_choice = input("Do you want to return to the Castle? (yes/no): ").lower()
            if move_choice == "yes":
                self.move(self.castle)
                print("You have returned to the Castle.")
        else:
            print(f"{person.name} has nothing more to say.")
