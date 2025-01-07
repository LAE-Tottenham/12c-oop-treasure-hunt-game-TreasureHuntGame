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
    RogueSword = Weapon("Rogue Sword", 0, 5, "Sword")
    GildedSword = Weapon("Gilded Sword", 4, 10, "Sword")
    EnchantedSword = Weapon("Enchanted Sword", 8, 14, "Sword")
    LegendarySword = Weapon("Legendary Weapon", 12, 20, "Sword")

        #bows
    RogueBow = Weapon("Rogue Bow", 0, 7, "Bow")
    EnchantedBow = Weapon("Enchanted Bow", 10, 16, "Bow")

        #food
    Apple = Food("Apple", 5, "None")
    Steak = Food("Steak", 20, "None")

        #armour
    LeatherBoots = Armour("Leather Boots", 2)
    LeatherTrousers = Armour("Leather Trousers", 3)
    LeatherChestplate = Armour("Leather Chestplate", 4)
    LeatherHelmet = Armour("Leather Helmet", 3)
    IronBoots = Armour("Iron Boots", 10)
    IronLeggings = Armour("Iron Leggings", 12)
    IronChestplate = Armour("Iron Chestplate", 15)
    IronHelmet = Armour("Iron Helmet", 13)

        #potions
    HealingPotion1 = Potion("Instant Healing Potion I", 20, "None")
    HealingPotion2 = Potion("Instant Healing Potion II", 60, "None")

        #specialitem
    Keyboard = SpecialItem("Keyboard")

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
    locationsaverentity.locationinitialisation(homenonhostile.name)
    currentlocationmain = locationsaverentity.currentlocation
    return locationsaverentity, currentlocationmain
    
        
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
    cprint(" Enter in 4 to pick up the item.", "yellow")
    cprint(" When done, enter in 5 to finish.")
    noncombatopt()
    typewriter("A growl from your stomach reminds you of the baker’s fresh bread waiting in the town square.")
    # typewriter("")
    # typewriter("")
    return player

def noncombatopt():
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
        elif opt == "4":
            print("Please select the item you want to pick up")
            print(currentlocationmain)
            itemselection = input(currentlocationmain.items + " ")
            if itemselection in currentlocationmain.items:
                print("You have picked up that item.")
                locationsaverentity.currentlocation.items.remove()

        elif opt == "5":
            print("Exiting non-combat menu...")
            break
        else:
            print("You have entered an invalid option")

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


locationsaverentity, currentlocationmain = setup()
player = start()
noncombatopt()
