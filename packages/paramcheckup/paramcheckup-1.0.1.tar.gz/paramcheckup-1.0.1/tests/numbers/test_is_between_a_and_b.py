"""Tests if  ``is_between_a_and_b`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:

    python -m unittest -v tests/numbers/test_is_between_a_and_b.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest


### FUNCTION IMPORT ###
from paramcheckup.numbers import is_between_a_and_b


os.system("cls")


class Test_is_between_a_and_b(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.number = 1
        cls.lower = 0
        cls.upper = 2
        cls.param_name = "param"
        cls.kind = "function"
        cls.kind_name = "ttest"

    def test_outputs(self):
        output = is_between_a_and_b(
            self.number,
            self.lower,
            self.upper,
            self.param_name,
            self.kind,
            self.kind_name,
            True,
            4,
            True,
        )
        self.assertTrue(output, msg="not True when must be True")
        output = is_between_a_and_b(
            number=self.number,
            lower=self.lower,
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
            value, lower, upper = -0.5, 1, 0
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
                error=False,
            )

        with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
            value, lower, upper = 0.5, -1, 0
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
                error=False,
            )

        with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
            value, lower, upper = -10.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
                error=False,
            )

        with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
            value, lower, upper = 60.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
                error=False,
            )

    def test_raises_inclusive_true_reverted(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -0.5, 1, 0
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 0.5, -1, 0
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -10.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 60.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
            )

    def test_raises_inclusive_true(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -0.5, 0, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 0.5, -1, 0
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -10.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 60.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=True,
            )

    def test_raises_inclusive_false(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -0.5, 0, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 0.5, -1, 0
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -10.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 60.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -1, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 1, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

    def test_raises_inclusive_false_reverted(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -0.5, 1, 0
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 0.5, -1, 0
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -10.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 60.5, -1, 1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = -1, 1, -1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value not in range"
        ):
            value, lower, upper = 1, 1, -1
            result = is_between_a_and_b(
                value,
                lower,
                upper,
                self.param_name,
                self.kind,
                self.kind_name,
                inclusive=False,
            )

    def test_pass_inclusive_true(self):
        value, lower, upper = 0.5, 0, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=True,
        )
        self.assertTrue(result, msg="Raised error when value in range")

        value, lower, upper = 0.0, 0, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=True,
        )
        self.assertTrue(result, msg="Raised error when value in range")

        value, lower, upper = 1, 0, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=True,
        )
        self.assertTrue(result, msg="Raised error when value in range")

        value, lower, upper = 0.5, -1, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=True,
        )
        self.assertTrue(result, msg="Raised error when value in range")

        value, lower, upper = -0.5, -1, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=True,
        )
        self.assertTrue(result, msg="Raised error when value in range")

    def test_pass_inclusive_false(self):
        value, lower, upper = 0.999999, 0, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=False,
        )
        self.assertTrue(result, msg="Raised error when value in range")

        value, lower, upper = 0.5, 0, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=False,
        )
        self.assertTrue(result, msg="Raised error when value in range")

        value, lower, upper = 0.5, -1, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=False,
        )
        self.assertTrue(result, msg="Raised error when value in range")

        value, lower, upper = -0.5, -1, 1
        result = is_between_a_and_b(
            value,
            lower,
            upper,
            self.param_name,
            self.kind,
            self.kind_name,
            inclusive=False,
        )
        self.assertTrue(result, msg="Raised error when value in range")


if __name__ == "__main__":
    unittest.main()
