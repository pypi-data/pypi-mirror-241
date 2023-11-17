"""

##### List of functions (alphabetical order) #####

## Functions WITH TESTS ###

- is_empty(data_frame, param_name, kind, kind_name, stacklevel=4, error=True)
- column_name(column_name, data_frame, param_name, kind, kind_name, stacklevel=4, error=True)


## Functions WITH some TESTS (needs improvements) ###


## Functions WITHOUT tests ###



##### List of CLASS (alphabetical order) #####

Author: Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

Created: October 27, 2023.

Last update: November 15, 2023



"""

##### IMPORTS #####

### Standard ###
import sys

### Third part ###

### home made ###
from .utils import user_warning
from . import documentation as docs

##### CONSTANTS #####


##### CLASSES #####


##### FUNCTIONS #####
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
def column_name(
    column_name, data_frame, param_name, kind, kind_name, stacklevel=4, error=True
):
    """This function checks whether the *str* *column_name* is a valid column name for the :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` *dataframe*.

    Parameters
    ----------
    column_name : str
        The name of the column to be checked;
    data_frame : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
        The :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` that should contain the column named `column_name`;
    {param_name}
        {param_name_desc}  `data_frame`;
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
        If `column_name` **IS** a valid column name for the `data_frame`;
    raises : ValueError
        If `column_name` is **NOT** a valid column name for the `data_frame`;

    Examples
    --------
    >>> import pandas as pd
    >>> from paramcheckup import data_frames
    >>> data = [["Anderson", 33], ["Juliana", 31], ["Marcos", 26], ["Mariana", 30]]
    >>> columns = ["Name", "Age"]
    >>> df = pd.DataFrame(
        data=data,
        columns=columns,
    )
    >>> output = data_frames.column_name(
        column_name="Name",
        data_frame=df,
        param_name="data_frame",
        kind="function",
        kind_name="database",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> import pandas as pd
    >>> from paramcheckup import data_frames
    >>> data = [["Anderson", 33], ["Juliana", 31], ["Marcos", 26], ["Mariana", 30]]
    >>> columns = ["Name", "Age"]
    >>> df = pd.DataFrame(
        data=data,
        columns=columns,
    )
    >>> output = data_frames.column_name(
        column_name="Gender",
        data_frame=df,
        param_name="data_frame",
        kind="function",
        kind_name="database",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 10: The `data_frame` in function `database` does not contain a column with the name `Gender`.


    """

    if column_name not in data_frame.columns:
        user_warning(
            f"The `{param_name}` in {kind} `{kind_name}` does not contain a column with the name `{column_name}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("ColumnNameError")
            except ValueError:
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
def is_empty(data_frame, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether the `data_frame` is an empty :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`

    Parameters
    ----------
    data_frame : :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`
        The :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>` to be checked for emptiness;
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
        If variable `data_frame` is **NOT** an empty :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`;
    raises : ValueError
        If variable `data_frame` **IS** an empty :doc:`DataFrame <pandas:reference/api/pandas.DataFrame>`;


    Examples
    --------
    >>> import pandas as pd
    >>> from paramcheckup import data_frames
    >>> data = [["Anderson", 33], ["Juliana", 31], ["Marcos", 26], ["Mariana", 30]]
    >>> columns = ["Name", "Age"]
    >>> df = pd.DataFrame(
        data=data,
        columns=columns,
    )
    >>> output = data_frames.is_empty(
        data_frame=df,
        param_name="data_frame",
        kind="function",
        kind_name="database",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> import pandas as pd
    >>> from paramcheckup import data_frames
    >>> data = []
    >>> columns = ["Name", "Age"]
    >>> df = pd.DataFrame(
        data=data,
        columns=columns,
    )
    >>> output = data_frames.is_empty(
        data_frame=df,
        param_name="data_frame",
        kind="function",
        kind_name="database",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 10: The `data_frame` in function `database` is an EMPTY DataFrame.

    """

    if data_frame.empty:
        user_warning(
            f"The `{param_name}` in {kind} `{kind_name}` is an EMPTY DataFrame.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("EmptyDataFrameError")
            except ValueError:
                raise
    return True
