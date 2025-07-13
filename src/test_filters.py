import filters
import numpy as np
import pytest

"""
Tests for filters.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q python/test_filters.py
"""


class TestDcBlock:
    def test_dc_block_get_next_value(self):
        fs = 48000
        t = np.linspace(0, 1, fs, endpoint=False)
        dc_offset = 1.0
        signal = np.sin(2 * np.pi * 440 * t) + dc_offset

        dc_filter = filters.DcBlock()
        filtered = dc_filter.process_block(signal)
        out = filtered[14000:]
        print(str(np.mean(out)))
        print(str(1e-3))
        assert abs(np.mean(out)) < 1e-3

