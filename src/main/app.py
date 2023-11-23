import sys

# Replace the path below with the path of the project in your computer
sys.path.append('C:\\Users\\David\\Desktop\\Dev (Local)\\Dev-Github\\Python\\Estructura de Datos\\FacialGame')

from src.models.World import World
from src.models.Game import Game

def main():
    
    gameMap = World(4)
    gameMap.generateGrid()
    game = Game(gameMap)
    game.run()
    
    
if __name__ == '__main__':
    main()