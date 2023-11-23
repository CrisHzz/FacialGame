class Entity:
    def __init__(self):
        self.hearts = 0

class Hero(Entity):
    
    def __init__(self):
        super().__init__()
        self.hearts = 10
        self.inventory = []


class Devil(Entity):
    
    def __init__(self):
        super().__init__()
        self.hearts = 100