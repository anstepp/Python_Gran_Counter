import pytest

from gran_counter import CircularBuffer

good_buffer = [0.0, 0.1, 0.2, 0.3]
bad_buffer = [1, "string", "bad"]

def test_gran_init():
    """
        Test init function properly takes in the buffer and
        float-ifys it.
    """
    GoodBuffer = CircularBuffer(good_buffer)
    for supposed_to_be_float in GoodBuffer.samples:
        assert type(supposed_to_be_float) == float

    BadBuffer = CircularBuffer(bad_buffer)
    for supposed_to_be_float in BadBuffer.samples:
        assert type(supposed_to_be_float) != float


def test_increment_input():
    IncrementTestBuffer = CircularBuffer(good_buffer)
    assert IncrementTestBuffer.input_counter == 0
    IncrementTestBuffer._advance_input_counter()
    assert IncrementTestBuffer.input_counter == 1


def test_increment_output():
    IncrementTestBuffer = CircularBuffer(good_buffer)

def test_sample_length():
    IncrementTestBuffer = CircularBuffer(good_buffer)
    assert len(IncrementTestBuffer.samples) == 4