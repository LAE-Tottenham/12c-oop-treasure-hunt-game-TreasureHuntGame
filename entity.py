class enemy():
    def __init__(self, name, health, damagelb, damageub):
        self.name = name
        self.health = health
        self.damagelb = damagelb
        self.damageub = damageub

class skeleton(enemy):
    def __init__(self, name, health, damagelb, damageub, arrow_count):
        super().__init__(name, health, damagelb, damageub)
        self.arrow_count = arrow_count
        self.type = "ranged"

class zombie(enemy):
    def __init__(self, name, health, damagelb, damageub):
        super().__init__(name, health, damagelb, damageub)
        self.type = "melee"


#Positive NPCs

class NPC():
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)