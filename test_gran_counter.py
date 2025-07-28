import pytest

from gran_counter import CircularBuffer

test_buffer = [0.0, 0.1, 0.2, 0.3]

def test_gran_init():
    """
        Test init function properly takes in the buffer and
        float-ifys it.
    """
    TestBuffer = CircularBuffer(test_buffer)
    for supposed_to_be_float in TestBuffer.samples:
        assert type(supposed_to_be_float) == float

def test_increment_input():
    pass

def test_increment_output():
    pass

def test_sample_length():
    pass