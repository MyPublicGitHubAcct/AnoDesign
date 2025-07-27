import objects
import pytest
import numpy as np

from conftest import gain_control

"""
Tests for objects.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q src/test_objects.py
"""

def test_initial_gain(gain_control):
    # initial gain is 1.0, processing sample returns same value
    x = 0.5
    y = gain_control.process_sample(x)
    assert y == pytest.approx(0.5)

def test_instant_gain_change(gain_control):
    gain_control.set_gain(2.0, ramp_length=1)
    y = gain_control.process_sample(1.0)
    assert y == pytest.approx(2.0)
    assert gain_control.current_gain == 2.0

def test_ramped_gain_single_samples(gain_control):
    gain_control.set_gain(2.0, ramp_length=4)
    inputs = [1.0, 1.0, 1.0, 1.0]
    expected_gains = [1.25, 1.5, 1.75, 2.0]
    outputs = []
    for expected_gain, x in zip(expected_gains, inputs):
        y = gain_control.process_sample(x)
        outputs.append(y)
        assert y == pytest.approx(expected_gain)
    assert gain_control.current_gain == 2.0
    assert gain_control.samples_left == 0

def test_process_block_constant_gain(gain_control):
    gain_control.set_gain(1.5, ramp_length=1)
    block = np.ones(5)
    out = gain_control.process_block(block)
    assert np.allclose(out, 1.5)

def test_process_block_with_ramp(gain_control):
    gain_control.set_gain(2.0, ramp_length=4)
    block = np.ones(4)
    out = gain_control.process_block(block)
    expected = np.array([1.25, 1.5, 1.75, 2.0])
    np.testing.assert_allclose(out, expected)
    assert gain_control.current_gain == 2.0
    assert gain_control.samples_left == 0

def test_process_block_partial_ramp(gain_control):
    gain_control.set_gain(3.0, ramp_length=6)
    block1 = np.ones(4)
    out1 = gain_control.process_block(block1)
    expected1 = np.array([1.3333333, 1.6666667, 2.0, 2.3333333])
    np.testing.assert_allclose(out1, expected1, rtol=1e-6)

    block2 = np.ones(2)
    out2 = gain_control.process_block(block2)
    expected2 = np.array([2.6666667, 3.0])
    np.testing.assert_allclose(out2, expected2, rtol=1e-6)

    assert gain_control.current_gain == 3.0
    assert gain_control.samples_left == 0


