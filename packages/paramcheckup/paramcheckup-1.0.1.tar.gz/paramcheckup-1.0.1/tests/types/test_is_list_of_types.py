"""Tests if  ``is_list_of_types`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/types/test_is_list_of_types.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest


### FUNCTION IMPORT ###
from paramcheckup.types import is_list_of_types


os.system("cls")


class Test_is_list_of_types(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.my_list = [1, 2, 3, 4]
        cls.expected_type = int
        cls.param_name = "comparison_test"
        cls.kind = "function"
        cls.kind_name = "ttest"
        cls.stacklevel = 3
        cls.error = True

        cls.values = [
            [[1, 2, 3, 4], int],
            [[1.1, 2.2, 3.3, 4.4], float],
            [["Anderson", "Marcos", "Dias"], str],
            [[["Anderson"], ["Marcos"], ["Dias"]], list],
            [[{"Anderson": 1}, {"Marcos": 2}, {"Dias": 4}], dict],
        ]

        cls.raises = [
            [["1", "2", 3], str],
            [["1", "2", 3], int],
            [["1", "2", 3.1], float],
            [["1", {"2": 2}, 3.1, 2, [1, 2], (1, 2, 3)], float],
        ]

    def test_outputs(self):
        output = is_list_of_types(
            self.my_list,
            self.expected_type,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = is_list_of_types(
            my_list=self.my_list,
            expected_type=self.expected_type,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_pass(self):
        for i in range(len(self.values)):
            output = is_list_of_types(
                my_list=self.values[i][0],
                expected_type=self.values[i][1],
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=self.error,
            )
            self.assertTrue(output, msg="not True when must be True")

    def test_pass_error_false(self):
        for i in range(len(self.values)):
            output = is_list_of_types(
                my_list=self.values[i][0],
                expected_type=self.values[i][1],
                param_name=self.param_name,
                kind=self.kind,
                kind_name=self.kind_name,
                stacklevel=self.stacklevel,
                error=False,
            )
            self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        with self.assertRaises(
            TypeError, msg="Does not raised error when has a str when it should not"
        ):
            for i in range(len(self.values)):
                output = is_list_of_types(
                    my_list=self.raises[i][0],
                    expected_type=self.values[i][1],
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=True,
                )

    def test_raises_error_false(self):
        with self.assertRaises(
            SystemExit,
            msg="Does not raised SystemExit when has a str when it should not",
        ):
            for i in range(len(self.values)):
                output = is_list_of_types(
                    my_list=self.raises[i][0],
                    expected_type=self.values[i][1],
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )


if __name__ == "__main__":
    unittest.main()
