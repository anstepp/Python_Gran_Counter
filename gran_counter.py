#set up a circular buffer object

class CircularBuffer:
    
    def __init__(self, samples: list[float]) -> None:
        self.samples = samples
        self.input_counter = 0
        self.output_counter = 0


    def _advance_input_counter(self) -> None:
        if self.input_counter < len(self.samples):
            self.input_counter += 1
        else:
            self.input_counter = 0

    def _advance_output_counter(self) -> None:
        if self.output_counter < len(self.samples):
            self.output_counter += 1
        else:
            self.output_counter = 0

    def read_output(self) -> float:
        self._advance_output_counter()
        return samples[output_counter]

    def _read_input(self, read_sample) -> None:
        samples[input_counter] = read_sample
        self._advance_input_counter()