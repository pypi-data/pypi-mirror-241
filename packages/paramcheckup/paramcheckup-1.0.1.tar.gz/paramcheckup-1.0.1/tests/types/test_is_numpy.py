"""Tests if  ``is_numpy`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/types/test_is_numpy.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np
import pandas as pd

### FUNCTION IMPORT ###
from paramcheckup.types import is_numpy


os.system("cls")


class Test_is_numpy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = np.array([1, 2, 3, 4, 5])
        cls.param_name = "x_data"
        cls.kind = "function"
        cls.kind_name = "ttest"
        cls.stacklevel = 3
        cls.error = True

        cls.values = [np.array([[1, 2, 3]]), np.array([1, 2, 3]), np.array([1])]

        cls.raises = [
            "anderson",
            1.1,
            np.float64(1),
            np.float16(1),
            1,
            (1,),
            (1, 1, 1),
            (1, (1,), 1),
            None,
            {"a": 1},
            set([1, 2, 3]),
            pd.Series([1, 2, 3]),
        ]

    def test_outputs(self):
        output = is_numpy(
            self.value,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = is_numpy(
            value=self.value,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        for value in self.raises:
            with self.assertRaises(
                TypeError,
                msg=f"Does not raised error when value is a {type(value).__name__}",
            ):
                output = is_numpy(
                    value=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_error_false(self):
        for value in self.raises:
            with self.assertRaises(
                SystemExit,
                msg=f"Does not raised SystemExit when value is a {type(value).__name__}",
            ):
                output = is_numpy(
                    value=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )

    def test_pass(self):
        for value in self.values:
            output = is_numpy(
                value=value,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
        self.assertTrue(output, msg="not True when must be True")

    def test_pass_error_false(self):
        for value in self.values:
            output = is_numpy(
                value=value,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )
        self.assertTrue(output, msg="not True when must be True")


if __name__ == "__main__":
    unittest.main()
