from math import pi, cos, sin, degrees, radians

from circular_buffer import CircularBuffer

class WindowType(Enum):
    HANN = 1
    HAMM = 2
    RECTANGULAR = 3
    TRAPEZOID = 4

class Window: # Should this inherit from CircularBuffer instead of containing an instance?

    def __init__(self, window_type: str, buffer: list[float]) -> None:

        self.window_type = window_type
        self.window_index = 0
        computed_window_samples = self._calculate_window(self.window_type)
        self.window_buffer = CircularBuffer(computed_window_samples)


    def _calculate_window(self, window_type: WindowType):
        N = len(window)
        match window_type:
            case 1:
                computed_window_samples = [0.5 * (1 - cos((2 * pi * n)/N)) for n in range(N)]
            case 2:
                computed_window_samples = [0.54 * 0.46 * cos((2 * pi * n)/(N-1)) for n in range(N)]
            case 3:
                computed_window_samples = [1 for x in range(N)]
            case 4:
                computed_window_samples = [1 for x in range(N)]

        return computed_window_samples


class Granulator:

    def __init__(self, window: Window, window_size: int, window_type="hann": WindowType):
        self.sample_buffer = CircularBuffer(buffer)
        self.buffer_index = 0
        self.window = window(window_type)

    def return_sample(self):
        
        sample = self.sample_buffer.read_index() * self.window.window_buffer.read_index()
        
        return sample

