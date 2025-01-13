class Item():
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight  # Add weight attribute here
    
    def __str__(self):
        return self.name

class Weapon(Item):
    def __init__(self, name, rangelb, rangeub, type, weight):
        super().__init__(name, weight)  # Pass weight to the parent class
        self.rangelb = rangelb
        self.rangeub = rangeub
        self.type = type

class Armour(Item):
    def __init__(self, name, resistanceub, weight):
        super().__init__(name, weight)  # Pass weight to the parent class
        self.resistancetub = resistanceub

class Food(Item):
    def __init__(self, name, healamount, attributes, weight):
        super().__init__(name, weight)  # Pass weight to the parent class
        self.type = "Food"
        self.healamount = healamount
        self.attributes = attributes

class Potion(Item):
    def __init__(self, name, healamount, attributes, weight):
        super().__init__(name, weight)  # Pass weight to the parent class
        self.type = "Potion"
        self.healamount = healamount
        self.attributes = attributes

class SpecialItem(Item):
    def __init__(self, name, weight):
        super().__init__(name, weight)  # Pass weight to the parent class
        pass


