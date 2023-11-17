"""Tests if  ``n_dimensions`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numpy_arrays/test_n_dimensions.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np


### FUNCTION IMPORT ###
from paramcheckup.numpy_arrays import n_dimensions


os.system("cls")


class Test_integer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.array = np.array([1, 2, 3, 4, 5])
        cls.param_name = "x_data"
        cls.ndim = 1
        cls.kind = "function"
        cls.kind_name = "ttest"
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = n_dimensions(
            self.array,
            self.param_name,
            self.ndim,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = n_dimensions(
            array=self.array,
            param_name=self.param_name,
            ndim=self.ndim,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when value has 2 dimensions"
        ):
            x = np.array([[1, 2, 3, 4]])
            output = n_dimensions(
                array=x,
                param_name=self.param_name,
                ndim=1,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )

        with self.assertRaises(
            ValueError, msg="Does not raised error when value has 2 dimensions"
        ):
            x = np.array([1, 2, 3, 4])
            output = n_dimensions(
                array=x,
                param_name=self.param_name,
                ndim=2,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )

    def test_raises_error_false(self):
        with self.assertRaises(
            SystemExit, msg="Does not raised error when value has 2 dimensions"
        ):
            x = np.array([[1, 2, 3, 4]])
            output = n_dimensions(
                array=x,
                param_name=self.param_name,
                ndim=1,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )

        with self.assertRaises(
            SystemExit, msg="Does not raised error when value has 2 dimensions"
        ):
            x = np.array([1, 2, 3, 4])
            output = n_dimensions(
                array=x,
                param_name=self.param_name,
                ndim=2,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )

    def test_pass(self):
        x = np.array([1, 2, 3, 4])
        output = n_dimensions(
            array=x,
            param_name=self.param_name,
            ndim=1,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=True,
        )
        self.assertTrue(
            output, msg="Does not return True when the input is np.array([1,2,3,4])"
        )

        x = np.array([[1, 2, 3, 4]])
        output = n_dimensions(
            array=x,
            param_name=self.param_name,
            ndim=2,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=True,
        )
        self.assertTrue(
            output, msg="Does not return True when the input is np.array([[1,2,3,4]])"
        )

    def test_pass_error_false(self):
        x = np.array([1, 2, 3, 4])
        output = n_dimensions(
            array=x,
            param_name=self.param_name,
            ndim=1,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(
            output, msg="Does not return True when the input is np.array([1,2,3,4])"
        )

        x = np.array([[1, 2, 3, 4]])
        output = n_dimensions(
            array=x,
            param_name=self.param_name,
            ndim=2,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(
            output, msg="Does not return True when the input is np.array([[1,2,3,4]])"
        )


if __name__ == "__main__":
    unittest.main()
