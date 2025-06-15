"""https://docs.cycling74.com/userguide/gen/gen~_operators/"""

import numpy as np


# Functions - no memory needed


def latch() -> float:
    pass


# def modulo(val1, val2):
#   # avoid division by 0
#   if val2 == 0:
#     return 0
#
#   # compute the quotient and result (remainder)
#   quotient = val1 / val2
#   result = val1 - quotient * val2
#
#   # wrap if needed
#   if (result < 0 < val2) or (result > 0 > val2):
#     result += val2
#
#   return result


def peek(buffer, channel: int, index: int) -> float:
    """
    Read values from a data/buffer object. The first argument should be a name of a data
    or buffer object in the gen patcher. The second argument specifies the number of
    output channels. The first inlet specifies a sample index to read
    (no interpolation); indices out of range return zero. The last inlet specifies a
    channel offset (default 0).
    """
    data = buffer.get_data()
    return data[channel][index]


def phase_wrap(angle):
    """
    :param angle: The input value
    :return: The input wrapped to the range -pi to +pi
    """
    angle = np.fmod(angle + np.pi, 2 * np.pi)
    if angle < 0:
        angle += 2 * np.pi

    return angle - np.pi


def scale() -> float:
    pass


def switch(reset: bool, new_value) -> float:
    """
    :param reset: If true (not 0) is received, the function outputs new_value. A 0 value
            will cause the function to output 0.
    :param new_value: A value received. Example: This can come from an addition to a
            history object.
    :return: A float, either 0 or new_value.
    """
    if reset:
        return 0
    else:
        return new_value


def wrap(value=0, minimum=0, maximum=1):
    """
    :param value: The input value
    :param minimum: minimum return value
    :param maximum: maximum return value
    :return: The input wrapped to the range minimum to maximum
    """
    rng = maximum - minimum
    if rng <= 0:
        return minimum
    else:
        return ((value - minimum) % rng + rng) % rng + minimum


# Classes - memory needed


class Accumulator:
    """
    The object adds to, and then outputs, an internal sum. This occurs at sample-rate,
    so the sum can grow very large, very fast. The value to be added is specified by
    either the first inlet or argument. The internal sum can be reset to the minimum
    by sending a nonzero value to the right-most inlet. The minimum value is 0 by
    default, but can be changed with the @min attribute. An optional maximum value
    can be specified with the @max attribute; values will wrap at the maximum.
    """

    def __init__(self, value=0, minimum=0, maximum=10):
        self.internal_value = value
        self.min = minimum
        self.max = maximum

    def get_current_value(self, value, reset) -> float:
        if reset != 0:
            self.internal_value = self.min
            return self.internal_value
        else:
            if value > self.max or value < self.min:
                value = wrap(value, self.min, self.max)
            return self.internal_value + value


class Buffer:
    """
    References a named buffer~ object in the gen~ object's parent patch. The first
    argument specifies a name by which to refer to this data in other objects in the
    gen patcher (such as peek and poke); the second optional argument specifies the
    name of the external buffer~ object to reference (if omitted, the first argument
    name is used). The first outlet sends the length of the buffer in samples; the
    second outlet sends the number of channels.

    from operators import Buffer
    arr = np.array([ [0.00], [0.00] ])
    buff = Buffer("new_buffer", arr)
    """

    def __init__(self, buffer_name: str, buffer_data=np.array([[0.00], [0.00]])):
        self.buffer_name = buffer_name
        self.buffer_data = buffer_data

        if buffer_data.all():
            self.buffer_number_channels = len(buffer_data)
            self.buffer_channel_length = len(
                self.buffer_data[0]
            )  # assumes same - otherwise, ValueError

    def get_name(self):
        return self.buffer_name

    def get_channel_length(self) -> int:
        return self.buffer_channel_length

    def get_number_channels(self) -> int:
        return self.buffer_number_channels

    def get_data(self):
        return self.buffer_data


class History:
    """
    The history operator allows feedback in the gen patcher through the insertion of a
    single-sample delay. The first argument is an optional name for the history
    operator, which allows it to also be set externally (in the same way as the param
    operator). The second argument specifies an initial value of stored history
    (defaults to zero).
    """

    def __init__(self, last_value):
        self.last_value = last_value

    def get_last_value(self, new_value):
        out = self.last_value
        self.last_value = new_value
        return out
