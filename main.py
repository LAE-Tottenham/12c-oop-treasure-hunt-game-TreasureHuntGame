from typewriter import typewriter
from place import Place
from Locationsaver import locationsaver
from player import Player
from item import Weapon, Food, Armour, Potion, SpecialItem
from termcolor import cprint

def setup():
    # Initialize game locations
    locationsaverentity = locationsaver()
    homenonhostile = Place("Home", False)
    hayfields = Place("Hay Fields")
    village1 = Place("Village")
    cave = Place("Cave")
    beach = Place("Beach")
    village2 = Place("The Second Village")
    volcano = Place("Volcano")
    enemyvillage = Place("Enemy Village")
    homehostile = Place("Home that has been taken over")
    
    # Add items to locations
    apple = Food("Apple", 5, "None", weight=0.5)
    leather_boots = Armour("Leather Boots", 2, weight=3)
    rogue_sword = Weapon("Rogue Sword", 0, 5, "Sword", weight=5)
    leather_trousers = Armour("Leather Trousers", 3, weight=5)
    rogue_bow = Weapon("Rogue Bow", 0, 7, "Bow", weight=4)
    leather_chestplate = Armour("Leather Chestplate", 4, weight=8)
    leather_helmet = Armour("Leather Helmet", 3, weight=4)
    healing_potion_1 = Potion("Instant Healing Potion I", 20, "None", weight=0.2)
    
    homenonhostile.add_item(apple)
    homenonhostile.add_item(leather_boots)
    hayfields.add_item(rogue_sword)
    hayfields.add_item(leather_trousers)
    village1.add_item(rogue_bow)
    village1.add_item(leather_chestplate)
    cave.add_item(leather_helmet)
    cave.add_item(healing_potion_1)

    # Set the initial location
    locationsaverentity.locationinitialisation(homenonhostile.name)
    currentlocationmain = homenonhostile
    return locationsaverentity, currentlocationmain, hayfields, village1, cave, beach, village2, volcano, enemyvillage, homehostile
    
        
        # finish the setup function...

def start(locationsaverentity, currentlocationmain):
    havingstarted = False
    while not havingstarted:
        checkerstart = input("Press Enter to begin: ")
        if checkerstart == "":
            havingstarted = True

    cprint("Welcome to my game, John Valley", "green")
    print("You find yourself at your own home, finally able to leave the comfort of your own home.")
    name = input("Enter player name: ")
    player = Player(name)
    
    cprint("You are currently at Home", "yellow")
    typewriter("Sunlight streams through the small window, painting the wooden floor in golden light...")
    typewriter("A growl from your stomach reminds you of the baker’s fresh bread waiting in the town square.")
    
    # Pass arguments to noncombatopt
    noncombatopt(player, currentlocationmain, locationsaverentity)
    
    typewriter("You now walk down the stairs and outside the House, heading towards the hayfields.")
    cprint("You have now unlocked the location Hay Fields, and have completed the first tutorial.", "yellow")
    
    currentlocationmain = locationsaverentity.location_unlocker(hayfields, currentlocationmain)
    return player, currentlocationmain

def hayfields_story(player, hayfields):
    typewriter("You step into the golden Hay Fields...")
    typewriter("The sun warms your skin as you hear the rustle of tall grass.")
    typewriter("A strange feeling fills the air. You notice something glinting among the grass.")
    print("1. Investigate the glint.")
    print("2. Ignore it and move on.")
    choice = input("What do you do? ")
    if choice == "1":
        typewriter("You approach and find a small, ornate key. It might be useful later.")
        player.add_item(SpecialItem("Ornate Key"))
    elif choice == "2":
        typewriter("You decide not to investigate. Perhaps it wasn’t important.")
    else:
        typewriter("You hesitate and decide to move on.")


def noncombatopt(player, currentlocationmain, locationsaverentity):
    while True:
        opt = input("""
What would you like to do?
1. Go to a place
2. Check inventory
3. Consume item
4. Pick up an item in your location
5. Exit menu
""")
        if opt == "1":
            locationsaverentity.showlocation()
            placeselection = input("Which place would you like to go to? ")
            currentlocationmain = locationsaverentity.placeselectionchooser(placeselection, currentlocationmain)
        elif opt == "2":
            player.printinventory()
        elif opt == "3":
            itemuse = input("Enter the name of the item to consume: ")
            player.use_item(itemuse)
        elif opt == "4":
            print("Available items in this location:")
            for item in currentlocationmain.items:
                cprint(item.name, "light_yellow")
            itemselection = input("Enter the name of the item you want to pick up: ")
            selected_item = next((item for item in currentlocationmain.items if item.name.lower() == itemselection.lower()), None)
            if selected_item:
                player.add_item(selected_item)
                currentlocationmain.items.remove(selected_item)
                print(f"You picked up {selected_item.name}.")
            else:
                print("Item not found.")
        elif opt == "5":
            print("Exiting non-combat menu...")
            break
        else:
            print("Invalid option. Please try again.")

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
player, currentlocationmain = start(locationsaverentity, currentlocationmain)
noncombatopt(player, currentlocationmain, locationsaverentity)

