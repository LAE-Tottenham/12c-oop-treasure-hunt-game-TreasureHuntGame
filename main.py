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
    return locationsaverentity
    
        
        # finish the setup function...

def start():
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
    return player
        
def noncombatopt():
    while True:
        opt = input("""
What would you like to do?
1. Go to a place 
2. Check inventory
3. Consume item
""")
        if opt == "1":
            locationsaverentity.showlocation()
            placeselection = input("Which place would you like to go to? ")
            locationsaverentity.placeselectionchooser(placeselection)
        elif opt == "2":
            player.printinventory()
        elif opt == "3":
            print("Please select an item to consume.")
            player.printinventory
            itemuse = input()
            player.use_item(itemuse)

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
        if opt == "2":
            pass
        if opt == "3":
            pass
        if opt == "4":
            pass
        if opt == "5":
            pass











# RUN SETUP DO NOT TOUCH


locationsaverentity = setup()
player = start()
noncombatopt()
