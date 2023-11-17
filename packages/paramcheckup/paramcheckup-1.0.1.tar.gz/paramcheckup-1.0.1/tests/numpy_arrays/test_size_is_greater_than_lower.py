"""Tests if  ``size_is_greater_than_lower`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numpy_arrays/test_size_is_greater_than_lower.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np


### FUNCTION IMPORT ###
from paramcheckup.numpy_arrays import size_is_greater_than_lower


os.system("cls")


class Test_cast_greater_than_n(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x_exp = np.array([1, 2, 3])
        cls.param_name = "x_data"
        cls.kind = "function"
        cls.kind_name = "linear_regression"
        cls.lower = 3
        cls.inclusive = True
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = size_is_greater_than_lower(
            self.x_exp,
            self.param_name,
            self.kind,
            self.kind_name,
            self.lower,
            self.inclusive,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when it should")

        output = size_is_greater_than_lower(
            array=self.x_exp,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            lower=self.lower,
            inclusive=self.inclusive,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when it should")

    def test_raises_inclusive_true(self):
        datas = [
            np.array([1, 1, 1, 1, 1]),
            np.array([1, 1]),
            np.array([1, 1]),
        ]
        lowers = [6, 6, 3]
        for data, lower in zip(datas, lowers):
            with self.assertRaises(
                ValueError, msg=f"Does not raised size is lower={lower} than expected"
            ):
                output = size_is_greater_than_lower(
                    array=data,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    lower=lower,
                    inclusive=self.inclusive,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_inclusive_false(self):
        datas = [
            np.array([1, 1, 1, 1, 1]),
            np.array([1, 1, 1]),
            np.array([1, 1]),
        ]
        lowers = [5, 3, 3]
        for data, lower in zip(datas, lowers):
            with self.assertRaises(
                ValueError, msg=f"Does not raised size is lower={lower} than expected"
            ):
                output = size_is_greater_than_lower(
                    array=data,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    lower=lower,
                    inclusive=False,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_inclusive_true(self):
        datas = [
            np.array([1, 1, 1, 1, 1]),
            np.array([1, 1, 1, 1, 1]),
            np.array([1, 1, 1]),
        ]
        lowers = [5, 4, 3]
        for data, lower in zip(datas, lowers):
            output = size_is_greater_than_lower(
                array=data,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                lower=lower,
                inclusive=self.inclusive,
                stacklevel=self.stacklevel,
                error=self.error,
            )
            self.assertTrue(output, msg="not True when it should")

    def test_inclusive_false(self):
        datas = [
            np.array([1, 1, 1, 1, 1, 1, 1]),
            np.array([1, 1, 1, 1, 1, 1]),
            np.array([1, 1, 1, 1, 1]),
        ]
        lowers = [6, 5, 4]
        for data, lower in zip(datas, lowers):
            output = size_is_greater_than_lower(
                array=data,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                lower=lower,
                inclusive=False,
                stacklevel=self.stacklevel,
                error=self.error,
            )
            self.assertTrue(output, msg="not True when it should")

    def test_raises_error_false(self):
        with self.assertRaises(SystemExit, msg="Does not raised eSystemExitm"):
            output = size_is_greater_than_lower(
                array=np.array([1, 1, 1, 1]),
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                lower=4,
                inclusive=False,
                stacklevel=self.stacklevel,
                error=False,
            )

        with self.assertRaises(SystemExit, msg="Does not raised SystemExit"):
            output = size_is_greater_than_lower(
                array=np.array([1, 1, 1, 1]),
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                lower=5,
                inclusive=True,
                stacklevel=self.stacklevel,
                error=False,
            )

    def test_error_false(self):
        output = size_is_greater_than_lower(
            array=np.array([1, 1, 1, 1, 1]),
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            lower=4,
            inclusive=False,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(output, msg="not True when it should")

        output = size_is_greater_than_lower(
            array=np.array([1, 1, 1, 1]),
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            lower=4,
            inclusive=True,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(output, msg="not True when it should")


if __name__ == "__main__":
    unittest.main()
