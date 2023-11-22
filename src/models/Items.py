class Item:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Consumable(Item):
    def __init__(self, x, y, icon):
        Item.__init__(self, x, y)
        self.icon = "🍕"
        
class Weapon(Item):
    def __init__(self, x, y, icon):
        Item.__init__(self, x, y)
        self.icon = "🔪"
        self.damage = 0
