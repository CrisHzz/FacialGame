from src.models.World import World
from src.models.Entity import Hero, Devil
from src.models.Face import FaceController

class Game:
    
    def __init__(self, map: World):
        self.map = map
        self.hero = Hero()
        self.devil = Devil()
        
    def getHeroPosition(self):
        size = self.map.size
        for i in range(size):
            for j in range(size):
                if isinstance(self.map.map[i][j], Hero):
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
            
            self.map.addEntity(x, y, None)
            
            if direction == 1:
                x -= 1
            elif direction == -1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == -2:
                y += 1
                
            self.map.addEntity(x, y, self.hero)
      
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
                
            self.map.addEntity(x, y, self.hero)
    
    def isGameOver(self):
        heroHearts = self.hero.hearts
        devilHearts = self.devil.hearts
        return (heroHearts <= 0) or (devilHearts <= 0)
    
    
    
    def run(self):
        
        cam = FaceController("Fuck the devil", screen_weight=1920, screen_height=1013)
        cam.start()
        cam.mainloop()
                
        self.setHeroPosition(0,0)
        self.setDevilPosition(3,3)
        
        current = "hero"
        action = None
        movement = None
                
        while not self.isGameOver():

            
            if current == "hero":
                while (action != None or movement != None):
                    action = cam.get_action()
                    movement = cam.get_movement()
            else:
                pass
