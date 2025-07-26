import numpy as np

# Functions - no memory needed


# Classes - memory needed

'''
Write a dsp gain control  in python with linear interpolation & pytest tests and
conftest. Process by blocks or single samples.
'''
class GainControl:
    def __init__(self, initial_gain: float = 1.0):
        self.current_gain = float(initial_gain)
        self.target_gain = float(initial_gain)
        self.gain_step = 0.0
        self.steps_remaining = 0

    def set_gain(self, target_gain: float, duration_samples: int):
        self.target_gain = float(target_gain)
        self.steps_remaining = max(1, duration_samples)
        self.gain_step = (self.target_gain - self.current_gain) / self.steps_remaining

    def process_sample(self, sample: float) -> float:
        if self.steps_remaining > 0:
            self.current_gain += self.gain_step
            self.steps_remaining -= 1
        return sample * self.current_gain

    def process_block(self, block: np.ndarray) -> np.ndarray:
        out = np.zeros_like(block)
        for i in range(len(block)):
            out[i] = self.process_sample(float(block[i]))
        return out



