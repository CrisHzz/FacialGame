import sys

# Replace the path below with the path of the project in your computer
sys.path.append('/Users/andresdavidcardenasramirez/Documents/Universidad/semestre2023-2/codigo/proyecto-final/FacialGame')

from src.models.World import World
from src.models.Game import Game

def main():
    
    gameMap = World(4)
    gameMap.generateGrid()
    game = Game(gameMap)
    game.run()
    
    
if __name__ == '__main__':
    main()