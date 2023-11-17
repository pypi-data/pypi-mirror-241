"""Adapted Ui widgets for float and integer input."""

import re

from kivy.properties import BooleanProperty  # pylint: disable=no-name-in-module
from kivy.uix.textinput import TextInput


class FloatInput(TextInput):
    """FloatInput inherits from Kivy's TextInput class.

    The filtering capability of Kivy's built-in TextInput class for numeric
    value only allows the input of positive numbers. FloatInput extends the
    TextInput capability to allow positive and negative float numbers if
    required. To achieve this, a new BooleanProperty named allow_negative is
    introduced. Negative float number input is only possible if the the value
    of allow_negative is True.

    In the Buzz implementation, this is required to define the:

    * Voltage
    * Conductor radius
    * Bundle radius
    * Conductor angle offset
    * x-coordinates
    * y-coordinates
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_negative = BooleanProperty(None)
        self.allow_negative = False

    def insert_text(self, substring, from_undo=False):
        """Override insert_text function such that only negative float values
        are allowed. Regular expression check is used to achieve this goal.
        """

        pat = re.compile("[^0-9]")
        if "." in self.text:
            s = re.sub(pat, "", substring)
        else:
            s = ".".join([re.sub(pat, "", s) for s in substring.split(".", 1)])

        # Only allow the input of a minus sign at the beginning of the input
        # and if the input does not already have a minus sign.
        if (
            self.allow_negative
            and "-" == substring[0]
            and self.cursor_col == 0
            and "-" not in self.text
        ):
            s = "-" + s

        return super().insert_text(s, from_undo=from_undo)


class IntegerInput(TextInput):
    """IntegerInput inherits from Kivy's TextInput class.

    IntegerInput only allows positive integers as valid input.

    In the Buzz implementation, this is required to define the number of
    conductors in a line.
    """

    def insert_text(self, substring, from_undo=False):
        """Override insert_text function such that only positive integers are
        allowed. Regular expression check is used to achieve this goal.
        """

        pat = re.compile("[^0-9]")
        if self.cursor_col == 0 and substring[0] == "0":
            substring = substring[1:]
        s = re.sub(pat, "", substring)
        return super().insert_text(s, from_undo=from_undo)
