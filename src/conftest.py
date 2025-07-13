import pytest
import numpy as np
from scipy import signal as sg
from operators import Accumulator, Buffer, Counter, History, Latch
from filters import DcBlock
# from waveforms import Phasor


@pytest.fixture
def new_accumulator():
    return Accumulator(5)


@pytest.fixture
def new_buffer():
    return Buffer("test_buffer", np.array([[0.01, 0.02, 0.03], [0.04, 0.05, 0.06]]))


@pytest.fixture
def new_counter_10():
    return Counter(1, 9)


@pytest.fixture
def new_counter_8():
    return Counter(1, 7)


@pytest.fixture
def new_history():
    last_value = 3
    return History(last_value)


@pytest.fixture
def new_latch():
    return Latch()


@pytest.fixture
def new_peek_buffer():
    data = np.array([[0.04, 0.05, 0.06], [0.01, 0.02, 0.03]])
    buffer = Buffer("test_peek_buffer", data)
    return buffer


@pytest.fixture
def new_saw():
    t = np.linspace(0, 1, 500)
    return sg.sawtooth(2 * np.pi * 5 * t)


@pytest.fixture
def new_wrap_expectations():
    return [
        (5.5, 0.0, 5.0, 0.5),
        (-1.0, 0.0, 5.0, 4.0),
        (12.3, 3.0, 7.0, 4.3),
        (3.0, 3.0, 7.0, 3.0),
        (7.0, 3.0, 7.0, 3.0),
    ]
