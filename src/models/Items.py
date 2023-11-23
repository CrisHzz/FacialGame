class Item:
    
    def __init__(self, icon = None):
        self.icon = icon

class Consumable(Item):
    
    def __init__(self,  icon = "🍕"):
        super().__init__(icon)
        
class Weapon(Item):
    
    def __init__(self, icon = "🔪"):
        super().__init__(icon)
        self.damage = 25
