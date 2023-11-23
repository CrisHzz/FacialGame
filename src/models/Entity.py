class Entity:
    def __init__(self, hearts: int = 0, icon: str = None):
        self.hearts = hearts
        self.icon = icon
    def __repr__(self) -> str:
        return str(self.icon)

class Hero(Entity):
    
    def __init__(self, icon: str = "👺"):
        super().__init__(hearts=10, icon=icon)
        self.inventory = []
        
    # If there's any enemy in front of the hero, attack it (Action) [Stand By]
    # If there's no enemy, eat (Action) [Stand By]
    # If there's any item below the hero, pick it up (Action) [Stand By]


class Devil(Entity):
    
    def __init__(self, icon: str = "🐔"):
        super().__init__(hearts=100, icon=icon)
        
    def __repr__(self) -> str:
        return super().__repr__()