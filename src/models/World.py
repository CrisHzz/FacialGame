import sys

sys.path.append('C:\\Users\\David\\Desktop\\Dev (Local)\\Dev-Github\\Python\\Estructura de Datos\\FacialGame')

import random
from typing import Union
from src.models.Entity import Entity
from src.models.Items import Consumable, Weapon


class World:
    
    def __init__(self, size: int = None) -> None:
        self.size: int = size
        self.grid: list[list] = None
        self.spaces: str = "  "

    def isValidPosition(self, x: int, y: int) -> bool:
        
        check1 = (x != None and y != None)
        check2 = (x >= 0 and x < self.size)
        check3 = (y >= 0 and y < self.size)
            
        return check1 and check2 and check3
    
    def isPositionEmpty(self, x: int, y: int) -> bool:
        return self.grid[x][y] == self.spaces

    def generateGrid(self) -> None:
        if self.size is None:
            self.size = 5
        self.grid = [[self.spaces for _ in range(self.size)] for _ in range(self.size)]

    def generateRandomPosition(self) -> tuple:
        
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.isValidPosition(x, y):
                return (x, y)
        
    def showGrid(self) -> None:
        for i in range(self.size):
            print(self.grid[i])
        
    def addEntity(self, entity: Entity, x: int = None, y: int = None) -> None:
        if (self.isValidPosition(x, y)):
            self.grid[x][y] = entity
        
    def addConsumable(self, x: int = None, y: int = None) -> None:
        if (self.isValidPosition(x, y)):
            self.grid[x][y] = Consumable()
        
    def addWeapon(self, x: int = None, y: int = None) -> None:
        if (self.isValidPosition(x, y)):
            self.grid[x][y] = Weapon()
        
    def getElement(self, x: int, y: int) -> Union[Entity, Consumable, Weapon, None]:
        if self.isValidPosition(x, y):
            return self.grid[x][y]
        return None