class World:
    def __init__(self,size):
        self.size = size
        self.grid = [[None for i in range(size)] for i in range(size)]
        self.Hero = None
        self.devil = None