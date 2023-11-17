"""Tests if  ``is_bool`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/types/test_is_bool.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np


### FUNCTION IMPORT ###
from paramcheckup.types import is_bool


os.system("cls")


class Test_boolean(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = True
        cls.param_name = "show"
        cls.kind = "function"
        cls.kind_name = "plot"
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = is_bool(
            self.value,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = is_bool(
            value=self.value,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_pass_error_false(self):
        output = is_bool(
            value=self.value,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        values = [
            "anderson",
            "as",
            1,
            np.int32(1),
            np.int64(1),
            [1],
            [[1]],
            (1,),
            (1, 1, 1),
            (1, (1,), 1),
            None,
        ]
        for value in values:
            with self.assertRaises(
                TypeError,
                msg=f"Does not raised error when value is a {type(value).__name__}",
            ):
                output = is_bool(
                    value=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_error_false(self):
        values = [
            "anderson",
            "as",
            1,
            np.int32(1),
            np.int64(1),
            [1],
            [[1]],
            (1,),
            (1, 1, 1),
            (1, (1,), 1),
            None,
        ]
        for value in values:
            with self.assertRaises(
                SystemExit,
                msg=f"Does not raised SystemExit when value is a {type(value).__name__}",
            ):
                output = is_bool(
                    value=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )


if __name__ == "__main__":
    unittest.main()
