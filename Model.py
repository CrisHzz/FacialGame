class World:
    def __init__(self,size):
        self.size = size
        self.grid = [[None for i in range(size)] for i in range(size)]
        self.Hero = None
        self.devil = None
        #Creacion de el tamaño del mundo y el tablero, hero sera el jugador y devil el enemigo

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
        self.damage = None




    
