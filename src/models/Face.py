import cv2
from dataclasses import dataclass, field
import threading
import time
import queue


@dataclass
class FaceController:
    title: str = field(default_factory=str, init=True)
    screen_width: int = field(default_factory=int, init=True)  # 1920
    screen_height: int = field(default_factory=int, init=True)  # 1013

    # Variables para hacer el frame cuadrado
    _width: int = field(init=False)
    _height: int = field(init=False)

    # Variables para crear rectángulos alrededor de la cara y la pantalla
    _left_top: tuple = field(default=(50, 30))  # Coordenadas predeterminadas
    _right_bottom: tuple = field(init=False)
    _top_face: tuple = field(default=(0, 0))  # Coordenadas predeterminadas
    _bottom_face: tuple = field(default=(0, 0))  # Coordenadas predeterminadas

    # Variables para usar el detector de caras
    _face_cascade: cv2.CascadeClassifier = field(default_factory=cv2.CascadeClassifier)
    _cap: cv2.VideoCapture = field(default_factory=cv2.VideoCapture)
    _faces: list = field(default_factory=list)

    # Cola para las imágenes procesadas
    image_queue = queue.Queue()

    def __post_init__(self) -> None:
        self._width = int(0.2 * self.screen_width)
        self._height = int(0.2 * self.screen_height)
        self._right_bottom = (self.screen_width - self._width - 120, self.screen_height - self._height - 10)

    def start(self) -> None:
        self._face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self._cap = cv2.VideoCapture(0)
        self._cap.set(3, self._width)
        self._cap.set(4, self._height)

    def stop(self) -> None:
        self._cap.release()
        cv2.destroyAllWindows()

    def get_frame(self) -> tuple:
        return self._cap.read()[1]

    def check_exit(self) -> bool:
        return cv2.waitKey(1) in [27, 113]

    def get_action(self) -> bool:
        if len(self._faces) > 0:
            return False
        return True

    def get_movement(self) -> int:
        # Calcula el centro del rectángulo alrededor del rostro
        face_center_x = (self._top_face[0] + self._bottom_face[0]) // 2
        face_center_y = (self._top_face[1] + self._bottom_face[1]) // 2

        # Calcula el centro del rectángulo de la pantalla
        screen_center_x = (self._left_top[0] + self._right_bottom[0]) // 2
        screen_center_y = (self._left_top[1] + self._right_bottom[1]) // 2

        # Calcula la diferencia entre los centros
        dx = face_center_x - screen_center_x
        dy = face_center_y - screen_center_y

        # Define un umbral de movimiento para determinar si el jugador se ha movido
        threshold = 10

        # Detecta el movimiento en la dirección horizontal
        if abs(dx) > threshold:
            if dx > 0:
                return 2  # Movimiento hacia la derecha
            else:
                return -2  # Movimiento hacia la izquierda

        # Detecta el movimiento en la dirección vertical
        if abs(dy) > threshold:
            if dy > 0:
                return 1  # Movimiento hacia arriba
            else:
                return -1  # Movimiento hacia abajo

        return 0  # No hay movimiento

    def auxiliar_loop(self):
        prev_face_position = None  # Almacena la posición anterior del rectángulo alrededor del rostro
        while True:
            frame = self.get_frame()
            if frame is not None:
                frame = cv2.flip(frame, 1)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                self._faces = self._face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                for (x, y, w, h) in self._faces:
                    # Calcular las coordenadas para el rectángulo alrededor del rostro centrado
                    center_x = x + w // 2
                    center_y = y + h // 2
                    rect_width = int(0.6 * w)
                    rect_height = int(1.2 * h)
                    rect_x = center_x - rect_width // 2
                    rect_y = center_y - rect_height // 2

                    self._top_face = (rect_x, rect_y)
                    self._bottom_face = (rect_x + rect_width, rect_y + rect_height)

                    # Si hay una posición anterior, compara con la posición actual para detectar movimiento
                    if prev_face_position is not None:
                        dx = center_x - prev_face_position[0]
                        dy = center_y - prev_face_position[1]

                        # Define un umbral de movimiento para determinar si el jugador se ha movido
                        threshold = 10

                        # Detecta el movimiento en la dirección horizontal
                        if abs(dx) > threshold:
                            if dx > 0:
                                print('Movimiento hacia la derecha')
                            else:
                                print('Movimiento hacia la izquierda')

                        # Detecta el movimiento en la dirección vertical
                        if abs(dy) > threshold:
                            if dy > 0:
                                print('Movimiento hacia abajo')
                            else:
                                print('Movimiento hacia arriba')

                    # Actualiza la posición anterior
                    prev_face_position = (center_x, center_y)

                    # Calcular las coordenadas para el rectángulo alrededor de la pantalla centrada
                    self._right_bottom = ((self._width - 120), (self._height - 10))
                    screen_width = self._right_bottom[0] - self._left_top[0]
                    screen_height = self._right_bottom[1] - self._left_top[1]
                    screen_x = center_x - screen_width // 2
                    screen_y = center_y - screen_height // 2
                    self._left_top = (screen_x, screen_y)

                # Dibujar los rectángulos en el frame
                cv2.rectangle(frame, self._top_face, self._bottom_face, (255, 0, 0), 2)
                cv2.rectangle(frame, self._left_top, self._right_bottom, (0, 255, 0), 2)

                # Enviar frame a la cola
                self.image_queue.put(frame)

    def display_images(self):
        while True:
            if not self.image_queue.empty():
                frame = self.image_queue.get()
                cv2.imshow(self.title, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    def mainloop(self):
        self.start()  # Iniciar la cámara y la detección de rostros

        # Crear e iniciar un hilo para el procesamiento auxiliar (detección de rostros)
        threading.Thread(target=self.auxiliar_loop).start()

        # Ejecutar el ciclo principal para mostrar imágenes
        self.display_images()

        self.stop()  # Cerrar la cámara y destruir todas las ventanas al final


"""
if __name__ == '__main__':
    cam = FaceController(title='Spy cam', screen_width=1440, screen_height=900)
    cam.start()
    threading.Thread(target=cam.auxiliar_loop).start()
    cam.display_images()
"""