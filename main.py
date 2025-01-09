from typewriter import typewriter
from place import Place
from Locationsaver import locationsaver 
from player import Player
from item import Weapon, Food, Armour, Potion, SpecialItem
from termcolor import cprint

def setup():
    # here you will setup your Game
    # places
    locationsaverentity = locationsaver()
    homenonhostile = Place("Home", False)
    hayfields = Place("Hay Fields")
    village1 = Place("Village")
    Cave = Place("Cave")
    Beach = Place("Beach")
    Village2 = Place("The Second Village")
    volcano = Place("Volcano")
    enemyvillage = Place("Enemy Village")
    homehostile = Place("Home that has been taken over")
        # etc. 

        # items


        #swords
    # Swords
    RogueSword = Weapon("Rogue Sword", 0, 5, "Sword", weight=5)  # Light sword
    GildedSword = Weapon("Gilded Sword", 4, 10, "Sword", weight=8)  # Mid-tier sword
    EnchantedSword = Weapon("Enchanted Sword", 8, 14, "Sword", weight=10)  # Heavy sword
    LegendarySword = Weapon("Legendary Weapon", 12, 20, "Sword", weight=12)  # Very heavy sword

    # Bows
    RogueBow = Weapon("Rogue Bow", 0, 7, "Bow", weight=4)  # Lightweight bow
    EnchantedBow = Weapon("Enchanted Bow", 10, 16, "Bow", weight=6)  # Heavier bow

    # Food
    Apple = Food("Apple", 5, "None", weight=0.5)  # Very light food
    Steak = Food("Steak", 20, "None", weight=1.5)  # Heavier food

    # Armour
    LeatherBoots = Armour("Leather Boots", 2, weight=3)  # Light armour
    LeatherTrousers = Armour("Leather Trousers", 3, weight=5)  # Light armour
    LeatherChestplate = Armour("Leather Chestplate", 4, weight=8)  # Moderate armour
    LeatherHelmet = Armour("Leather Helmet", 3, weight=4)  # Light armour
    IronBoots = Armour("Iron Boots", 10, weight=12)  # Heavy armour
    IronLeggings = Armour("Iron Leggings", 12, weight=15)  # Heavy armour
    IronChestplate = Armour("Iron Chestplate", 15, weight=18)  # Very heavy armour
    IronHelmet = Armour("Iron Helmet", 13, weight=10)  # Heavy armour

    # Potions
    HealingPotion1 = Potion("Instant Healing Potion I", 20, "None", weight=0.2)  # Lightweight potion
    HealingPotion2 = Potion("Instant Healing Potion II", 60, "None", weight=0.3)  # Slightly heavier potion

    # Special Item
    Keyboard = SpecialItem("Keyboard", weight=1)  # Light, not much weight


    homenonhostile.add_item(Apple)
    homenonhostile.add_item(LeatherBoots)
    hayfields.add_item(RogueSword)
    hayfields.add_item(LeatherTrousers)
    village1.add_item(RogueBow)
    village1.add_item(LeatherChestplate)
    Cave.add_item(LeatherHelmet)
    Cave.add_item(HealingPotion1)


        # home will be our starting place
    # current_place = homenonhostile.name
    # locationsaverentity.locationinitialisation(homenonhostile.name)
    # currentlocationmain = locationsaverentity.currentlocation
    # return locationsaverentity, currentlocationmain
    locationsaverentity.locationinitialisation(homenonhostile.name)
    currentlocationmain = homenonhostile  # Initialize the current location to home
    return locationsaverentity, currentlocationmain, hayfields, village1, Cave, Beach, Village2,volcano, enemyvillage, homehostile 
    
        
        # finish the setup function...

def start():
    currentlocationmain = locationsaverentity.currentlocation
    havingstarted = False
    while havingstarted == False:
        checkerstart = input("Press Enter to begin")
        if checkerstart == "":
            havingstarted = True
        else:
            havingstarted = True
    cprint("Welcome to my game John Valley", "green")
    print("You find yourself at your own home, finally able to leave the comfort of your own home.")
    name = input("Enter player name: ")
    player = Player(name)
    cprint("You are currently at Home","yellow")
    typewriter("Sunlight streams through the small window, painting the wooden floor in golden light. Birds chirp outside, and the sound of rustling leaves stirs you from sleep.")
    typewriter("As your eyes open, you see your modest room: shelves with trinkets, a sturdy wardrobe, and herbs drying by the windowsill.")
    typewriter("You stretch, shaking off the last traces of sleep. The woolen blanket tempts you to stay, but the thought of the bustling town pulls you from bed. Today isn’t a day to waste.")
    typewriter("You swing your legs over the edge of the bed, your feet touching the cool wooden floor. After a quick splash of water from the basin. Your feet are cold. You see your boots in the corner of the room.")
    print("    ")
    cprint(" Enter in 4 to pick up the item.", "yellow")
    cprint(" When done, enter in 5 to finish.", "yellow")
    cprint(" Note that you will not be able to pick up the item unless you come back here in the future.", "red")
    noncombatopt(player)  # Pass the player object here
    typewriter("A growl from your stomach reminds you of the baker’s fresh bread waiting in the town square.")
    cprint(" Pick up the apple now. If you have already picked it up, then exit the menu.", "yellow")
    cprint(" Note that you will not be able to pick up the item unless you come back here in the future.", "red")
    noncombatopt(player)
    typewriter("You now walk down the stairs and outside the House, heading towards the hayfields that lie outside your home.")
    cprint("You have now unlocked the location Hay Fields, and have completed the first tutorial.", "yellow")
    locationsaverentity.locationinitialisation(hayfields)
    print("DEBUG")
    return player


def noncombatopt(player):
    while True:
        opt = input("""
What would you like to do?
1. Go to a place 
2. Check inventory
3. Consume item
4. Pick up an item in your location.
5. Exit menu
""")
        if opt == "1":
            locationsaverentity.showlocation()
            placeselection = input("Which place would you like to go to? ")
            locationsaverentity.placeselectionchooser(placeselection)
        elif opt == "2":
            print("This is the contents of your inventory: ")
            player.printinventory()
        elif opt == "3":
            print("Please select an item to consume.")
            print("If your inventory is empty, just press enter.")
            player.printinventory()
            itemuse = input()
            player.use_item(itemuse)
        # elif opt == "4":
        #     print("Please select the item you want to pick up")
        #     print(currentlocationmain)
        #     itemselection = input(currentlocationmain.items + " ")
        #     if itemselection in currentlocationmain.items:
        #         print("You have picked up that item.")
        #         locationsaverentity.currentlocation.items.remove()
        elif opt == "4":
            print("Available items in this location:")
            for item in currentlocationmain.items:
                cprint(item.name,"light_yellow")  # Display item names properly
            itemselection = input("Enter the name of the item you want to pick up: ")
            selected_item = None
            for item in currentlocationmain.items:
                pickupitemvaraible = item.name
                if pickupitemvaraible.lower() == itemselection.lower():
                    selected_item = item
                    player.add_item(selected_item)  # This now has access to player
                    currentlocationmain.items.remove(selected_item)  # Remove the item from location
                    print(f"You have picked up {itemselection}.")
                else:
                    print("Item not found.")

        elif opt == "5":
            print("Exiting non-combat menu...")
            break
        else:
            print("You have entered an invalid option DEBUG")

def villageropt1():
    while True:
        opt = input("""
What would you like to do?
1. Go to a place 
2. Check inventory
3. Consume item
4. Talk to Bill the Villager
5. Talk to Emily the Villager
""")
        if opt == "1":
            pass
        elif opt == "2":
            pass
        elif opt == "3":
            pass
        elif opt == "4":
            pass
        elif opt == "5":
            pass
        else:
            pass


def combatopt():
    while True:
        opt = input("""
What would you like to do?
1. Attack enemy
2. Check inventory
3. Consume item
""")
        if opt == "1":
            pass
        elif opt == "2":
            pass
        elif opt == "3":
            pass
        else:
            pass








# RUN SETUP DO NOT TOUCH


locationsaverentity, currentlocationmain, hayfields, village1, Cave, Beach, Village2,volcano, enemyvillage, homehostile = setup()
player = start()
noncombatopt(player)