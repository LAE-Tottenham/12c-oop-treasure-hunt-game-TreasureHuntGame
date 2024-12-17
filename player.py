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
        if item_instance.type == "food":
            self.health += item_instance.healamount
        elif item_instance.type == "potion":
            self.health += item_instance.healamount
        # add more code here

    # add more methods as needed
