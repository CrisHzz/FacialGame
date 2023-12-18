import cv2
from dataclasses import dataclass, field
import threading
@dataclass
class FaceController:
    
    title: str = field(default_factory=str, init=True)
    
    screen_weight: int = field(default_factory=int, init=True) # 1920
    screen_height: int = field(default_factory=int, init=True) # 1013
    
    # Variables to make frame as a square
    _weight: int = field(init=False)
    _height: int = field(init=False)
    
    # Variables to create rectangles around the face and the screen
    _left_top: tuple = field(default=(50, 30)) # Default coords
    _right_bottom: tuple = field(init=False)
    
    _top_face: tuple = field(default=(0, 0)) # Default coords
    _bottom_face: tuple = field(default=(0, 0)) # Default coords
    
    # Variables to use the face detector
    _face_cascade: cv2.CascadeClassifier = field(default_factory=cv2.CascadeClassifier)
    _cap: cv2.VideoCapture = field(default_factory=cv2.VideoCapture)
    _faces: list = field(default_factory=list)
    
    def __post_init__(self) -> None:
        self._weight = int(0.2 * self.screen_weight)
        self._height = int(0.2 * self.screen_height)
        self._right_bottom = (self.screen_weight - self._weight - 120, self.screen_height - self._height - 10)
    
    def start(self) -> None:
        self._face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self._cap = cv2.VideoCapture(0)
        self._cap.set(3, self._weight)
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
                
        # Up
        if self._top_face[1] < self._left_top[1]:
            return 1
        
        # Down
        elif self._bottom_face[1] > self._right_bottom[1]:
            return -1
        
        # Left
        elif self._top_face[0] < self._left_top[0]:
            return -2
        
        # Right
        elif self._bottom_face[0] > self._right_bottom[0]:
            return 2
        
        # Center
        return 0

    def mainloop(self) -> None:
        
        def auxiliar_loop():
            
            while True:
                
                frame = self.get_frame()
                frame = cv2.flip(frame, 1)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                self._faces = self._face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                for (x, y, w, h) in self._faces:
                    
                    
                    
                    self._top_face = (x, y)
                    self._bottom_face = (x + w, y + h)
                    
                    self._right_bottom = ((self._weight - 120), (self._height - 10))
                    self._left_top = (50, 30)
                    
                    cv2.rectangle(frame, self._top_face, self._bottom_face, (255, 0, 0), 2) # -> CV2
                    
                    cv2.rectangle(frame, self._left_top, self._right_bottom, (0, 255, 0), 2) # -> Manuales
                      
                cv2.imshow(self.title, frame)
                
                if self.check_exit():
                    break

        threading.Thread(target=auxiliar_loop).start()

        
    