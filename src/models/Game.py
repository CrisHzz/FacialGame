import time
from src.models.World import World
from src.models.Entity import Hero, Devil
from src.models.Items import Consumable, Weapon
from src.models.Face import FaceController
from src.models.External import clear_console

class Game:
    
    def __init__(self, map: World, weapons: int = 3, consumables: int = 6):
        self.map = map
        self.hero = Hero()
        self.devil = Devil()
        self.weapons = weapons
        self.consumables = consumables
        
    def _isHeroHere(self, x: int, y: int):
        return isinstance(self.map.grid[x][y], Hero)
    
    def _checkTimes(self, times):
        if times >= ((self.map.size)**2) - 3:
            times -= 1
            return self._checkTimes(times)
        return times    
      
    def _generateConsumable(self, times = 3):
        
        if self._checkTimes(times) >= 0:
            i = 0
            
            while i < times:
                
                position = self.map.generateRandomPosition()
                if self.map.isPositionEmpty(position[0], position[1]):
                    self.map.addConsumable(position[0], position[1])
                    i += 1
      
    def _generateWeapon(self, times = 3):
        
        if self._checkTimes(times) >= 0:
            i = 0
            
            while i < times:
                
                position = self.map.generateRandomPosition()
                if self.map.isPositionEmpty(position[0], position[1]):
                    self.map.addWeapon(position[0], position[1])
                    i += 1
        
    def _canPlayerTakeIt(self, x: int, y: int):
        obj = self.map.getElement(x, y)
        if isinstance(obj, Consumable) or isinstance(obj, Weapon):
            return True
        return False

    def _canHeroAttack(self, x: int, y: int):
        
        if self.map.isValidPosition(x + 1, y):
            obj = self.map.getElement(x + 1, y)
            if isinstance(obj, Devil) and self.hero.getWeaponAmount() > 0:
                return True
        
        if self.map.isValidPosition(x - 1, y):
            obj = self.map.getElement(x - 1, y)
            if isinstance(obj, Devil) and self.hero.getWeaponAmount() > 0:
                return True
        
        if self.map.isValidPosition(x, y + 1):
            obj = self.map.getElement(x, y + 1)
            if isinstance(obj, Devil) and self.hero.getWeaponAmount() > 0:
                return True
        
        if self.map.isValidPosition(x, y - 1):
            obj = self.map.getElement(x, y - 1)
            if isinstance(obj, Devil) and self.hero.getWeaponAmount() > 0:
                return True
        
        return False
        
    def _canHeroEat(self):
        for element in self.hero.inventory:
            if isinstance(element, Consumable):
                return True
        return False
    
    def _spawnEntity(self):
        forHero = False
        forDevil = False
        
        while not forHero:
            position = self.map.generateRandomPosition()
            if self.map.isPositionEmpty(position[0], position[1]):
                self.setHeroPosition(position[0], position[1])
                forHero = True
                
        while not forDevil:
            position = self.map.generateRandomPosition()
            if self.map.isPositionEmpty(position[0], position[1]):
                self.setDevilPosition(position[0], position[1])
                forDevil = True
    
    def getHeroPosition(self):
        size = self.map.size
        for i in range(size):
            for j in range(size):
                if isinstance(self.map.grid[i][j], Hero):
                    return (i, j)
        return None
    
    def getDevilPosition(self):
        size = self.map.size
        for i in range(size):
            for j in range(size):
                if isinstance(self.map.grid[i][j], Devil):
                    return (i, j)
        return None
    
    def setHeroPosition(self, x: int, y: int):
        self.map.addEntity(self.hero, x, y)
    
    def setDevilPosition(self, x: int, y: int):
        self.map.addEntity(self.devil, x, y)
    
    def moveHero(self, direction: int):
        
        heroPosition = self.getHeroPosition()
        
        if heroPosition != None and self.map.isValidPosition(heroPosition[0], heroPosition[1]):
            x_origin = heroPosition[0]
            y_origin = heroPosition[1]
            
            x = heroPosition[0]
            y = heroPosition[1]
            
            spaces = self.map.spaces
                
            if direction == 1:
                x -= 1
                
            elif direction == -1:
                x += 1
                
            elif direction == 2:
                y += 1
                
            elif direction == -2:
                y -= 1
                
            if self.map.isValidPosition(x, y):
                
                if self._canPlayerTakeIt(x, y):
                    object = self.map.getElement(x, y)
                    self.hero.inventory.append(object)
                    
                self.map.addEntity(spaces, x_origin, y_origin)
                self.map.addEntity(self.hero, x, y)
      
    def getDevilRandomMovement(self):
        return self.map.generateRandomPosition()
            
    def moveDevil(self, position: tuple):        
        x_origin = self.getDevilPosition()[0]
        y_origin = self.getDevilPosition()[1]
        
        x = position[0]
        y = position[1]
        
        self.map.addEntity(self.map.spaces, x_origin, y_origin)
        self.map.addEntity(self.devil, x, y)
        
    def isGameOver(self):
        heroHearts = self.hero.hearts
        devilHearts = self.devil.hearts
        return (heroHearts <= 0) or (devilHearts <= 0)
    
    def getWinner(self):
        heroHearts = self.hero.hearts
        devilHearts = self.devil.hearts
        
        if heroHearts > devilHearts:
            return self.hero
        
        elif devilHearts > heroHearts:
            return self.devil
    
    def run(self):
        
        self._spawnEntity()
        self._generateConsumable(self.consumables)
        self._generateWeapon(self.weapons)
        
        cam = FaceController("Fuck the devil", screen_weight=1920, screen_height=1013)
        cam.start()
        cam.mainloop()
        print("Camera started")
        
        current = "hero"
        hero_movenment = None
        hero_action = None
        
        while (not self.isGameOver()):
            
            
            hero_icon = self.hero.icon
            devil_icon = self.devil.icon
            
            hero_hearts = self.hero.hearts
            devil_hearts = self.devil.hearts
            
            self.map.showGrid()
            
            print("")
            
            if current == "hero":
                print(f"Current turn: {hero_icon}")
            else:
                print(f"Current turn: {devil_icon}")
            
            print(f" -> Hero ({hero_icon}) (x{hero_hearts} ❤)")
            print(f" -> Hero (Inventory 🎒) {self.hero.inventory}")
            
            
            print(f"-> Devil ({devil_icon}) (x{devil_hearts} ❤)")
            
            if current == "hero":
                
                while True:
                    
                    hero_movenment = cam.get_movement()
                    hero_action = cam.get_action()
                                        
                    if (hero_movenment != 0 and hero_movenment is not None) or (hero_action == True):
                        break
                
                if hero_action:
                    
                    if self._canHeroAttack(self.getHeroPosition()[0], self.getHeroPosition()[1]):
                        self.devil.getDamage(Weapon().damage)
                        
                    elif self._canHeroEat():
                        self.hero.getHealth(10)
                        self.hero.removeConsumable()
                    
                else:
                    self.moveHero(hero_movenment)
                
                current = "devil"
                
                
            elif current == "devil":
                
                position = self.getDevilRandomMovement()
                
                if self._isHeroHere(position[0], position[1]):
                    self.hero.getDamage(10)
                    
                else:
                    self.moveDevil(position)
                
                current = "hero"
                
            
            
            time.sleep(1.8)
            hero_movenment = None
            hero_action = None
            clear_console()
        print(f"Game Over, {self.getWinner()} has won!")
        
                    
            
