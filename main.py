from typewriter import typewriter
from place import Place
from Locationsaver import locationsaver
from player import Player
from item import Weapon, Food, Armour, Potion, SpecialItem
from termcolor import cprint
from entity import Wolf, NPC, Shop
from combat import combat

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

    locationsaverentity.all_location_append(homenonhostile)
    locationsaverentity.all_location_append(hayfields)
    locationsaverentity.all_location_append(village1)
    locationsaverentity.all_location_append(cave)
    
    # Add items to locations
    apple = Food("Apple", 5, "None", weight=0.5)
    leather_boots = Armour("Leather Boots", 2, weight=3)
    rogue_sword = Weapon("Rogue Sword", 0, 5, "Sword", weight=5)
    leather_trousers = Armour("Leather Trousers", 3, weight=5)
    rogue_bow = Weapon("Rogue Bow", 0, 7, "Bow", weight=4)
    leather_chestplate = Armour("Leather Chestplate", 4, weight=8)
    leather_helmet = Armour("Leather Helmet", 3, weight=4)
    healing_potion_1 = Potion("Instant Healing Potion I", 20, "None", weight=0.2)
    HealingPotion2 = Potion("Instant Healing Potion II", 60, "None", weight=0.3)  # Slightly heavier potion
    IronBoots = Armour("Iron Boots", 10, weight=12)  # Heavy armour
    IronLeggings = Armour("Iron Leggings", 12, weight=15)  # Heav
    IronChestplate = Armour("Iron Chestplate", 15, weight=18)  # Very heavy armour
    IronHelmet = Armour("Iron Helmet", 13, weight=10)  # Heavy armour
    Keyboard = SpecialItem("Keyboard", weight=1)  # Light, not much weight
    Steak = Food("Steak", 20, "None", weight=1.5)  # Heavier food
    EnchantedBow = Weapon("Enchanted Bow", 10, 16, "Bow", weight=6)  # Heavier bow
    GildedSword = Weapon("Gilded Sword", 4, 10, "Sword", weight=8)  # Mid-tier sword
    EnchantedSword = Weapon("Enchanted Sword", 8, 14, "Sword", weight=10)  # Heavy sword
    LegendarySword = Weapon("Legendary Weapon", 12, 20, "Sword", weight=12)  # Very heavy sword


    homenonhostile.add_item(apple)
    homenonhostile.add_item(leather_boots)
    hayfields.add_item(rogue_sword)
    hayfields.add_item(leather_trousers)
    village1.add_item(rogue_bow)
    village1.add_item(leather_chestplate)
    cave.add_item(leather_helmet)
    cave.add_item(healing_potion_1)

    prices = {
        "Steak": 10,
        "Gilded Sword": 50,
        "Instant Healing Potion I": 25
    }
    shop = Shop([Steak,GildedSword,healing_potion_1], prices)
    

    # Set the initial location
    locationsaverentity.locationinitialisation(homenonhostile.name)
    currentlocationmain = homenonhostile
    hayfields.story = lambda: hayfields_story(player, hayfields, Keyboard, currentlocationmain)
    village1.story = lambda: village1_story(village1)
    return locationsaverentity, currentlocationmain, hayfields, village1, cave, beach, village2, volcano, enemyvillage, homehostile, Keyboard, shop
    
        
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

def hayfields_story(player, hayfields,keyboard, currentlocationmain):
    typewriter("You step into the golden Hay Fields...")
    typewriter("The sun warms your skin as you hear the rustle of tall grass.")
    typewriter("A strange feeling fills the air. You notice something glinting among the grass.")
    print("1. Investigate the glint.")
    print("2. Ignore it and move on.")
    choice = input("What do you do? ")
    if choice == "1":
        typewriter("You approach and find a small, ornate keyboard. It might be useful later.")
        typewriter("Suddenly, you hear a low growl behind you. A wild wolf emerges from the grass, baring its teeth!")
        combat_result = combat(player, Wolf())  # Create an instance of the Wolf class
        if combat_result == True:
            typewriter("You have defeated the wolf and survived the encounter!")
            typewriter("Feeling emboldened, you continue your journey through the Hay Fields.")
            player.add_item(keyboard)
            player.currency += 50
        else:
            typewriter("The wolf's attack overwhelms you. You collapse, unable to continue.")
            typewriter("The wolf leaves you alone miraculously.")
    elif choice == "2":
        typewriter("You decide not to investigate. Perhaps it wasn’t important.")
    else:
        typewriter("You hesitate and decide to move on.")
    typewriter("The Hay Fields stretch endlessly, but you feel you've overcome its challenges for now.")
    currentlocationmain = locationsaverentity.location_unlocker(village1, currentlocationmain)
    return currentlocationmain


def village1_story(village):
    """
    Handles the story events when the player arrives at the first village.
    This story can be skipped if the player has already experienced it.
    """
    if village.storycompletion:
        print("You have already visited the village and encountered the Dark Collector.")
        return  # Skips the story if the story has already been completed for this place

    # If the player hasn't completed the story yet, proceed with the story
    typewriter("After a long journey, you arrive at a small, bustling village nestled between rolling hills.")
    typewriter("The sounds of chatter, clinking tools, and merchants haggling fill the air.")
    typewriter("You notice villagers running toward the town square, shouting in alarm.")

    typewriter("Curious and concerned, you follow the crowd and find yourself in the middle of the square.")
    typewriter("There, a tall figure clad in dark, flowing robes stands atop a cart, holding a gleaming chest of jewels.")
    typewriter("The villagers cry out, pleading for the figure to return the stolen treasure.")

    typewriter("The figure turns to face the crowd. Their face is hidden behind a mask, but their presence radiates power.")
    typewriter("With a booming voice, the figure declares, 'These jewels are mine now. Your wealth will serve a greater purpose!'")
    typewriter("Before anyone can act, the figure raises a hand. A swirl of black smoke engulfs them and the chest.")

    typewriter("When the smoke clears, the figure is gone, leaving only the villagers' despair behind.")
    typewriter("You notice an elderly man sitting on the steps of the town hall, his head in his hands.")
    typewriter("Approaching him, you ask, 'Who was that?'")

    typewriter("The man looks up at you, his eyes filled with sorrow. 'That was Morvan, the Dark Collector. He preys on villages like ours, stealing our wealth and leaving us to struggle.'")
    typewriter("'No one knows where he hides, but some say he has a lair deep in the Cursed Forest beyond the mountains.'")

    typewriter("You clench your fists, feeling a surge of determination. You know this is only the beginning of your journey.")
    typewriter("The villagers thank you for listening, and the elder offers you a small token: a map of the surrounding lands.")
    typewriter("'Take this,' he says. 'It may guide you to places where you can grow stronger and find allies.'")

    typewriter("With the map in hand and a new sense of purpose, you prepare to leave the village, vowing to stop Morvan and recover the stolen jewels.")

    # Mark the village story as completed
    village.storycompletion = True
    villageropt1(shopkeeper)


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
            currentlocationmain = locationsaverentity.placeselectionchooser(placeselection)
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

def villageropt1(shopkeeper):
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
            locationsaverentity.showlocation()
            placeselection = input("Which place would you like to go to? ")
            currentlocationmain = locationsaverentity.placeselectionchooser(placeselection)
        elif opt == "2":
            player.printinventory()
        elif opt == "3":
            itemuse = input("Enter the name of the item to consume: ")
            player.use_item(itemuse)
        elif opt == "4":
            shopkeeper.interact(player)
            print(player.currency)
        elif opt == "5":
            pass
        else:
            pass









# RUN SETUP DO NOT TOUCH


locationsaverentity, currentlocationmain, hayfields, village1, Cave, Beach, Village2,volcano, enemyvillage, homehostile, keyboard, shop = setup()
shopkeeper = NPC("Bill", shop)
player, currentlocationmain = start(locationsaverentity, currentlocationmain)
noncombatopt(player, currentlocationmain, locationsaverentity)

