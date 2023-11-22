import random
class World:
    def __init__(self,size):
        self.size = size
        self.grid = [[None for i in range(size)] for j in range(size)]
        self.Hero = None
        self.devil = None
        #Creacion de el tamaño del mundo y el tablero, hero sera el jugador y devil el enemigo

    def RandomPlaceEntity(self, entity):
        while True:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            if self.grid[x][y] == None:
                entity.x = x
                entity.y = y
                self.grid[x][y] = entity
                break
        #Funcion para colocar entidades en el tablero de forma aleatoria

    def createHero(self):
        self.Hero = Hero(0, 0)
        self.placeEntityRandomly(self.Hero)

    def createDevil(self):
        self.devil = Devil(0, 0)  
        self.placeEntityRandomly(self.devil)

    def createConsumable(self):
        self.consumable = Consumable(0, 0)
        self.placeEntityRandomly(self.consumable)

    def createWeapon(self):
        self.weapon = Weapon(0, 0)
        self.placeEntityRandomly(self.weapon)
    

class Entity:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hearts = None
        #Creacion de la entidad, x y y son las coordenadas de la entidad, hearts son los corazones de la entidad

class Hero(Entity):
    def __init__(self,x,y):
        Entity.__init__(self,x,y)
        self.hearts = 10
        self.inventory = []
        #Creacion del heroe, Este hereda de la Entity


class Devil(Entity):
    def __init__(self,x,y):
        Entity.__init__(self,x,y)
        self.hearts = 100
        #Creacion del enemigo, Este hereda de la Entity

class item:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #Creacion de los items, seran estaticos

class Consumable(item):
    def __init__(self, x, y, icon):
        item.__init__(self, x, y)
        self.icon = "🍕"
        
class Weapon(item):
    def __init__(self, x, y, icon):
        item.__init__(self, x, y)
        self.icon = "🔪"
        self.damage = 25




    
