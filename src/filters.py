import numpy as np


class DcBlock:
    """
    A one-pole high-pass filter to remove DC components. Equivalent to the GenExpr:
    History x1, y1; y = in1 - x1 + y1*0.9997; x1 = in1; y1 = y; out1 = y;
    """
    def __init__(self):
        self.x1 = 0.0
        self.y1 = 0.0

    def process_sample(self, in1):
        res = in1 - self.x1 + self.y1 * 0.9997
        self.x1 = in1
        self.y1 = res
        return res

    def process_block(self, block):
        out = np.zeros_like(block)
        for i, x in enumerate(block):
            out[i] = self.process_sample(x)
        return out
