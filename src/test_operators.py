import operators
import pytest

"""
Tests for operators.

To run all tests, type pytest at top level like:
    pytest

To run only the tests in this file, do this:
    pytest -q python/test_operators.py
"""


# --- Functions ---

# class TestModulo:
#
#   def test_modul0(self):
#     res = operators.modulo(10.5, 3.2)
#     assert res == 0.9


class TestPeek:
    def test_peek_get_second_sample_in_first_channel(self, new_peek_buffer):
        res = operators.peek(new_peek_buffer, 0, 1)
        assert res == 0.05

    def test_peek_get_first_sample_in_second_channel(self, new_peek_buffer):
        res = operators.peek(new_peek_buffer, 1, 0)
        assert res == 0.01


class TestPhaseWrap:
    def test_phase_wrap_within(self):
        res1 = operators.phase_wrap(2.516)
        res2 = operators.phase_wrap(-2.516)
        assert res1 == 2.516
        assert res2 == -2.516

    def test_phase_wrap_above(self):
        res = operators.phase_wrap(5.519)
        assert res == -0.7641853071795861

    def test_phase_wrap_below(self):
        res = operators.phase_wrap(-4.289)
        assert res == 1.9941853071795865


class TestSwitch:
    def test_switch_false(self):
        res = operators.switch(False, 0.35)
        assert res == 0.35

    def test_switch_true(self):
        res = operators.switch(True, 0.35)
        assert res == 0


class TestWrap:
    def test_wrap_range(self, new_wrap_expectations):
        for value, minimum, maximum, expected in new_wrap_expectations:
            res = operators.wrap(value, minimum, maximum)
            assert res == pytest.approx(expected)


# --- Classes ---


class TestAccumulator:

  def test_accumulator_no_reset(self, new_accumulator):
    res = new_accumulator.get_current_value(4, 0)
    assert res == 9

  def test_accumulator_with_reset(self, new_accumulator):
    res = new_accumulator.get_current_value(4, 1)
    assert res == 0


class TestBuffer:
    def test_new_buffer_has_name(self, new_buffer):
        res = new_buffer.get_name()
        assert res == "test_buffer"

    def test_new_buffer_has_channels(self, new_buffer):
        res = str(new_buffer.get_number_channels())
        assert res == "2"

    def test_new_buffer_has_length(self, new_buffer):
        res = str(new_buffer.get_channel_length())
        assert res == "3"

    def test_new_buffer_data(self, new_buffer):
        res1 = str(new_buffer.get_data()[0])
        assert res1 == "[0.01 0.02 0.03]"
        res2 = str(new_buffer.get_data()[1])
        assert res2 == "[0.04 0.05 0.06]"


class TestHistory:
    def test_history_get_last_value(self, new_history):
        res = new_history.get_last_value(4)
        next_res = new_history.get_last_value(5)
        assert res == 3
        assert next_res == 4
