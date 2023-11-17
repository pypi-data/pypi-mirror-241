"""Tests if  ``empty_array`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numpy_arrays/test_empty_array.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np


### FUNCTION IMPORT ###
from paramcheckup.numpy_arrays import empty_array


os.system("cls")


class Test_empty_array(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.array = np.array([1, 2, 3])
        cls.param_name = "x_data"
        cls.kind = "function"
        cls.kind_name = "ttest"
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = empty_array(
            self.array,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = empty_array(
            array=self.array,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises_array(self):
        with self.assertRaises(
            ValueError, msg="Does not raised error when the numpy array is empty"
        ):
            x = np.array([])
            output = empty_array(
                array=x,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )

    def test_raises_error_false(self):
        with self.assertRaises(
            SystemExit, msg="Does not raised SystemExit when the numpy array is empty"
        ):
            x = np.array([])
            output = empty_array(
                array=x,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )

    def test_correct(self):
        x = np.array([1, 2, 3, 4])
        output = empty_array(
            array=x,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(
            output, msg="Does not return True when the input is np.array([1,2,3,4])"
        )

    def test_correct_error_false(self):
        x = np.array([1, 2, 3, 4])
        output = empty_array(
            array=x,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(
            output, msg="Does not return True when the input is np.array([1,2,3,4])"
        )


if __name__ == "__main__":
    unittest.main()
