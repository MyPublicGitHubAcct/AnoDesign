import objects

import numpy as np

from conftest import default_gain_control

"""
Tests for objects.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q src/test_objects.py
"""

def test_process_single_sample(default_gain_control):
    assert default_gain_control.process_sample(0.5) == 0.5

def test_gain_change_linear_interp(default_gain_control):
    default_gain_control.set_gain(2.0, duration_samples=4)
    results = [default_gain_control.process_sample(1.0) for _ in range(5)]
    expected = [1.25, 1.5, 1.75, 2.0, 2.0]
    np.testing.assert_allclose(results, expected, atol=1e-6)

def test_block_processing_interp(default_gain_control, sample_block):
    default_gain_control.set_gain(2.0, duration_samples=len(sample_block))
    processed = default_gain_control.process_block(sample_block)
    # Expected gains linearly from 1.1 to 2.0 over 10 samples
    expected = np.linspace(1.1, 2.0, 10)
    np.testing.assert_allclose(processed, expected, atol=1e-6)

def test_no_gain_change(default_gain_control, sample_block):
    processed = default_gain_control.process_block(sample_block)
    np.testing.assert_allclose(processed, sample_block, atol=1e-6)

