"""
##### List of functions (alphabetical order) #####

## Functions WITH TESTS ###
- param_options(option, options, param_name, kind, kind_name, stacklevel, error)


## Functions WITH some TESTS (needs improvements) ###


## Functions WITHOUT tests ###



##### List of CLASS (alphabetical order) #####


Author: Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

Created: October 28, 2023.

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
def param_options(option, options, param_name, kind, kind_name, stacklevel, error):
    """This function checks whether a `option` is a valid `options` for `param_name`.

    Parameters
    ----------
    option : any
        The parameter option to be evaluated;
    options : list
        A list with all the possible values for `param_name`;
    {param_name}
        {param_name_desc}
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
        If `option` **IS** in `options`;
    raises : ValueError
        If `option` is **NOT** in `options`;


    Examples
    --------
    >>> from paramcheckup import parameters
    >>> result = parameters.param_options(
        option="tukey",
        options=["tukey", "fisher", "dunett"],
        param_name="test",
        kind="function",
        kind_name="comparison_test",
        stacklevel=3,
        error=True,
    )
    >>> print(result)
    True


    >>> from paramcheckup import parameters
    >>> result = parameters.param_options(
        option="Student",
        options=["tukey", "fisher", "dunett"],
        param_name="test",
        kind="function",
        kind_name="comparison_test",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The `Student` is not a valid option for `test` in function `comparison_test`.
    Only the following options are accepted:
    --> tukey
    --> fisher
    --> dunett


    """
    if option not in options:
        user_warning(
            f"The `{option}` is not a valid option for `{param_name}` in {kind} `{kind_name}`.",
            stacklevel=stacklevel,
        )
        print("Only the following options are accepted:")
        for p_value in options:
            print(f"--> {p_value}")
        print("\n")
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("OptionNotFoundError")
            except ValueError:
                raise
    return True
