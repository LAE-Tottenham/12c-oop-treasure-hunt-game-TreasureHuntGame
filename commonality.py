# from Locationsaver import locationsaver
# from termcolor import cprint
# from player import Player



# def noncombatopt(player):
#     while True:
#         opt = input("""
# What would you like to do?
# 1. Go to a place 
# 2. Check inventory
# 3. Consume item
# 4. Pick up an item in your location.
# 5. Exit menu
# """)
#         if opt == "1":
#             from main import locationsaverentity, currentlocationmain
#             locationsaverentity.showlocation()
#             placeselection = input("Which place would you like to go to? ")
#             locationsaverentity.placeselectionchooser(placeselection)
#         elif opt == "2":
#             print("This is the contents of your inventory: ")
#             player.printinventory()
#         elif opt == "3":
#             print("Please select an item to consume.")
#             print("If your inventory is empty, just press enter.")
#             player.printinventory()
#             itemuse = input()
#             player.use_item(itemuse)
#         # elif opt == "4":
#         #     print("Please select the item you want to pick up")
#         #     print(currentlocationmain)
#         #     itemselection = input(currentlocationmain.items + " ")
#         #     if itemselection in currentlocationmain.items:
#         #         print("You have picked up that item.")
#         #         locationsaverentity.currentlocation.items.remove()
#         if opt == "4":
#             print("Available items in this location:")
#             for item in currentlocationmain.items:
#                 cprint(item.name,"light_yellow")  # Display item names properly
#             itemselection = input("Enter the name of the item you want to pick up: ")
#             selected_item = None
#             for item in currentlocationmain.items:
#                 pickupitemvaraible = item.name
#                 if pickupitemvaraible.lower() == itemselection.lower():
#                     selected_item = item
#                     player.add_item(selected_item)  # This now has access to player
#                     currentlocationmain.items.remove(selected_item)  # Remove the item from location
#                     print(f"You have picked up {itemselection}.")
#                 else:
#                     print("Item not found.")

#         elif opt == "5":
#             print("Exiting non-combat menu...")
#             break
#         else:
#             print("You have entered an invalid option")

# def villageropt1():
#     while True:
#         opt = input("""
# What would you like to do?
# 1. Go to a place 
# 2. Check inventory
# 3. Consume item
# 4. Talk to Bill the Villager
# 5. Talk to Emily the Villager
# """)
#         if opt == "1":
#             pass
#         elif opt == "2":
#             pass
#         elif opt == "3":
#             pass
#         elif opt == "4":
#             pass
#         elif opt == "5":
#             pass
#         else:
#             pass


# def combatopt():
#     while True:
#         opt = input("""
# What would you like to do?
# 1. Attack enemy
# 2. Check inventory
# 3. Consume item
# """)
#         if opt == "1":
#             pass
#         elif opt == "2":
#             pass
#         elif opt == "3":
#             pass
#         else:
#             pass


