from place import Place, nextplaces, placeselectionchooser
from player import Player
from item import Weapon, Food, Armour, Potion, SpecialItem
from termcolor import cprint

def setup():
    # here you will setup your Game
    # places
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

        # home will be our starting place
    current_place = homenonhostile.name
    nextplaces.append(homenonhostile.name)
    return current_place
    
        
        # finish the setup function...

def start():
    havingstarted = False
    while havingstarted == False:
        checkerstart = input("Press Enter to begin")
        if checkerstart == "":
            havingstarted = True
        else:
            pass
    cprint("Welcome to my game John Valley", "green")
    print("You find yourself at your own home, finally able to leave the comfort of your own home.")
    name = input("Enter player name: ")
    player = Player(name)

    print("You are currently in " + CurrentPlace)
        
def noncombatopt():
    opt = input("""
What would you like to do?
1. Go to a place
2. Pickup item
3. Check inventory
4. Consume item
""")
    if opt == "1":
        print("Here are the following places you can currently travel to:")
        print(nextplaces)
        placeselection = input("Which place would you like to go to? ")
        placeselectionchooser(placeselection)
        pass
    elif opt == "2":
        # add code
        pass
    elif opt == "3":
        # add code
        pass


CurrentPlace = setup()
start()
noncombatopt()