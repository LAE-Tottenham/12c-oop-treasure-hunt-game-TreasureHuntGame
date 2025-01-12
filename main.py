from place import Place
from player import Player
from item import Item
import time
import random
class Person:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

class Enemy:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

forest = Place("Forest", "A dark, dense forest with tall trees.")
castle = Place("Castle", "A grand castle with towering walls.")
secret_room = Place("Secret Room", "A hidden room within the castle with a riddle to solve.")
lake = Place("Lake", "A serene lake with crystal clear water.")
cave = Place("Cave", "A dark, mysterious cave.")
village = Place("Village", "A quaint village with friendly inhabitants.")
mountain = Place("Mountain", "A towering mountain with snow-capped peaks.")
desert = Place("Desert", "A vast, arid desert with scorching sun.")
river = Place("River", "A flowing river with cool, refreshing water.")
swamp = Place("Swamp", "A murky swamp with dense vegetation.")
plains = Place("Plains", "Vast, open plains with tall grass.")
toxic_town = Place("Toxic Town", "A town filled with toxic gas and higher-tier loot.")


secret_room.connect("west",castle)
forest.connect("east", castle)
castle.connect("south", forest)
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
desert.connect("north", toxic_town)
toxic_town.connect("south", desert)


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
silent_step_shoes = Item("Silent Step Shoes", 1)
health_potion = Item("Health Potion", 1)
map = Item("Map", 1)
gas_mask = Item("Gas Mask", 2)
golden_trophy = Item("Golden Trophy", 5)


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
secret_room.add_item(gas_mask)
swamp.add_item(silent_step_shoes)
toxic_town.add_item(golden_trophy)


guard = Person("Guard", "You need a key to enter the secret room.")
villager = Person("Villager", "Welcome to our village! We could use a hero like you.")
monster = Enemy("Monster", 20)
thief = Enemy("Thief", 15)
dragon = Enemy("Dragon", 50)


castle.add_person(guard)
village.add_person(villager)
cave.add_enemy(monster)
desert.add_enemy(thief)
mountain.add_enemy(dragon)


player_name = input("Enter your hero's name: ")


player = Player(player_name, secret_room, castle)
player.move(forest)

print(f"\nWelcome, {player_name}!")
print("You stand at the edge of the Mystic Forest, a place of legend filled with untold secrets and lurking dangers.")
print("Your quest is to brave the wild, battle ferocious foes, and seize the Everlasting Treasure hidden deep within the Castle of Arkamor.")
print(f"Arm yourself, {player_name}, and let the adventure begin!\n")

def solve_riddle():
    print("\nRiddle: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    attempts = 3
    while attempts > 0:
        answer = input("Your answer: ").strip().lower()
        if answer == "echo":
            print("Correct! You may now pick up the gas mask.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect. You have {attempts} attempts left.")
    print("You failed to solve the riddle. You cannot take the gas mask.")
    return False

def toxic_town_death_sequence():
    if any(item.name == "Gas Mask" for item in player.rucksack):
        print("Your Gas Mask protects you from the toxic gas. You can safely explore Toxic Town.")
        return  

    print("The toxic gas starts affecting you...")
    for i in range(10, 0, -1):
        player.health -= 10
        print(f"Health: {player.health} | Time left: {i} seconds")
        time.sleep(1)
        if player.health <= 0:
            print("You have succumbed to the toxic gas. Game over!")
            exit()

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
        print(f"Description: {player.current_place.description}")
        player.current_place.display()

        directions = ", ".join([f"{direction.capitalize()}: {place.name}" for direction, place in player.current_place.connected_places.items()])
        print(f"You can go: {directions}")

        command = input("What do you want to do next? (move [direction], pick up [item], interact with [person], fight [enemy], use [item], status, check rucksack, quit): ").lower()

        if command == "quit":
            print("Thank you for playing! Goodbye!")
            break

        elif command.startswith("move "):
            direction = command.split("move ")[1]
            if direction in player.current_place.connected_places:
                next_place = player.current_place.connected_places[direction]
                player.move(next_place)
                if next_place == toxic_town:
                    toxic_town_death_sequence()
            else:
                print("You can't go that way.")

        elif command.startswith("pick up "):
            item_name = command.split("pick up ")[1]
            item = next((item for item in player.current_place.items if item.name.lower() == item_name), None)
            if item:
                if item.name == "Gas Mask" and player.current_place == secret_room:
                    if solve_riddle():
                        player.pick_up(item)
                        player.current_place.items.remove(item)
                    else:
                        print("You cannot pick up the gas mask.")
                elif item.name == "Golden Trophy":

                    player.pick_up(item)
                    print("Congratulations! You have obtained the Golden Trophy, marking the end of your epic quest!")
                    print("Thank you for playing! The game is now complete. Well done, hero!")
                    break
                else:
                    player.pick_up(item)
                    player.current_place.items.remove(item)
            else:
                print("Item not found.")

        elif command.startswith("interact with "):
            person_name = command.split("interact with ")[1]
            person = next((person for person in player.current_place.people if person.name.lower() == person_name), None)
            if person:
                if person.name.lower() == "guard" and any(item.name == "Key" for item in player.rucksack):
                    print("You showed the Key to the guard and entered the Secret Room.")
                    player.move(secret_room)
                else:
                    print(person.dialogue)
            else:
                print("Person not found.")

        elif command.startswith("fight "):
            enemy_name = command.split("fight ")[1]
            enemy = next((enemy for enemy in player.current_place.enemies if enemy.name.lower() == enemy_name), None)
            if enemy:
                print(f"You are fighting {enemy.name}!")
                while enemy.strength > 0 and player.health > 0:
                    print(f"The {enemy.name} attacks!")
                    player.health -= random.randint(5, 15)
                    print(f"Your health is now {player.health}.")

                    if player.health <= 0:
                        print(f"The {enemy.name} has defeated you.")
                        break

                    print(f"You strike the {enemy.name}.")
                    enemy.strength -= random.randint(10, 20)
                    print(f"The {enemy.name}'s strength is now {enemy.strength}.")

                if enemy.strength <= 0:
                    print(f"You defeated the {enemy.name}!")
                    player.current_place.enemies.remove(enemy)
            else:
                print("Enemy not found.")

        elif command.startswith("use "):
            item_name = command.split("use ")[1]
            player.use_item(item_name)

        elif command == "status":
            player.display_status()

        elif command == "check rucksack":
            player.check_rucksack()

        else:
            print("Invalid command.")


game_loop()