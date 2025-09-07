from math import pi, cos, sin, degrees, radians

from circular_buffer import CircularBuffer

class WindowType(Enum):
    HANN = 1
    HAMM = 2
    RECTANGULAR = 3
    TRAPEZOID = 4

class Window:

    def __init__(self, window_type: str, buffer: list[float]) -> None:

        self.window_type = window_type
        self.window_index = 0
        self.window_buffer = CircularBuffer(buffer)

    def _calculate_window(self, window_type: WindowType):
        match window_type:
            case 1:
                return 0.5 * (1 - cos((2 * pi * n)/N))
            case 2:
                return 0.54 * 0.46 * cos((2 * pi * n)/(N-1))
            case 3:
                return x
            case 4:
                pass


class Granulator:

    def __init__(self, window: Window, window_size: int, window_type="hann": WindowType):
        self.buffer = CircularBuffer(buffer)
        self.buffer_index = 0
        self.window = window("hann")

    def return_sample(self):
        
        sample = self.buffer.read_index() * self.window.window_buffer.read_index()
        
        return (sample)

