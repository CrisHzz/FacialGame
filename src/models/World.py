import random
from src.models.Entity import Entity, Hero, Devil, Consumable, Weapon


class World:
    def __init__(self,size: int) -> None:
        self.size: int = size
        self.grid: list[list] = [[None for i in range(size)] for j in range(size)]
        self.hero: Hero = None
        self.devil: Devil = None

    def RandomPlaceEntity(self, entity: Entity) -> None:
        
        while True:
            
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            
            if self.grid[x][y] == None:
                entity.x = x
                entity.y = y
                self.grid[x][y] = entity
                break

    def createHero(self) -> None:
        self.Hero = Hero(0, 0)
        self.placeEntityRandomly(self.Hero)

    def createDevil(self) -> None:
        self.devil = Devil(0, 0)  
        self.placeEntityRandomly(self.devil)

    def createConsumable(self) -> None:
        self.consumable: Consumable = Consumable(0, 0)
        self.placeEntityRandomly(self.consumable)

    def createWeapon(self) -> None:
        self.weapon: Weapon = Weapon(0, 0)
        self.placeEntityRandomly(self.weapon)
        
    def getHeroPosition(self) -> tuple:
        return (self.hero.x, self.hero.y)
    
    def getDevilPosition(self) -> tuple:
        return (self.devil.x, self.devil.y)