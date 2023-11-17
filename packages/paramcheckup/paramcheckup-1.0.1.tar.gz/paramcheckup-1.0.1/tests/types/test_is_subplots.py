"""Tests if  ``is_subplots`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/types/test_is_subplots.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np
import matplotlib.pyplot as plt

### FUNCTION IMPORT ###
from paramcheckup.types import is_subplots


os.system("cls")


class Test_is_subplots(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fig, cls.value = plt.subplots()
        cls.param_name = "axes"
        cls.kind = "function"
        cls.kind_name = "plot"
        cls.stacklevel = 3
        cls.error = True

        cls.raises = [
            "asdas",
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
        ]

    def test_outputs(self):
        output = is_subplots(
            self.value,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")
        output = is_subplots(
            value=self.value,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_outputs_error_false(self):
        output = is_subplots(
            self.value,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            False,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = is_subplots(
            value=self.value,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=False,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        for value in self.raises:
            with self.assertRaises(
                TypeError,
                msg=f"Does not raised error when value is a {type(value).__name__}",
            ):
                output = is_subplots(
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
                output = is_subplots(
                    value=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )


if __name__ == "__main__":
    unittest.main()
