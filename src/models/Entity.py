from src.models.Items import Consumable, Weapon


class Entity:
    def __init__(self, hearts: int = 0, icon: str = None):
        self.hearts = hearts
        self.icon = icon
    def __repr__(self) -> str:
        return str(self.icon)
    
    def getDamage(self, damage: int):
        self.hearts -= damage
        if self.hearts < 0:
            self.hearts = 0
            
    def getHealth(self, health: int):
        self.hearts += health

class Hero(Entity):
    
    def __init__(self, icon: str = "👺"):
        super().__init__(hearts=10, icon=icon)
        self.inventory = []
        
    def getWeaponAmount(self) -> int:
        count = 0
        for item in self.inventory:
            if isinstance(item, Weapon):
                count += 1
        return count
                
    def getConsumableAmount(self) -> int:
        count = 0
        for item in self.inventory:
            if isinstance(item, Consumable):
                count += 1
        return count
        
    def removeWeapon(self):
        for item in self.inventory:
            if isinstance(item, Weapon):
                self.inventory.remove(item)
                break
    
    def removeConsumable(self):
        for item in self.inventory:
            if isinstance(item, Consumable):
                self.inventory.remove(item)
                break    
    
    # If there's any enemy in front of the hero, attack it (Action) [Stand By]
    # If there's no enemy, eat (Action) [Stand By]


class Devil(Entity):
    
    def __init__(self, icon: str = "🐔"):
        super().__init__(hearts=100, icon=icon)
        
    def __repr__(self) -> str:
        return super().__repr__()