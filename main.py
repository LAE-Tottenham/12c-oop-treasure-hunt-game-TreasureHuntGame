from place import Place
from player import Player
from item import Item

class Person:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

class Enemy:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
# Create places
forest = Place("Forest", "A dark, dense forest with tall trees.")
castle = Place("Castle", "A grand castle with towering walls.")
lake = Place("Lake", "A serene lake with crystal clear water.")
cave = Place("Cave", "A dark, mysterious cave.")
village = Place("Village", "A quaint village with friendly inhabitants.")
mountain = Place("Mountain", "A towering mountain with snow-capped peaks.")
desert = Place("Desert", "A vast, arid desert with scorching sun.")
river = Place("River", "A flowing river with cool, refreshing water.")
swamp = Place("Swamp", "A murky swamp with dense vegetation.")
plains = Place("Plains", "Vast, open plains with tall grass.")
toxic_town = Place("Toxic Town", "A town filled with toxic gas and higher-tier loot.")  # Add Toxic Town

# Connect places
forest.connect("east", castle)
castle.connect("west", forest)
castle.connect("north", lake)
lake.connect("south", castle)
forest.connect("north", village)
village.connect("south", forest)
village.connect("north", mountain)
mountain.connect("south", village)
castle.connect("west", cave)
cave.connect("east", castle)
mountain.connect("east", desert)
desert.connect("west", mountain)
river.connect("east", swamp)
swamp.connect("west", river)
plains.connect("east", forest)
plains.connect("west", river)
desert.connect("north", toxic_town)  # Connect Toxic Town
toxic_town.connect("south", desert)  # Add connection for Toxic Town

# Create items
key = Item("Key", 1)
sword = Item("Sword", 5)
blunt_dagger = Item("Blunt Dagger", 3)
sharp_dagger = Item("Sharp Dagger", 2)
magic_wand = Item("Magic Wand", 4)
dagger_sharpener = Item("Dagger Sharpener", 1)
mysterious_ring = Item("Mysterious Ring", 1)
shield = Item("Shield", 5)
larger_backpack = Item("Larger Backpack", 0)
ancient_scroll = Item("Ancient Scroll", 1)
statue_of_immortality = Item("Statue of Immortality", 10)
fireball = Item("Fireball", 1)
magic_orb = Item("Magic Orb", 3)
damage_potion = Item("Damage Potion", 2)
unknown_food_item = Item("Unknown Food Item", 1)
gas_mask = Item("Gas Mask", 2)
silent_step_shoes = Item("Silent Step Shoes", 1)
health_potion = Item("Health Potion", 1)
map = Item("Map", 1)

# Add items to places
forest.add_item(key)
castle.add_item(sword)
village.add_item(shield)
cave.add_item(health_potion)
lake.add_item(map)
forest.add_item(mysterious_ring)
cave.add_item(dagger_sharpener)
mountain.add_item(sharp_dagger)
castle.add_item(blunt_dagger)
village.add_item(ancient_scroll)
swamp.add_item(statue_of_immortality)
river.add_item(magic_wand)
plains.add_item(fireball)
village.add_item(magic_orb)
desert.add_item(damage_potion)
lake.add_item(unknown_food_item)
desert.add_item(gas_mask)
swamp.add_item(silent_step_shoes)

# Create people and enemies
guard = Person("Guard", "You need a key to enter the castle.")
villager = Person("Villager", "Welcome to our village!")
monster = Enemy("Monster", 20)
thief = Enemy("Thief", 15)
dragon = Enemy("Dragon", 50)

# Add people and enemies to places
castle.add_person(guard)
village.add_person(villager)
cave.add_enemy(monster)
desert.add_enemy(thief)
mountain.add_enemy(dragon)

# Get player information
player_name = input("Enter your hero's name: ")

# Initialize player and move to the starting location
player = Player(player_name)
player.move(forest)

# Introduce the storyline
print(f"\nWelcome, {player_name}!")
print("You stand at the edge of the Mystic Forest, a place of legend filled with untold secrets and lurking dangers.")
print("Your quest is to brave the wild, battle ferocious foes, and seize the Everlasting Treasure hidden deep within the Castle of Arkamor.")
print(f"Arm yourself, {player_name}, and let the adventure begin!\n")
import time

def game_loop():
    while True:
        if player.health <= 0:
            if player.has_statue_of_immortality:
                player.has_statue_of_immortality = False
                player.health = 50
                print("The Statue of Immortality saved you from death! Your health is now 50.")
            else:
                print("You have been defeated. Game over!")
                break
        print(f"\nCurrent Location: {player.current_place.name}")
        player.current_place.display()

        print("You can go to:")
        for direction, place in player.current_place.connected_places.items():
            print(f"{direction}: {place.name}")

        command = input("What do you want to do next? (move [direction], pick up [item], interact with [person], fight [enemy], use [item], look, status, check rucksack, solve riddle, quit): ").lower()
        if command == "quit":
            print("Thank you for playing! Goodbye!")
            break
        elif command.startswith("move "):
            direction = command.split("move ")[1]
            if direction in player.current_place.connected_places:
                player.move(player.current_place.connected_places[direction])
            else:
                print("You can't go that way.")
        elif command.startswith("pick up "):
            item_name = command.split("pick up ")[1]
            item = next((item for item in player.current_place.items if item.name.lower() == item_name), None)
            if item:
                player.pick_up(item)
                player.current_place.items.remove(item)
            else:
                print("Item not found.")
        elif command.startswith("interact with "):
            person_name = command.split("interact with ")[1]
            person = next((person for person in player.current_place.people if person.name.lower() == person_name), None)
            if person:
                player.interact(person)
            else:
                print("Person not found.")
        elif command.startswith("fight "):
            enemy_name = command.split("fight ")[1]
            enemy = next((enemy for enemy in player.current_place.enemies if enemy.name.lower() == enemy_name), None)
            if enemy:
                player.fight(enemy)
            else:
                print("Enemy not found.")
        elif command.startswith("use "):
            item_name = command.split("use ")[1]
            player.use_item(item_name)
        elif command.startswith("solve riddle"):
            if player.current_place.name == "Secret Room":
                riddle_answer = input("Solve this riddle to unlock the treasure. What has keys but can’t open locks?: ").lower()
                if riddle_answer == "piano":
                    print("Correct! A hidden treasure chest appears before you.")
                    treasure_chest = Item("Treasure Chest", 50)
                    player.current_place.add_item(treasure_chest)
                else:
                    print("Wrong answer. Try again.")
            else:
                print("There is no riddle to solve here.")
        elif command == "look":
            player.current_place.display()
        elif command == "status":
            player.display_status()
        elif command == "check rucksack":
            player.check_rucksack()
        elif command == "help":
            print("Available commands: move [direction], pick up [item], interact with [person], fight [enemy], use [item], look, status, check rucksack, solve riddle, quit.")
        else:
            print("I don't understand that command.")

game_loop()
