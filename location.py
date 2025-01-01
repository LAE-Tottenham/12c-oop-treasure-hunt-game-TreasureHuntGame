from random import shuffle, choice, randint
from entities import *
from getch import getch
from time import sleep

class MazeDimensionError(Exception):
    pass

class Location():
    def __init__(self, type:str, size:int):
        self.type = type
        self.size = size
        self.room = []

    def generate_maze(self):
        if self.size % 2 == 0:
            raise MazeDimensionError("Dimensions must be odd")

        maze = [["x" for i in range(self.size)] for i in range(self.size)]

        x, y = (-1, 1)
        stack = [(y, x)]
        directions = [(0,2), (0,-2), (2,0), (-2,0)]
        
        while len(stack) > 0:
            y, x = stack[-1]

            shuffle(directions)

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if nx > 0 and ny > 0 and nx < self.size-1 and ny < self.size-1 and maze[ny][nx] == "x":
                    maze[ny][nx] = " "
                    maze[ny-dy//2][nx-dx//2] = " "
                    stack.append((ny, nx))
                    break
            else:
                stack.pop()

        maze[-2][-1] = " "

        self.room = maze
        #for row in maze:
        #    print(str(row).replace("[", "").replace("]", "").replace(",", "").replace("'", ""))

    def load_enemies(self, enemies):
        pass

    def load_items(self, items):
        pass

    def load_npcs(self, npcs):
        pass

class Minigame(Location):
    def __init__(self, room):
        super().__init__("Minigame", len(room))
        self.room = room
        self.won = False

class Combat():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turnOrder = sorted(player.summons.extend([player, enemy]), key=lambda x: x.speed)
        self.exp = enemy.exp[0]

    def start(self):
        while self.player.health[1] > 0 and self.enemy.health[1] > 0:
            current = self.turnOrder[0].pop()

            if type(current) is Player:
                for number, ability in enumerate(current.abilities):
                    print(number+1, ability.name)
                print("What move do you want to use?")
                num = int(getch())
                while num not in range(1,6):
                    print("Invalid input", end="\r")
                    sleep(1)
                    print("\033[K")
                    num = int(getch())
                current.attack(self.enemy, ability[num])
            else:
                moves = shuffle(current.abilities)
                for move in moves:
                    if move.cost <= current.sp[1]:
                        if current.isSummon:
                            current.attack(self.enemy, move)
                        else:
                            current.attack(choice(self.turnOrder), move)
                        break
                else:
                    if current.sp[1] < 0.1 * current.sp[0]:
                        current.rest()
                    else:
                        current.wait()

            self.turnOrder.append(current)

        if self.enemy.health[1] <= 0:
            for summon in self.player.summons:
                summon.exp[1] += self.exp
                while summon.exp[1] > summon.exp[0]:
                    summon.levelUp()