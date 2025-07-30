

class Window:

    def __init__(self, window_type: str, buffer: list[float]) -> None:
        self.window_type = window_type
        self.window_index = 0

    def _advance_window_index(self):
        pass


class Granulator:

    def __init__(self, window: Window):
        self.buffer = buffer
        self.buffer_index = 0
        self.window = window

    def return_sample(self):
        sample = self.buffer[self.buffer_index] * self.window.samples[self.window.window_index]
        
        return (sample)

    def _advance_buffer_index(self):
        pass
