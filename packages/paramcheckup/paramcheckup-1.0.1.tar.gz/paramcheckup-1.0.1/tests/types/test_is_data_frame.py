"""Tests if  ``is_data_frame`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/types/test_is_data_frame.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import pandas as pd
import numpy as np

### FUNCTION IMPORT ###
from paramcheckup.types import is_data_frame


os.system("cls")


class Test_is_data_frame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame(
            {
                "Column A": [
                    1,
                    2,
                    4,
                    5,
                ]
            }
        )
        cls.param_name = "x_data"
        cls.kind = "function"
        cls.kind_name = "ttest"
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = is_data_frame(
            self.df,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = is_data_frame(
            data_frame=self.df,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
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
                output = is_data_frame(
                    data_frame=value,
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
                output = is_data_frame(
                    data_frame=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )

    def test_pass(self):
        df = pd.DataFrame(columns=["a", "b"])
        df["a"] = [1, 2]
        df["b"] = [3, 4]
        output = is_data_frame(
            data_frame=df,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=True,
        )
        self.assertTrue(output, msg="Returning False when the input is a DataFrame")

        output = is_data_frame(
            data_frame=df,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(output, msg="Returning False when the input is a DataFrame")


if __name__ == "__main__":
    unittest.main()
