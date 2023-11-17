"""Tests if  ``is_lower_than`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numbers/test_is_lower_than.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest


### FUNCTION IMPORT ###
from paramcheckup.numbers import is_lower_than


os.system("cls")


class Test_is_lower_than(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.number = 0
        cls.upper = 1
        cls.param_name = "param"
        cls.kind = "function"
        cls.kind_name = "ttest"

    def test_outputs(self):
        output = is_lower_than(
            self.number,
            self.upper,
            self.param_name,
            self.kind,
            self.kind_name,
            True,
            4,
            True,
        )
        self.assertTrue(output, msg="not True when must be True")
        output = is_lower_than(
            number=self.number,
            upper=self.upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
            stacklevel=4,
            error=True,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises_error_false(self):
        with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
            value, upper = 0, -0.5
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=True,
                stacklevel=4,
                error=False,
            )

        with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
            value, upper = -10, -10.5
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
                stacklevel=4,
                error=False,
            )

    def test_pass_error_false(self):
        value, upper = 0, 0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
            stacklevel=4,
            error=False,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")

        value, upper = -1.5, -0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=False,
            stacklevel=4,
            error=False,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")

    def test_raises_inclusive_true(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = 0, -0.5
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=True,
                stacklevel=4,
                error=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = -10, -10.5
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=True,
                stacklevel=4,
                error=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = 100, 5
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=True,
                stacklevel=4,
                error=True,
            )

    def test_raises_inclusive_false(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = 0, -0.5
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
                stacklevel=4,
                error=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = -10, -10.5
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
                stacklevel=4,
                error=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = 100, 5
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
                stacklevel=4,
                error=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = 0, 0
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
                stacklevel=4,
                error=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = -10, -10
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
                stacklevel=4,
                error=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not lower than"
        ):
            value, upper = 10, 10
            result = is_lower_than(
                number=value,
                upper=upper,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                inclusive=False,
                stacklevel=4,
                error=True,
            )

    def test_pass_inclusive_true(self):
        value, upper = 0, 0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
            stacklevel=4,
            error=True,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")

        value, upper = -0.5, 0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
            stacklevel=4,
            error=True,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")

        value, upper = -1.5, -0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
            stacklevel=4,
            error=True,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")

        value, upper = 0.5, 0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=True,
            stacklevel=4,
            error=True,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")

    def test_pass_inclusive_false(self):
        value, upper = 0, 0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=False,
            stacklevel=4,
            error=True,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")

        value, upper = -0.5, 0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=False,
            stacklevel=4,
            error=True,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")

        value, upper = -1.5, -0.5
        result = is_lower_than(
            number=value,
            upper=upper,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            inclusive=False,
            stacklevel=4,
            error=True,
        )
        self.assertTrue(result, msg="Raised error when value in lower than")


if __name__ == "__main__":
    unittest.main()
