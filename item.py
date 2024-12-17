class Item():
    def __init__(self, name):
        self.name = name
        pass

class Weapon(Item):
    def __init__(self, name, rangelb, rangeub, type):
        super().__init__(name)
        self.rangelb = rangelb
        self.rangeub = rangeub
        self.type = type

class Armour(Item):
    def __init__(self, name, resistanceub):
        super().__init__(name)
        self.resistancetub = resistanceub

class Food(Item):
    def __init__(self, name, healamount, attributes):
        super().__init__(name)
        self.type = "Food"
        self.healamount = healamount
        self.attributes = attributes

class Potion(Item):
    def __init__(self, name, healamount, attributes):
        super().__init__(name)
        self.type = "Potion"
        self.healamount = healamount
        self.attributes = attributes

class SpecialItem(Item):
    def __init__(self, name):
        super().__init__(name)
        pass 

