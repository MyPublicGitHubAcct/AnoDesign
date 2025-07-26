import numpy as np


class DcBlock:
    """
    A one-pole high-pass filter to remove DC components. Equivalent to the GenExpr:
    History x1, y1; y = in1 - x1 + y1*0.9997; x1 = in1; y1 = y; out1 = y;
    The 'r' variable determines how aggressively the filter removes very low frequencies,
    especially DC (0 Hz). It is typically in range [0.995, 0.9999].
    """
    def __init__(self, r=0.9997):
        self.r = r
        self.x1 = 0.0
        self.y1 = 0.0

    def process_sample(self, in1):
        res = in1 - self.x1 + self.y1 * self.r
        self.x1 = in1
        self.y1 = res
        return res

    def process_block(self, block):
        out = np.zeros_like(block)
        for i, x in enumerate(block):
            out[i] = self.process_sample(x)
        return out
