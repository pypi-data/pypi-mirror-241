"""Tests if  ``is_empty`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/data_frames/test_is_empty.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import pandas as pd


### FUNCTION IMPORT ###
from paramcheckup.data_frames import is_empty


os.system("cls")


class Test_is_empty(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        output = is_empty(
            self.data_frame,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = is_empty(
            data_frame=self.data_frame,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        datas = [pd.DataFrame(data=[], columns=["columns"]), pd.DataFrame({})]
        for data in datas:
            with self.assertRaises(
                ValueError, msg="Does not raised error when the dataframe is empty"
            ):
                output = is_empty(
                    data_frame=data,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_errro_false(self):
        datas = [pd.DataFrame(data=[], columns=["columns"]), pd.DataFrame({})]
        for data in datas:
            with self.assertRaises(
                SystemExit, msg="Does not raised SystemExit when the dataframe is empty"
            ):
                output = is_empty(
                    data_frame=data,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )

    def test_pass_error_false(self):
        output = is_empty(
            self.data_frame,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            False,
        )
        self.assertTrue(output, msg="not True when must be True")


if __name__ == "__main__":
    unittest.main()
