class Place:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.people = []
        self.enemies = []
        self.connected_places = {}

    def add_item(self, item):
        self.items.append(item)

    def add_person(self, person):
        self.people.append(person)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def connect(self, direction, place):
        self.connected_places[direction] = place

    def display(self):
        print(f"{self.name}: {self.description}")
        print("Items: ", ", ".join([item.name for item in self.items]))
        print("People: ", ", ".join([person.name for person in self.people]))
        print("Enemies: ", ", ".join([enemy.name for enemy in self.enemies]))

