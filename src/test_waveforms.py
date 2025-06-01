"""
Tests for waveforms.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q python/test_waveforms.py
"""

from waveforms import Phasor


def test_phasor():
    sample_rate = 44100
    test_frequencies = [6, 60, 600, 6000]
    phasor = Phasor(sample_rate)

    for freq in test_frequencies:
        phasor.change_frequency(freq)
        samples = [phasor.get_next_sample() for _ in range(10)]

        # Ensure values stay within expected range
        assert all(0.0 <= s < 1.0 for s in samples)

        # Ensure monotonic increase (except wrapping)
        for i in range(1, len(samples)):
            assert samples[i] >= samples[i - 1] or samples[i - 1] > samples[i]

        # Check phase wrapping
        phasor.phase = 0.99  # Near wrap point
        sample1 = phasor.get_next_sample()
        sample2 = phasor.get_next_sample()
        assert sample2 >= sample1 or sample1 > sample2  # Wrapping should occur properly


def test_get_block_of_samples():
    sample_rate = 44100
    test_frequencies = [6, 60, 600, 6000]
    phasor = Phasor(sample_rate)

    for freq in test_frequencies:
        phasor.change_frequency(freq)
        samples = phasor.get_block_of_samples(10)

        # Ensure all values are within expected range
        assert all(0.0 <= s < 1.0 for s in samples)

        # Ensure correct phase wrapping
        phasor.phase = 0.99
        samples = phasor.get_block_of_samples(10)
        assert all(0.0 <= s < 1.0 for s in samples)
