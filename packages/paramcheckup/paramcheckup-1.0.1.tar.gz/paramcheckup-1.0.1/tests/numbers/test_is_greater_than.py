"""Tests if  ``is_greater_than`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numbers/test_is_greater_than.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest


### FUNCTION IMPORT ###
from paramcheckup.numbers import is_greater_than


os.system("cls")


class Test_is_greater_than(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.number = 1
        cls.lower = 0
        cls.param_name = "param"
        cls.kind = "function"
        cls.kind_name = "ttest"

    def test_outputs(self):
        output = is_greater_than(
            self.number, self.lower, self.param_name, self.kind, self.kind_name
        )
        self.assertTrue(output, msg="not True when must be True")
        output = is_greater_than(
            number=self.number,
            lower=self.lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
            stacklevel=3,
            error=True,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises_error_false(self):
        with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
            value, lower = -0.5, 0
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=True,
                error=False,
            )

        with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
            value, lower = -0.5, 0
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
                error=False,
            )

    def test_pass_error_false(self):
        value, lower = 0.5, 0
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=False,
            error=False,
        )
        self.assertTrue(result, msg="Raised error when value in greater than")

        value, lower = 0.5, -0.5
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
            error=False,
        )

    def test_raises_inclusive_true(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = -0.5, 0
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = -10.5, -10
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = 100, 500
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=True,
            )

    def test_raises_inclusive_false(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = -0.5, 0
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = -10.5, -10
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
            )
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = 100, 500
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = 0, 0
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = -10, -10
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not greater than"
        ):
            value, lower = 10, 10
            output = is_greater_than(
                number=value,
                lower=lower,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
            )

    def test_pass_inclusive_true(self):
        value, lower = 0.5, 0
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
        )

        self.assertTrue(result, msg="Raised error when value in greater than")

        value, lower = 0.5, -0.5
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
        )
        self.assertTrue(result, msg="Raised error when value in greater than")

        value, lower = -0.5, -1.5
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
        )
        self.assertTrue(result, msg="Raised error when value in greater than")

        value, lower = 0.5, 0.5
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
        )
        self.assertTrue(result, msg="Raised error when value in greater than")

    def test_pass_inclusive_false(self):
        value, lower = 0.5, 0
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=False,
        )
        self.assertTrue(result, msg="Raised error when value in greater than")

        value, lower = 0.5, -0.5
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=False,
        )
        self.assertTrue(result, msg="Raised error when value in greater than")

        value, lower = -0.5, -1.5
        result = is_greater_than(
            number=value,
            lower=lower,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=False,
        )
        self.assertTrue(result, msg="Raised error when value in greater than")


if __name__ == "__main__":
    unittest.main()
