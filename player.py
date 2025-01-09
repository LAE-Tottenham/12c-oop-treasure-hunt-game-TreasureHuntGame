class Player:
    def __init__(self, name):
        self.name = name
        self.rucksack = []
        self.current_place = None
        self.health = 100
        self.max_items = 5  # Default max items
        self.has_statue_of_immortality = False

    def move(self, place):
        if place:
            self.current_place = place
            print(f"You have moved to {self.current_place.name}")
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
        if item.name == "Health Potion":
            print("This potion will restore 50 health when used.")
        elif item.name == "Larger Backpack":
            print("This backpack allows you to carry more items.")
        elif item.name == "Fireball":
            print("This spell will instantly kill an enemy when used.")
        elif item.name == "Statue of Immortality":
            print("This statue will allow you to avoid death once.")
        elif item.name == "Gas Mask":
            print("This mask protects you from toxic gas.")
        elif item.name == "Silent Step Shoes":
            print("These shoes make you undetectable by enemies.")
        elif item.name == "Damage Potion":
            print("This potion deals 50 damage to an enemy when used.")
        elif item.name == "Magic Orb":
            print("This orb reveals information about monsters and their locations.")
        elif item.name == "Unknown Food Item":
            print("This food has unpredictable effects. Be cautious!")
        elif item.name == "Mysterious Ring":
            print("This ring helps you find hidden treasures nearby.")
        elif item.name == "Ancient Scroll":
            print("This scroll contains clues to help you navigate.")
        elif item.name == "Dagger Sharpener":
            print("This sharpener improves the effectiveness of your daggers.")

    def use_item(self, item_name):
        item = next((item for item in self.rucksack if item.name.lower() == item_name), None)
        if item:
            if item.name == "Health Potion":
                self.health += 50
                print(f"You used a Health Potion. Your health is now {self.health}.")
                self.rucksack.remove(item)
            elif item.name == "Larger Backpack":
                self.max_items += 5
                print("You used a Larger Backpack and can now carry more items.")
                self.rucksack.remove(item)
            elif item.name == "Fireball":
                print("You used a Fireball! The next enemy encounter will be an instant kill.")
                self.rucksack.remove(item)
                self.instant_kill_next_enemy()
            elif item.name == "Statue of Immortality":
                self.has_statue_of_immortality = True
                print("You used the Statue of Immortality. You can avoid death once.")
                self.rucksack.remove(item)
            elif item.name == "Gas Mask":
                print("You are now protected from toxic gas and can enter Toxic Town without losing health.")
                self.rucksack.remove(item)
            elif item.name == "Silent Step Shoes":
                print("You used the Silent Step Shoes. You can now move around without being detected by enemies.")
                self.rucksack.remove(item)
                self.become_undetectable()
            elif item.name == "Damage Potion":
                print("You used the Damage Potion. The next enemy you encounter will take 50 damage.")
                self.rucksack.remove(item)
                self.deal_damage_next_enemy()
            elif item.name == "Magic Orb":
                print("You used the Magic Orb. It reveals information about monsters and their locations.")
                self.rucksack.remove(item)
                self.reveal_monster_info()
            elif item.name == "Unknown Food Item":
                if random.choice([True, False]):
                    self.health += 50
                    print(f"You ate the Unknown Food Item. Your health is now {self.health}.")
                else:
                    self.health -= 50
                    print(f"You ate the Unknown Food Item and it was poisoned! Your health is now {self.health}.")
                self.rucksack.remove(item)
            elif item.name == "Mysterious Ring":
                print("The Mysterious Ring is vibrating. You're near a town with hidden treasures.")
                self.rucksack.remove(item)
                self.detect_hidden_treasure()
            elif item.name == "Ancient Scroll":
                print("The Ancient Scroll reveals clues that help you navigate the world more effectively.")
                self.rucksack.remove(item)
                self.reveal_navigation_clues()
            elif item.name == "Dagger Sharpener":
                print("You used the Dagger Sharpener. Your daggers are now sharper and more effective in combat.")
                self.rucksack.remove(item)
                self.sharpen_daggers()
            else:
                print(f"You used the {item.name}.")
                self.rucksack.remove(item)
        else:
            print("Item not in your rucksack.")

    def instant_kill_next_enemy(self):
        print("The next enemy will be instantly killed when encountered.")

    def become_undetectable(self):
        print("You are now undetectable by enemies for the next 5 minutes.")

    def deal_damage_next_enemy(self):
        print("The next enemy you encounter will take 50 damage.")

    def reveal_monster_info(self):
        print("The Magic Orb reveals: The dragon is in the mountains, the thief is in the desert, and the monster is in the cave.")

    def detect_hidden_treasure(self):
        print("The Mysterious Ring vibrates more intensely as you approach towns with hidden treasures.")

    def reveal_navigation_clues(self):
        print("The Ancient Scroll reveals: Follow the river to the swamp and find the secret entrance to the hidden village.")

    def sharpen_daggers(self):
        print("Your daggers are now sharper and more effective in combat.")

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
