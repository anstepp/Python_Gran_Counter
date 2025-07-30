import pytest

from circular_buffer import CircularBuffer

good_buffer = [0.0, 0.1, 0.2, 0.3]
bad_buffer = [1, "string", "bad"]

@pytest.fixture
def good_buffer_obj():
    test_buffer = CircularBuffer(good_buffer)
    yield test_buffer

@pytest.fixture
def bad_buffer_obj():
    test_buffer = CircularBuffer(bad_buffer)
    yield test_buffer

def test_gran_init(good_buffer_obj, bad_buffer_obj):
    """
        Test init function properly takes in the buffer and
        float-ifys it.
    """
    for supposed_to_be_float in good_buffer_obj.samples:
        assert type(supposed_to_be_float) == float

    for supposed_to_be_float in bad_buffer_obj.samples:
        assert type(supposed_to_be_float) != float


def test_increment_input(good_buffer_obj):
    assert good_buffer_obj.input_counter == 0
    good_buffer_obj._advance_input_counter()
    assert good_buffer_obj.input_counter == 1
    good_buffer_obj._advance_input_counter()
    good_buffer_obj._advance_input_counter()
    good_buffer_obj._advance_input_counter()
    assert good_buffer_obj.input_counter == 0


def test_increment_output(good_buffer_obj):
    assert good_buffer_obj.output_counter == 0
    good_buffer_obj._advance_output_counter()
    assert good_buffer_obj.output_counter == 1
    good_buffer_obj._advance_output_counter()
    good_buffer_obj._advance_output_counter()
    good_buffer_obj._advance_output_counter()
    assert good_buffer_obj.output_counter == 0

def test_sample_length(good_buffer_obj):
    assert len(good_buffer_obj.samples) == 4