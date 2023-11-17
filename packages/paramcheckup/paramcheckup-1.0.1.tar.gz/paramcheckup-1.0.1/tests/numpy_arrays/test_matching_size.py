"""Tests if  ``matching_size`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numpy_arrays/test_matching_size.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np


### FUNCTION IMPORT ###
from paramcheckup.numpy_arrays import matching_size


os.system("cls")


class Test_matching_size(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arrays = [np.array([2, 4, 6, 8]), np.array([1, 2, 3, 4])]
        cls.param_names = ["concentration", "absorbance"]
        cls.kind = "function"
        cls.kind_name = "calibration"
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = matching_size(
            self.arrays,
            self.param_names,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = matching_size(
            arrays=self.arrays,
            param_names=self.param_names,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_pass(self):
        x_data = [
            np.array([1, 3, 5, 4]),
            np.array(
                [
                    1,
                    3,
                    5,
                    4,
                    5,
                    6,
                ]
            ),
            np.array(
                [
                    1,
                    3,
                ]
            ),
        ]
        y_data = [
            np.array([4, 6, 7, 8]),
            np.array([4, 6, 7, 8, 9, 2]),
            np.array(
                [
                    4,
                    6,
                ]
            ),
        ]

        for x, y in zip(x_data, y_data):
            output = matching_size(
                arrays=[x, y],
                param_names=self.param_names,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
            self.assertTrue(output, msg="not True when must be True")

        output = matching_size(
            arrays=[np.array([1, 2, 5]), np.array([6, 2, 3]), np.array([1, 2, 3])],
            param_names=["A", "B", "C"],
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = matching_size(
            arrays=[np.array(["4", "6", "7", "8"]), np.array(["1", "3", "5", "4"])],
            param_names=["A", "B"],
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_pass_error_false(self):
        output = matching_size(
            arrays=[np.array(["4", "6", "7", "8"]), np.array(["1", "3", "5", "4"])],
            param_names=["A", "B"],
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises_sizes_differ(self):
        x_data = [np.array([1, 3, 5, 4, 4]), np.array([1, 3, 5, 4, 4])]
        y_data = [np.array([4, 6, 7, 8]), np.array([4, 6, 7, 8, 5, 6, 8])]
        with self.assertRaises(
            ValueError, msg="Does not raised error when the sizes doesn't match"
        ):
            for x, y in zip(x_data, y_data):
                output = matching_size(
                    arrays=[x, y],
                    param_names=self.param_names,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_sizes_differ_error_false(self):
        x_data = [np.array([1, 3, 5, 4, 4]), np.array([1, 3, 5, 4, 4])]
        y_data = [np.array([4, 6, 7, 8]), np.array([4, 6, 7, 8, 5, 6, 8])]
        with self.assertRaises(
            SystemExit, msg="Does not raised SystemExit when the sizes doesn't match"
        ):
            for x, y in zip(x_data, y_data):
                output = matching_size(
                    arrays=[x, y],
                    param_names=self.param_names,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )


if __name__ == "__main__":
    unittest.main()
