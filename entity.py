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

class Wolf(enemy):  # Inherit from the Enemy class
    def __init__(self):
        # Call the superclass (Enemy) constructor with the proper values
        super().__init__(name="Wild Wolf", health=50, damagelb=5, damageub=15)
        self.type = "melee"


#Positive NPCs
class Shop:
    def __init__(self, items=None, prices=None):
        self.items = items if items is not None else []  # List of items for sale
        self.prices = prices if prices is not None else {}  # Dictionary of item prices

    def display_items(self):
        print("Items for sale:")
        for idx, item in enumerate(self.items, start=1):
            price = self.prices.get(item.name, "Price unavailable")
            print(f"{idx}. {item.name} - Price: {price} gold")
    
    def buy_item(self, player, item_name):
        for item in self.items:
            if item.name == item_name:
                price = self.prices.get(item_name)
                if price is None:
                    print("Price unavailable. You cannot buy this item.")
                    return
                if player.currency >= price:
                    player.currency -= price
                    player.inventory.append(item)
                    print(f"You bought {item_name} for {price} gold!")
                else:
                    print("You don't have enough gold.")
                return
        print(f"{item_name} is not available in the shop.")




class NPC:
    def __init__(self, name, shop):
        self.name = name
        self.shop = shop

    def interact(self, player):
        print(f"{self.name} says: 'Welcome to my shop!'")
        self.shop.display_items()
        choice = input("Which item would you like to buy? (Enter item name or 'exit' to leave): ").strip()
        if choice.lower() != 'exit':
            self.shop.buy_item(player, choice)
        else:
            print("Thanks for visiting!")
