import random
from place import Place
from Locationsaver import locationsaver
from player import Player
from item import Weapon

def combat(player, enemy):
    print(f"Combat started! You are fighting a {enemy.name}.")
    print(f"{enemy.name}'s health: {enemy.health}")
    print(f"Your health: {player.health}")

    while player.health > 0 and enemy.health > 0:
        print("\nYour Turn:")
        print("1. Attack")
        print("2. Use Item")
        action = input("Choose your action: ")

        if action == "1":
            # Attack
            weapon = None
            for item in player.inventory:
                if isinstance(item, Weapon):  # Check if the item is a weapon
                    weapon = item
                    break

            if weapon:
                damage = random.randint(weapon.rangelb, weapon.rangeub)
                enemy.health -= damage
                print(f"You attacked with {weapon.name}, dealing {damage} damage!")
            else:
                damage = random.randint(5, 10)  # Default attack damage
                enemy.health -= damage
                print(f"You attacked with your fists, dealing {damage} damage!")
            
            if enemy.health <= 0:
                print(f"You defeated the {enemy.name}!")
                return True  # Victory
        elif action == "2":
            # Use Item
            if not player.inventory:
                print("Your inventory is empty!")
            else:
                print("Inventory:")
                for idx, item in enumerate(player.inventory):
                    print(f"{idx + 1}. {item.name} (Weight: {item.weight})")
                choice = input("Choose an item to use: ")
                if choice.isdigit() and 1 <= int(choice) <= len(player.inventory):
                    chosen_item = player.inventory[int(choice) - 1]
                    if hasattr(chosen_item, "healamount"):  # Check if it's consumable
                        player.use_item(chosen_item)
                    else:
                        print(f"{chosen_item.name} cannot be used in combat.")
                else:
                    print("Invalid choice.")
        else:
            print("Invalid action. Try again.")

        # Enemy Turn
        if enemy.health > 0:
            enemy_damage = random.randint(enemy.damagelb, enemy.damageub)
            player.health -= enemy_damage
            print(f"The {enemy.name} attacked you, dealing {enemy_damage} damage!")
            print(f"Your health: {player.health}")

            if player.health <= 0:
                print("You have been defeated!")
                return False  # Defeat

    return False
