class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.inventory_max_weight = 50
        self.inventory = []
        # add more atributes as needed

    # def calculate_inventory_size(self):
    #     total = 0
    #     for i in self.inventory:
    #         total = total + i.weight
    #     self.weight = i.weight
    #     pass

    def calculate_inventory_size(self):
        total = 0
        for item in self.inventory:
            if hasattr(item, 'weight'):
                total += item.weight  # Ensure the item has a weight attribute
        return total


    # def add_item(self, item_instance):
    #     if self.calculate_inventory_size() > self.inventory_max_weight:
    #         self.inventory.append(item_instance)
    #     else:
    #         print("Your inventory is full...")

    def add_item(self, item_instance):
        if self.calculate_inventory_size() + item_instance.weight <= self.inventory_max_weight:
            self.inventory.append(item_instance)
            print(f"Added {item_instance.name} to inventory.")
        else:
            print("Your inventory is full...")


    # def use_item(self, item_instance):
    #     itemuseselectionconfirmation = False
    #     while itemuseselectionconfirmation == False:
    #         if hasattr(item_instance, 'type') and hasattr(item_instance, 'healamount'):
    #             if item_instance.type == "food":
    #                 self.health += item_instance.healamount
    #                 self.inventory.remove(item_instance)
    #                 itemuseselectionconfirmation = True
    #             elif item_instance.type == "potion":
    #                 self.health += item_instance.healamount
    #                 self.inventory.remove(item_instance)
    #                 itemuseselectionconfirmation = True
    #             else:
    #                 print("The item you have entered does not exist. Please choose again")
    #         print(f"The provided input '{item_instance}' is not a valid item.")
    #         itemuseselectionconfirmation = True
    def use_item(self, item_instance):
        if hasattr(item_instance, 'type') and hasattr(item_instance, 'healamount'):
            if item_instance.type == "Food" or item_instance.type == "Potion":
                self.health += item_instance.healamount
                self.inventory.remove(item_instance)
                print(f"Used {item_instance.name}. Your health is now {self.health}.")
            else:
                print(f"{item_instance.name} is not a consumable item.")
        else:
            print(f"The item '{item_instance}' is not valid.")



    # def printinventory(self):
    #     if not self.inventory:
    #         print(self.inventory)
    #         print("Debug")
    #     else:
    #         print("Your inventory is empty")

    def printinventory(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item.name} (Weight: {item.weight})")
        else:
            print("Your inventory is empty.")

    
