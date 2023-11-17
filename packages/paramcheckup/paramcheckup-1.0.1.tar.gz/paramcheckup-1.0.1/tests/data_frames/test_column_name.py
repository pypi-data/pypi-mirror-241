"""Tests if  ``column_name`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/data_frames/test_column_name.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import pandas as pd


### FUNCTION IMPORT ###
from paramcheckup.data_frames import column_name


os.system("cls")


class Test_column_name(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.column_name = "A"
        cls.data_frame = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [4, 5, 6],
            }
        )
        cls.param_name = "data_frame"
        cls.kind = "function"
        cls.kind_name = "database"
        cls.stacklevel = 3
        cls.error = True

    def test_outputs(self):
        output = column_name(
            self.column_name,
            self.data_frame,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = column_name(
            column_name=self.column_name,
            data_frame=self.data_frame,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        names = [1, "b", "And"]
        for name in names:
            with self.assertRaises(
                ValueError,
                msg="Does not raised ValueError when value column_name not in dataframe",
            ):
                output = column_name(
                    column_name=name,
                    data_frame=self.data_frame,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_error_false(self):
        names = [1, "b", "And"]
        for name in names:
            with self.assertRaises(
                SystemExit,
                msg="Does not raised SystemExit when value column_name not in dataframe",
            ):
                output = column_name(
                    column_name=name,
                    data_frame=self.data_frame,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )

    def test_pass_error_false(self):
        names = ["A", "B"]
        for name in names:
            output = column_name(
                column_name=name,
                data_frame=self.data_frame,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )
            self.assertTrue(output, msg="not True when must be True")


if __name__ == "__main__":
    unittest.main()
