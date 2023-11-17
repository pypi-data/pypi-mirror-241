"""Tests if  ``is_float_or_int`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numbers/test_is_float_or_int.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np


### FUNCTION IMPORT ###
from paramcheckup.numbers import is_float_or_int


os.system("cls")


class Test_is_float_or_int(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.number = 12
        cls.param_name = "alpha"
        cls.kind = "function"
        cls.kind_name = "ttest"
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = is_float_or_int(
            self.number,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = is_float_or_int(
            number=self.number,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises_error_false(self):
        values = [
            "\n asda",
            [1],
            (1, 1, 1),
        ]
        for value in values:
            with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
                output = is_float_or_int(
                    number=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )

    def test_pass_error_false(self):
        values = [
            1,
            1.1,
            np.int32(1),
            np.int64(1),
            np.uint(1),
            np.int32(10),
            np.int64(10),
            np.uint(1),
            np.float16(1),
        ]

        for value in values:
            result = is_float_or_int(
                number=value,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )
            self.assertTrue(result, msg=f"An error was raised when number is {value}")

    def test_string(self):
        with self.assertRaises(
            TypeError, msg="Does not raised error when value is a string"
        ):
            output = is_float_or_int(
                number="self.number",
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
        with self.assertRaises(
            TypeError, msg="Does not raised error when value is a string"
        ):
            output = is_float_or_int(
                number="\n asda",
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )

    def test_list(self):
        with self.assertRaises(
            TypeError, msg="Does not raised error when value is a list"
        ):
            output = is_float_or_int(
                number=[1],
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
        with self.assertRaises(
            TypeError, msg="Does not raised error when value is a list of list"
        ):
            output = is_float_or_int(
                number=[[1]],
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )

    def test_tuple(self):
        with self.assertRaises(
            TypeError, msg="Does not raised error when value is a tuple"
        ):
            output = is_float_or_int(
                number=(1,),
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
        with self.assertRaises(
            TypeError, msg="Does not raised error when value is a tuple"
        ):
            output = is_float_or_int(
                number=(1, 1, 1),
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
        with self.assertRaises(
            TypeError, msg="Does not raised error when value is a tuple"
        ):
            output = is_float_or_int(
                number=(1, (1,), 1),
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )

    def test_empty(self):
        with self.assertRaises(
            TypeError, msg="Does not raised error when no value was passed"
        ):
            output = is_float_or_int(
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )

    def test_pass(self):
        values = [
            1,
            1.1,
            np.int32(1),
            np.int64(1),
            np.uint(1),
            np.int32(10),
            np.int64(10),
            np.uint(1),
            np.float16(1),
        ]

        for value in values:
            result = is_float_or_int(
                number=value,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
            self.assertTrue(result, msg=f"An error was raised when number is {value}")


if __name__ == "__main__":
    unittest.main()
