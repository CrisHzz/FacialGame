class Entity:
    def __init__(self, hearts: int = 0):
        self.hearts = hearts

class Hero(Entity):
    
    def __init__(self):
        super().__init__(hearts=10)
        self.inventory = []
        
    # If there's any enemy in front of the hero, attack it (Action) [Stand By]
    # If there's no enemy, eat (Action) [Stand By]
    # If there's any item below the hero, pick it up (Action) [Stand By]


class Devil(Entity):
    
    def __init__(self):
        super().__init__(hearts=100)