"""
##### List of functions (alphabetical order) #####

## Functions WITH TESTS ###
- is_bool(value, param_name, kind, kind_name, stacklevel=4, error=True)
- is_data_frame(data_frame, param_name, kind, kind_name, stacklevel=4, error=True)
- is_dict(value, param_name, kind, kind_name, stacklevel=4, error=True)
- is_float(value, param_name, kind, kind_name, stacklevel=4, error=True)
- is_int(value, param_name, kind, kind_name, stacklevel=4, error=True)
- is_list_of_types(my_list, expected_type, param_name, kind, kind_name, stacklevel=4, error=True)
- is_list(value, param_name, kind, kind_name, stacklevel=4, error=True)
- is_numpy(value, param_name, kind, kind_name, stacklevel=4, error=True)
- is_str(value, param_name, kind, kind_name, stacklevel=4, error=True)
- is_subplots(value, param_name, kind, kind_name, stacklevel=4, error=True)
- is_tuple(value, param_name, kind, kind_name, stacklevel=4, error=True)

## Functions WITH some TESTS (needs improvements) ###


## Functions WITHOUT tests ###

##### List of CLASS (alphabetical order) #####


Author: Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

Created: October 24, 2023.

Last update: October 26, 2023

"""

##### IMPORTS #####

### Standard ###
import sys

### Third part ###
import numpy as np
import pandas as pd
from matplotlib.axes import SubplotBase

### home made ###
from .utils import user_warning
from . import documentation as docs

##### CONSTANTS #####


##### CLASSES #####


##### FUNCTIONS #####


def is_generic_type():
    raise NotImplementedError


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_bool(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `value` is of the `bool` type.


    Parameters
    ----------
    {value}
        {value_desc} `bool`;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If `value` **IS** of the `bool` type;
    raises : TypeError
        If `value` is **NOT** of the `bool` type;


    Examples
    --------
    >>> from paramcheckup import types
    >>> result = types.is_bool(
        value=True,
        param_name="show",
        kind="function",
        kind_name="plot",
        stacklevel=3,
        error=True,
    )
    >>> print(result)
    True


    >>> from paramcheckup import types
    >>> result = types.is_bool(
        value="ok",
        param_name="show",
        kind="function",
        kind_name="plot",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The parameter `show` in function `plot` must be of type `bool`, but its type is `str`.

    """
    if isinstance(value, bool) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `bool`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotBoolError")
            except TypeError:
                raise
    return True


@docs.docstring_parameter(
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_data_frame(data_frame, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `data_frame` is of the :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` type.


    Parameters
    ----------
    data_frame : any type
        The variable that is tested as being of :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` type;
    {param_name}
        {param_name_desc} `data_frame`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If variable `data_frame` **IS** of the :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` type;
    raises : TypeError
        If variable `data_frame` is **NOT** of the :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` type;


    Examples
    --------
    >>> from paramcheckup import types
    >>> import pandas as pd
    >>> df = pd.DataFrame(data=[1, 2, 3, 4, 5], columns=["Dataset"])
    >>> result = types.is_data_frame(
        data_frame=df,
        param_name="x_data",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=True,
    )
    >>> print(result)
    True


    >>> from paramcheckup import types
    >>> import pandas as pd
    >>> df = [1, 2, 3, 4, 5]
    >>> result = types.is_data_frame(
        data_frame=df,
        param_name="x_data",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 4: The parameter `x_data` in function `ttest` must be of type `DataFrame`, but its type is `list`.


    """
    if isinstance(data_frame, pd.DataFrame) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `DataFrame`, but its type is `{type(data_frame).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotDataFrameError")
            except TypeError:
                raise

    return True


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_dict(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable *value* is of the *dict* type.

    Parameters
    ----------
    {value}
        {value_desc} `dict`;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If variable `value` **IS** of the `dict` type;
    raises : TypeError
        If variable `value` is **NOT** of the `dict` type;


    Examples
    --------
    >>> from paramcheckup import types
    >>> result = types.is_dict(
        value=dict(value_1=1, value_2=[1, 2, 3]),
        param_name="x_data",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=True,
    )
    >>> print(result)
    True


    >>> from paramcheckup import types
    >>> result = types.is_dict(
        value=[1, 2, 3, 4],
        param_name="x_data",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 4: The parameter `x_data` in function `ttest` must be of type `dict`, but its type is `list`.

    """
    if isinstance(value, dict) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `dict`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotDictError")
            except TypeError:
                raise

    return True


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_float(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable *value* is of the *float* type.


    Parameters
    ----------
    {value}
        {value_desc} `float`;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}

    Returns
    -------
    output : True
        If variable `value` **IS** of the `float` type;
    raises : TypeError
        If variable `value` is **NOT** of the `float` type;



    Notes
    -----
    The following types are considered to be `True`:

    * `float`;
    * `np.floating`;


    Examples
    --------
    >>> from paramcheckup import types
    >>> result = types.is_float(
        value=0.05,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=True,
    )
    >>> print(result)
    True


    >>> from paramcheckup import types
    >>> result = types.is_float(
        value=5,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The parameter `alpha` in function `ttest` must be of type `float`, but its type is `int`.

    """
    if isinstance(value, (float, np.floating)) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `float`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotFloatError")
            except TypeError:
                raise
    else:
        return True


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_int(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `value` is of the `int` type.

    Parameters
    ----------
    {value}
        {value_desc} `int`;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}

    Returns
    -------
    output : True
        If variable `value` **IS** of the `int` type;
    raises : TypeError
        If variable `value` is **NOT** of the `int` type;


    Notes
    -----
    The following types are considered to be `True`:

    * `int`;
    * `np.uint`;
    * `np.integer`;


    Examples
    --------
    >>> from paramcheckup import types
    >>> result = types.is_int(
        value=5,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=True,
    )
    >>> print(result)
    True


    >>> from paramcheckup import types
    >>> result = types.is_int(
        value=0.05,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The parameter `alpha` in function `ttest` must be of type `int`, but its type is `float`.

    """
    if isinstance(value, (int, np.uint, np.integer)) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `int`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotIntError")
            except TypeError:
                raise
    return True


@docs.docstring_parameter(
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_list_of_types(
    my_list, expected_type, param_name, kind, kind_name, stacklevel=4, error=True
):
    """This function checks whether all elements in the `list` `my_list` have the expected type of `expected_type`.


    Parameters
    ----------
    my_list :  list
        The `list` that the values are tested as being of `expected_type` type;
    expected_type : any
        The type that each element of the `list` `my_list` should be;
    {param_name}
        {param_name_desc} `my_list`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If all elements in `my_list` are of the type `expected_type`;
    raises : TypeError
        If at least one element in `my_list` **IS NOT** of type `expected_type`;

    Examples
    --------
    >>> from paramcheckup import types
    >>> result = types.is_list_of_types(
        my_list=["tukey", "dunnet", "fisher"],
        expected_type=str,
        param_name="comparison_test",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=True,
    )
    >>> print(result)
    True


    >>> from paramcheckup import types
    >>> result = types.is_list_of_types(
        my_list=[0.05, 0.10, 0.15, 0.20, 1],
        expected_type=float,
        param_name="alphas",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 4: At least one element of `alphas` in function `ttest` is not of type `float`.
    -  0.05 is `float`
    -  0.1 is `float`
    -  0.15 is `float`
    -  0.2 is `float`
    -  1 is `int` <------


    """
    if all(isinstance(item, expected_type) for item in my_list) is False:
        error_type = expected_type.__name__.capitalize()
        user_warning(
            f"At least one element of `{param_name}` in {kind} `{kind_name}` is not of type `{expected_type.__name__}`.",
            stacklevel=stacklevel,
        )
        for element in my_list:
            if not isinstance(element, expected_type):
                print("- ", element, "is", f"`{type(element).__name__}` <------")
            else:
                print("- ", element, "is", f"`{type(element).__name__}`")
        print("\n")
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError(f"Not{error_type}Error")
            except TypeError:
                raise
    return True


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_list(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `value` is of the `list` type.


    Parameters
    ----------
    {value}
        {value_desc} `list`;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If variable `value` **IS** of the `list` type;
    raises : TypeError
        If variable `value` is **NOT** of the `list` type;


    Examples
    --------
    >>> from paramcheckup import types
    >>> output = types.is_list(
        value=["0", "3/8", "1/2"],
        param_name="cte_alpha",
        kind="function",
        kind_name="critical_value",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import types
    >>> output = types.is_list(
        value=("0", "3/8", "1/2"),
        param_name="cte_alpha",
        kind="function",
        kind_name="critical_value",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 3: The parameter `cte_alpha` in function `critical_value` must be of type `list`, but its type is `tuple`.

    """
    if isinstance(value, list) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `list`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotListError")
            except TypeError:
                raise
    return True


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_numpy(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `value` is of the :doc:`numpy array <numpy:reference/generated/numpy.array>` type.


    Parameters
    ----------
    {value}
        {value_desc} :doc:`numpy array <numpy:reference/generated/numpy.array>` ;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If variable `value` **IS** of the :doc:`numpy array <numpy:reference/generated/numpy.array>` type;
    raises : TypeError
        If variable `value` is **NOT** of the :doc:`numpy array <numpy:reference/generated/numpy.array>` type;


    Examples
    --------
    >>> from paramcheckup import types
    >>> import numpy as np
    >>> output = types.is_numpy(
        value=np.array([1, 2, 3, 4, 5]),
        param_name="x_data",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import types
    >>> import numpy as np
    >>> output = types.is_numpy(
        value=[1, 2, 3, 4, 5],
        param_name="x_data",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 3: The parameter `x_data` in function `ttest` must be of type `numpy.ndarray`, but its type is `list`.


    """
    if isinstance(value, np.ndarray) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `numpy.ndarray`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotNumPyError")
            except TypeError:
                raise
    return True


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_str(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `value` is of the `str` type.


    Parameters
    ----------
    {value}
        {value_desc} `str` ;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If variable `value` **IS** of the `str` type;
    raises : TypeError
        If variable `value` is **NOT** of the `str` type;


    Examples
    --------
    >>> from paramcheckup import types
    >>> output = types.is_str(
        value="tukey",
        param_name="test",
        kind="function",
        kind_name="comparison_test",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import types
    >>> output = types.is_str(
        value=["tukey"],
        param_name="test",
        kind="function",
        kind_name="comparison_test",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The parameter `test` in function `comparison_test` must be of type `str`, but its type is `list`.

    """
    if isinstance(value, str) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `str`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotStrError")
            except TypeError:
                raise
    return True


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_subplots(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `value` is of the `matplotlib.axes.SubplotBase` type.

    Parameters
    ----------
    {value}
        {value_desc} `matplotlib.axes.SubplotBase` ;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If variable `value` **IS** of the `matplotlib.axes.SubplotBase` type;
    raises : TypeError
        If variable `value` is **NOT** of the `matplotlib.axes.SubplotBase` type;


    Examples
    --------
    >>> from paramcheckup import types
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> output = types.is_subplots(
        value=ax,
        param_name="axes",
        kind="function",
        kind_name="plot",
        stacklevel=3,
        error=True,
    )
    >>> plt.close()
    >>> print(output)
    True


    >>> from paramcheckup import types
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> output = types.is_subplots(
        value=fig,
        param_name="axes",
        kind="function",
        kind_name="plot",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 4: The parameter `axes` in function `plot` must be of type `matplotlib.axes.SubplotBase`, but its type is `Figure`.
    """
    if isinstance(value, SubplotBase) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `matplotlib.axes.SubplotBase`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotSubplotError")
            except TypeError:
                raise
    return True


@docs.docstring_parameter(
    value=docs.VALUE["type"],
    value_desc=docs.VALUE["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_tuple(value, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `value` is of the `tuple` type.


    Parameters
    ----------
    {value}
        {value_desc} `tuple` ;
    {param_name}
        {param_name_desc} `value`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If variable `value` **IS** of the `tuple` type;
    raises : TypeError
        If variable `value` is **NOT** of the `tuple` type;


    Examples
    --------
    >>> from paramcheckup import types
    >>> output = types.is_tuple(
        value=(0.345, 0.348, 0.401),
        param_name="critical",
        kind="function",
        kind_name="get_critical",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import types
    >>> output = types.is_tuple(
        value=[0.345, 0.348, 0.401],
        param_name="critical",
        kind="function",
        kind_name="get_critical",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The parameter `critical` in function `get_critical` must be of type `tuple`, but its type is `list`.

    """
    if isinstance(value, tuple) is False:
        user_warning(
            f"The parameter `{param_name}` in {kind} `{kind_name}` must be of type `tuple`, but its type is `{type(value).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotTupleError")
            except TypeError:
                raise
    return True
