import random
from typing import Union
from src.models.Entity import Entity, Consumable, Weapon


class World:
    
    def __init__(self, size: int = None) -> None:
        self.size: int = size
        self.grid: list[list] = None

    def _isValidPosition(self, x: int, y: int) -> bool:
        return (x >= 0 and x < self.size) and (y >= 0 and y < self.size) and (self.grid[x][y] == None)

    def generateGrid(self) -> None:
        if self.size == None:
            self.size = 5
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def generateRandomPosition(self) -> tuple:
        
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self._isValidPosition(x, y):
                return (x, y)
        
    def addEntity(self, entity: Entity, x: int = None, y: int = None) -> None:
        if x == None or y == None:
            x, y = self.generateRandomPosition()
        entity.x = x
        entity.y = y
        self.grid[x][y] = entity
        
    def addConsumable(self, consumable: Consumable, x: int = None, y: int = None) -> None:
        if x == None or y == None:
            x, y = self.generateRandomPosition()
        consumable.x = x
        consumable.y = y
        self.grid[x][y] = consumable
        
    def addWeapon(self, weapon: Weapon, x: int = None, y: int = None) -> None:
        if x == None or y == None:
            x, y = self.generateRandomPosition()
        weapon.x = x
        weapon.y = y
        self.grid[x][y] = weapon
        
    def getElement(self, x: int, y: int) -> Union[Entity, Consumable, Weapon, None]:
        if self._isValidPosition(x, y):
            return self.grid[x][y]
        return None