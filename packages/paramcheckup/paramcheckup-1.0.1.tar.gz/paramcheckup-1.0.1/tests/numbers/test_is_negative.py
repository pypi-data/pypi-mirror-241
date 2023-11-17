"""Tests if  ``is_negative`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numbers/test_is_negative.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest


### FUNCTION IMPORT ###
from paramcheckup.numbers import is_negative


os.system("cls")


class Test_is_negative(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.number = -10
        cls.param_name = "hypotenuse"
        cls.kind = "function"
        cls.kind_name = "pitagoras"
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = is_negative(
            self.number,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")
        output = is_negative(
            number=self.number,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises_zero_positive(self):
        values = [0, 0.0, 1, 0.00000000000001, 10000000000.111111]
        for value in values:
            with self.assertRaises(
                ValueError, msg=f"Does not raised error when value is {value}"
            ):
                output = is_negative(
                    number=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_pass(self):
        values = [-1, -1.0000001, -1186486464161647]
        for value in values:
            output = is_negative(
                number=value,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
            self.assertTrue(output, msg=f"Does not returned True when value is {value}")

    def test_raises_error_false(self):
        values = [0, 0.0, 1, 0.00000000000001, 10000000000.111111]
        for value in values:
            with self.assertRaises(SystemExit, msg=f"Does not raised SystemExit"):
                output = is_negative(
                    number=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )

    def test_pass_erro_false(self):
        values = [-1, -1.0000001, -1186486464161647]
        for value in values:
            output = is_negative(
                number=value,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )
            self.assertTrue(output, msg=f"Does not returned True when value is {value}")


if __name__ == "__main__":
    unittest.main()
