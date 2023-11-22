class Entity:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hearts = None

class Hero(Entity):
    def __init__(self,x,y):
        Entity.__init__(self,x,y)
        self.hearts = 10
        self.inventory = []


class Devil(Entity):
    def __init__(self,x,y):
        Entity.__init__(self,x,y)
        self.hearts = 100