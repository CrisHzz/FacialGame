import time
from src.models.World import World
from src.models.Entity import Hero, Devil
from src.models.Face import FaceController
from src.models.External import clear_console

class Game:
    
    def __init__(self, map: World):
        self.map = map
        self.hero = Hero()
        self.devil = Devil()
        
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
                if isinstance(self.map.map[i][j], Devil):
                    return (i, j)
        return None
    
    def setHeroPosition(self, x: int, y: int):
        self.map.addEntity(self.hero, x, y)
    
    def setDevilPosition(self, x: int, y: int):
        self.map.addEntity(self.devil, x, y)
    
    def moveHero(self, direction: int):
        
        heroPosition = self.getHeroPosition()
        
        if heroPosition != None:
            
            x = heroPosition[0]
            y = heroPosition[1]
            
            spaces = self.map.spaces
            
            self.map.addEntity(spaces, x, y)
            
            if direction == 1:
                x -= 1
            elif direction == -1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == -2:
                y += 1
                
            self.map.addEntity(self.hero, x, y)
      
    def getDevilRandomMovement(self):
        
        x = self.getDevilPosition()[0]
        y = self.getDevilPosition()[1]
        
        if self.map.isValidPosition(x + 1, y):
            return(x + 1, y)
        
        elif self.map.isValidPosition(x - 1, y):
            return(x - 1, y)
        
        elif self.map.isValidPosition(x, y + 1):
            return(x, y + 1)
        
        elif self.map.isValidPosition(x, y - 1):
            return(x, y - 1)
            
    def moveDevil(self, direction: int):
        
        devilPosition = self.getDevilPosition()
        
        if devilPosition != None:
            
            x = devilPosition[0]
            y = devilPosition[1]
            
            self.map.addEntity(x, y, None)
            
            if direction == 1:
                x -= 1
            elif direction == -1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == -2:
                y += 1
                
            self.map.addEntity(self.hero, x, y)
    
    def isGameOver(self):
        heroHearts = self.hero.hearts
        devilHearts = self.devil.hearts
        return (heroHearts <= 0) or (devilHearts <= 0)
    
    
    
    def run(self):
        
        self.setHeroPosition(0,0)
        self.setDevilPosition(9,9)
        
        cam = FaceController("Fuck the devil", screen_weight=1920, screen_height=1013)
        cam.start()
        cam.mainloop()
        
        current = "hero"
        hero_movenment = None
        hero_action = None
        
        hero_icon = self.hero.icon
        devil_icon = self.devil.icon
        
        hero_hearts = self.hero.hearts
        devil_hearts = self.devil.hearts
        
        while (not self.isGameOver()):
            
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
                    print("El jugador hizo algo, no sé")
                else:
                    self.moveHero(hero_movenment)
                
                current = "devil"
                
                
            elif current == "devil":
                
                print("El demonio ya hizo lo suyo equis deeeeee")
                
                current = "hero"
            
            
            time.sleep(5)
            hero_movenment = None
            hero_action = None
            clear_console()
        
                    
            
