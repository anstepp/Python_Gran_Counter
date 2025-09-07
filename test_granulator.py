import pytest

from granulator import Granulator, Window

@pytest.fixture
def sample_window():
    sample_window = [0, 1, 2]
    yield sample_window

@pytest.fixture
def sample_gran():
    sample_gran = [0, 1, 2]
    yield sample_gran

@pytest.fixture
def sample_objects(sample_window, sample_gran):
    window_object = Window(sample_window)
    granulator_object = Granulator(sample_gran)
    yield window_object, granulator_object

def test_gran_init(sample_window, sample_gran):
    pass

def test_window_init(sample_window, sample_gran):
    pass

def test_return_sample(sample_window, sample_gran):
    pass