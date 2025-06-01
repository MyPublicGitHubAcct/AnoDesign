import pytest
import numpy as np
from operators import Accum, Buffer, History, Peek
# from waveforms import Phasor


@pytest.fixture
def new_accum():
    return Accum(5)


@pytest.fixture
def new_buffer():
    return Buffer("test_buffer", np.array([[0.01, 0.02, 0.03], [0.04, 0.05, 0.06]]))


@pytest.fixture
def new_history():
    last_value = 3
    return History(last_value)


@pytest.fixture
def new_peek_buffer():
    data = np.array([[0.04, 0.05, 0.06], [0.01, 0.02, 0.03]])
    buffer = Buffer("test_peek_buffer", data)
    return Peek(buffer.get_data(), buffer.get_number_channels())


@pytest.fixture
def new_wrap_expectations():
    return [
        (5.5, 0.0, 5.0, 0.5),
        (-1.0, 0.0, 5.0, 4.0),
        (12.3, 3.0, 7.0, 4.3),
        (3.0, 3.0, 7.0, 3.0),
        (7.0, 3.0, 7.0, 3.0),
    ]
