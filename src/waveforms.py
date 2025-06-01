"""https://docs.cycling74.com/userguide/gen/gen~_operators/"""

import numpy as np


class Phasor:
    """
    A non-bandlimited sawtooth-waveform signal generator which can be used as LFO
    audio signal or a sample-accurate timing/control signal.
    """

    def __init__(self, sample_rate=44100, frequency=440.0, phase=0.0):
        self.sample_rate = sample_rate
        self.frequency = frequency
        self.phase = phase
        self.phase_increment = self.frequency / self.sample_rate

    def change_frequency(self, new_frequency):
        """Changes the frequency of the phasor."""
        self.frequency = new_frequency
        self.phase_increment = self.frequency / self.sample_rate

    def get_next_sample(self):
        """Returns the next sample and updates the phase."""
        sample = self.phase % 1.0  # Ensure phase stays in range [0,1)
        self.phase += self.phase_increment
        return sample

    def get_block_of_samples(self, number_of_samples):
        """Returns a block of samples and updates the phase correctly."""
        phases = (
            self.phase + np.cumsum(np.full(number_of_samples, self.phase_increment))
        ) % 1.0
        self.phase = phases[-1]  # Update phase for next call
        return phases.tolist()
