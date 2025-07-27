from typing import Union
import numpy as np

# Functions - no memory needed


# Classes - memory needed

class GainControl:
    def __init__(self, initial_gain: float = 1.0):
        self.current_gain = initial_gain
        self.target_gain = initial_gain
        self.step = 0.0
        self.samples_left = 0

    def set_gain(self, new_gain: float, ramp_length: int = 1):
        if ramp_length < 1:
            raise ValueError("ramp_length must be >= 1")
        self.target_gain = new_gain
        self.samples_left = ramp_length
        if ramp_length == 1:
            # Instant change
            self.current_gain = new_gain
            self.step = 0.0
            self.samples_left = 0
        else:
            self.step = (self.target_gain - self.current_gain) / ramp_length

    def process_sample(self, x: float) -> float:
        if self.samples_left > 0:
            self.current_gain += self.step
            self.samples_left -= 1
            if self.samples_left == 0:
                self.current_gain = self.target_gain
                self.step = 0.0
        return x * self.current_gain

    def process_block(self, x: Union[np.ndarray, list]) -> np.ndarray:
        x = np.asarray(x)
        y = np.empty_like(x, dtype=float)

        for i in range(len(x)):
            if self.samples_left > 0:
                self.current_gain += self.step
                self.samples_left -= 1
                if self.samples_left == 0:
                    self.current_gain = self.target_gain
                    self.step = 0.0
            y[i] = x[i] * self.current_gain

        return y




