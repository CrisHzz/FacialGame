import sys

# Replace the path below with the path of the project in your computer
sys.path.append('C:\\Users\\David\\Desktop\\Dev (Local)\\Dev-Github\\Python\\Estructura de Datos\\FacialGame')
from src.models.Face import FaceController

def main():
    spy = FaceController("I'm a Spyware ;)", 1920, 1013)
    spy.start()
    spy.mainloop()

if __name__ == '__main__':
    main()