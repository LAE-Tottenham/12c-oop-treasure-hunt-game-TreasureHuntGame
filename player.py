class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.inventory_max_weight = 50
        self.inventory = []
        # add more atributes as needed

    def calculate_inventory_size(self):
        total = 0
        for i in self.inventory:
            total = total + i.weight
        self.weight = i.weight
        
        pass

    def add_item(self, item_instance):
        if self.calculate_inventory_size() > self.inventory_max_weight:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full...")

    def use_item(self, item_instance):
        itemuseselectionconfirmation = False
        while itemuseselectionconfirmation == False:
            if item_instance.type == "food":
                self.health += item_instance.healamount
                self.inventory.remove(item_instance)
                itemuseselectionconfirmation = True
            elif item_instance.type == "potion":
                self.health += item_instance.healamount
                self.inventory.remove(item_instance)
                itemuseselectionconfirmation = True
            else:
                print("The item you have entered does not exist. Please choose again")

    def printinventory(self):
        print(self.inventory)
