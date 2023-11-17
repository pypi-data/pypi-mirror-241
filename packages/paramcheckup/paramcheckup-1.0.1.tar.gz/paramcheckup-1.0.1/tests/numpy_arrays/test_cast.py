"""Tests if  ``cast`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/numpy_arrays/test_cast.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np
import pandas as pd

### FUNCTION IMPORT ###
from paramcheckup.numpy_arrays import cast


os.system("cls")


class Test_cast(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.array = [1, 2, 3]
        cls.param_name = "x"
        cls.kind = "function"
        cls.kind_name = "ttest"
        cls.ndim = 1
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = cast(
            self.array,
            self.param_name,
            self.kind,
            self.kind_name,
            self.ndim,
            self.stacklevel,
            self.error,
        )

        self.assertTrue(
            np.allclose(output, np.array(self.array)), msg="arrays does not match"
        )

        output = cast(
            array=self.array,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            ndim=self.ndim,
            stacklevel=self.stacklevel,
            error=self.error,
        )

        self.assertTrue(
            np.allclose(output, np.array(self.array)), msg="arrays does not match"
        )

    def test_raises_error_false(self):
        with self.assertRaises(SystemExit, msg="Does not raised error when wrong dim"):
            y = [1, 2, 3, 4]
            output = cast(
                array=y,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                ndim=2,
                stacklevel=self.stacklevel,
                error=False,
            )

        datas = [
            {"abc": [1, 2, 3, 4]},
            set([1, 2, 3]),
            pd.DataFrame({"a": [1, 2, 3]}),
            pd.DataFrame(
                {
                    "a": [1, 2, 3],
                    "aa": [1, 2, 3],
                }
            ),
        ]
        for data in datas:
            with self.assertRaises(
                SystemExit, msg=f"Does not raised error for {type(data).__name__}"
            ):
                output = cast(
                    array=data,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    ndim=1,
                    stacklevel=self.stacklevel,
                    error=False,
                )

    def test_raises_n_dim(self):
        with self.assertRaises(ValueError, msg="Does not raised error when wrong dim"):
            y = [1, 2, 3, 4]
            output = cast(
                array=y,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                ndim=2,
                stacklevel=self.stacklevel,
                error=self.error,
            )

        with self.assertRaises(ValueError, msg="Does not raised error when wrong dim"):
            y = [[1, 2, 3, 4]]
            output = cast(
                array=y,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                ndim=1,
                stacklevel=self.stacklevel,
                error=self.error,
            )

    def test_raise_types(self):
        datas = [
            {"abc": [1, 2, 3, 4]},
            set([1, 2, 3]),
            pd.DataFrame({"a": [1, 2, 3]}),
            pd.DataFrame(
                {
                    "a": [1, 2, 3],
                    "aa": [1, 2, 3],
                }
            ),
        ]
        for data in datas:
            with self.assertRaises(
                ValueError, msg=f"Does not raised error for {type(data).__name__}"
            ):
                output = cast(
                    array=data,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    ndim=1,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_zero_dim(self):
        datas = [1, 0.1, ".1"]
        expecteds = [np.array([1]), np.array([0.1]), np.array([".1"])]
        for data, expected in zip(datas, expecteds):
            with self.assertRaises(
                ValueError, msg="Does not raised error when zero dim"
            ):
                output = cast(
                    array=data,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    ndim=1,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_correct(self):
        datas = [
            [1, 2, 3, 4],
            (1, 2, 3, 4),
            pd.Series([1, 2, 3, 4]),
            (1,),
            [[1, 4, 9, 16, 25, 36]],
            [
                [1, 4, 9, 16, 25, 36],
                [1, 4, 9, 16, 25, 36],
            ],
        ]
        expecteds = [
            np.array([1, 2, 3, 4]),
            np.array([1, 2, 3, 4]),
            np.array([1, 2, 3, 4]),
            np.array([1]),
            np.array([[1, 4, 9, 16, 25, 36]]),
            np.array(
                [
                    [1, 4, 9, 16, 25, 36],
                    [1, 4, 9, 16, 25, 36],
                ]
            ),
        ]
        ndims = [1, 1, 1, 1, 2, 2]

        for data, expected, ndim in zip(datas, expecteds, ndims):
            output = cast(
                array=data,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                ndim=ndim,
                stacklevel=self.stacklevel,
                error=self.error,
            )
            self.assertTrue(np.allclose(expected, output), msg="arrays does not match")

    def test_pass_error_false(self):
        datas = [
            [1, 2, 3, 4],
            (1, 2, 3, 4),
            pd.Series([1, 2, 3, 4]),
            (1,),
            [[1, 4, 9, 16, 25, 36]],
            [
                [1, 4, 9, 16, 25, 36],
                [1, 4, 9, 16, 25, 36],
            ],
        ]
        expecteds = [
            np.array([1, 2, 3, 4]),
            np.array([1, 2, 3, 4]),
            np.array([1, 2, 3, 4]),
            np.array([1]),
            np.array([[1, 4, 9, 16, 25, 36]]),
            np.array(
                [
                    [1, 4, 9, 16, 25, 36],
                    [1, 4, 9, 16, 25, 36],
                ]
            ),
        ]
        ndims = [1, 1, 1, 1, 2, 2]

        for data, expected, ndim in zip(datas, expecteds, ndims):
            output = cast(
                array=data,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                ndim=ndim,
                stacklevel=self.stacklevel,
                error=False,
            )
            self.assertTrue(np.allclose(expected, output), msg="arrays does not match")


if __name__ == "__main__":
    unittest.main()
