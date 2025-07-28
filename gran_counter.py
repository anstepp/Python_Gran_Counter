#set up a circular buffer object

class CircularBuffer:
    
    def __init__(self, samples: list[float]) -> None:
        self.samples = samples
        self.input_counter = 0
        self.output_counter = 0


    def _advance_input_counter(self) -> None:
        if input_counter < len(samples):
            input_counter += 1
        else:
            input_counter = 0

    def _advance_output_counter(self) -> None:
        if output_counter < len(samples):
            output_counter += 1
        else:
            output_counter = 0

    def read_output(self) -> float:
        self._advance_output_counter()
        return samples[output_counter]

    def _read_input(self, read_sample) -> None:
        samples[input_counter] = read_sample
        self._advance_input_counter()