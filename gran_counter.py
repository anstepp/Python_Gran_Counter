#set up a circular buffer object

class CircularBuffer:
    
    def __init__(self):
        self.samples = []
        self.input_counter = 0
        self.output_counter = 0


    def _advance_input_counter(self):
        if input_counter < len(samples):
            input_counter += 1
        else:
            input_counter = 0

    def _advance_output_counter(self):
        if output_counter < len(samples):
            output_counter += 1
        else:
            output_counter = 0

    def read_output(self):
        self._advance_output_counter()
        return samples[output_counter]

    def _read_input(self, read_sample):
        samples[input_counter] = read_sample
        self._advance_input_counter()