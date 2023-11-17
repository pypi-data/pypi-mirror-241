"""Tests if  ``param_options`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/parameters/test_param_options.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest


### FUNCTION IMPORT ###
from paramcheckup.parameters import param_options


os.system("cls")


class Test_param_options(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.option = "a"
        # cls.options = ["a", "b", "c"]
        # cls.params = [
        #     1,
        #     "1",
        #     False,
        #     [False],
        #     {True},
        #     (1, 1, 1),
        # ]
        cls.option = "tukey"
        cls.options = ["tukey", "fisher", "dunett"]
        cls.param_name = "test"
        cls.kind = "function"
        cls.kind_name = "comparison_test"
        cls.stacklevel = 3
        cls.error = (True,)

    def test_outputs(self):
        output = param_options(
            self.option,
            self.options,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")
        output = param_options(
            option=self.option,
            options=self.options,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        values = ["blom", 1, False, ["tukey"]]
        for value in values:
            with self.assertRaises(
                ValueError, msg=f"Does not raised error for {value}"
            ):
                output = param_options(
                    option=value,
                    options=self.options,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_error_false(self):
        values = ["blom", 1, False, ["tukey"]]
        for value in values:
            with self.assertRaises(
                SystemExit, msg=f"Does not raised SystemExit for {value}"
            ):
                output = param_options(
                    option=value,
                    options=self.options,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )

    def test_pass(self):
        options = [
            1,
            "cinco",
            True,
            "blom",
            [1],
        ]
        values = [
            1,
            "cinco",
            True,
            "blom",
            [1],
        ]
        for value in values:
            result = param_options(
                option=value,
                options=options,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
            self.assertTrue(result, msg=f"raised error when {value}")

    def test_pass_erro_false(self):
        options = [
            1,
            "cinco",
            True,
            "blom",
            [1],
        ]
        values = [
            1,
            "cinco",
            True,
            "blom",
            [1],
        ]
        for value in values:
            result = param_options(
                option=value,
                options=options,
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )
            self.assertTrue(result, msg=f"raised error when {value}")


if __name__ == "__main__":
    unittest.main()
