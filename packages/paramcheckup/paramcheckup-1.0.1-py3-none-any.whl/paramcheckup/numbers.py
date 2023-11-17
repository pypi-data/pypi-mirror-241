"""
##### List of functions (alphabetical order) #####

## Functions WITH TESTS ###
- is_between_a_and_b(number, lower, upper, param_name, kind, kind_name, inclusive=True, stacklevel=4, error=True,)
- is_float_or_int(number, param_name, kind, kind_name, stacklevel=4, error=True)
- is_greater_than(number, lower, param_name, kind, kind_name, inclusive=True, stacklevel=4, error=True)
- is_lower_than(number, upper, param_name, kind, kind_name, inclusive=True, stacklevel=4, error=True)
- is_negative(number, param_name, kind, kind_name, stacklevel=4, error=True)
- is_positive(number, param_name, kind, kind_name, stacklevel=4, error=True)


## Functions WITH some TESTS (needs improvements) ###


## Functions WITHOUT tests ###



##### List of CLASS (alphabetical order) #####



Author: Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

Created: October 24, 2023.

Last update: November 15, 2023



"""

##### IMPORTS #####

### Standard ###
import sys

### Third part ###
import numpy as np

### home made ###
from .utils import user_warning
from . import documentation as docs

##### CONSTANTS #####


##### CLASSES #####


##### FUNCTIONS #####
@docs.docstring_parameter(
    number=docs.NUMBER["type"],
    number_desc=docs.NUMBER["description"],
    lower=docs.LOWER["type"],
    lower_desc=docs.LOWER["description"],
    upper=docs.UPPER["type"],
    upper_desc=docs.UPPER["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    inclusive=docs.INCLUSIVE["type"],
    inclusive_desc=docs.INCLUSIVE["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_between_a_and_b(
    number,
    lower,
    upper,
    param_name,
    kind,
    kind_name,
    inclusive=True,
    stacklevel=4,
    error=True,
):
    """This function checks whether a number (`number`) is within the range (open or closed) `lower` and `upper`.

    Parameters
    ----------
    {number}
        {number_desc}
    {lower}
        {lower_desc}
    {upper}
        {upper_desc}
    {param_name}
        {param_name_desc} `number`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {inclusive}
        {inclusive_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Notes
    -----
    If `lower` is greater than `upper`, the function automatically inverts the values to make mathematical sense.


    Returns
    -------
    output : True
        If `number` **IN** `[a;b]` (or `(a;b)`) interval;
    raises : ValueError
        If `number` **NOT** in `[a;b]` (or `(a;b)`) interval;


    Examples
    --------

    Checking if the significance level is a number between 0 and 1:

    >>> from paramcheckup import numbers
    >>> output = numbers.is_between_a_and_b(
        number=0,
        lower=0,
        upper=1,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    >>> print(output)
    True


    In some cases the lower and upper limits must be opened. To disallow closed ranges, simply pass parameter `inclusive=False`:


    >>> from paramcheckup import numbers
    >>> output = numbers.is_between_a_and_b(
        number=0.0,
        lower=0,
        upper=1,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        inclusive=False,
        stacklevel=3,
        error=False,
    )
    UserWarning at line 3: The value of `alpha` in function `ttest` must be within the range of `0 < alpha < 1`, but it is `0`.


    Another example with an error being reported, but with `inclusive=True`:


    >>> from paramcheckup import numbers
    >>> output = numbers.is_between_a_and_b(
        number=-0.35,
        lower=0,
        upper=1,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 3: The value of `alpha` in function `ttest` must be within the range of `0 <= alpha <= 1`, but it is `-0.35`.


    """
    values = [lower, upper]
    lower = min(values)
    upper = max(values)

    if inclusive is True:
        if (lower <= number <= upper) is False:
            user_warning(
                f"The value of `{param_name}` in {kind} `{kind_name}` must be within the range of `{lower} <= {param_name} <= {upper}`, but it is `{number}`.\n",
                stacklevel=stacklevel,
            )
            if error is False:
                sys.exit(1)
            else:
                try:
                    raise ValueError("OutofBoundsError")
                except ValueError:
                    raise
    else:
        if (lower < number < upper) is False:
            user_warning(
                f"The value of `{param_name}` in {kind} `{kind_name}` must be within the range of `{lower} < {param_name} < {upper}`, but it is `{number}`.\n",
                stacklevel=stacklevel,
            )
            if error is False:
                sys.exit(1)
            else:
                try:
                    raise ValueError("OutofBoundsError")
                except ValueError:
                    print()
                    raise
    return True


@docs.docstring_parameter(
    number=docs.NUMBER["type"],
    number_desc=docs.NUMBER["description"],
    lower=docs.LOWER["type"],
    lower_desc=docs.LOWER["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    inclusive=docs.INCLUSIVE["type"],
    inclusive_desc=docs.INCLUSIVE["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_greater_than(
    number, lower, param_name, kind, kind_name, inclusive=True, stacklevel=4, error=True
):
    """This function checks if a `number` is equal (open or closed) or higher than `lower`.


    Parameters
    ----------
    {number}
        {number_desc}
    {lower}
        {lower_desc}
    {param_name}
        {param_name_desc} `number`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {inclusive}
        {inclusive_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If `number` **IS** greater than lower (or `number` **IS** equal/greater than `lower`);
    raises : ValueError
        If `number` is **NOT** greater than lower (or `number` is **NOT** equal/greater than `lower`);

    Examples
    --------
    >>> from paramcheckup import numbers
    >>> output = numbers.is_greater_than(
        number=0.05,
        lower=0,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        inclusive=True,
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import numbers
    >>> output = numbers.is_greater_than(
        number=0.00,
        lower=0,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        inclusive=False,
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The value of `alpha` in function `ttest` must be greater than `0` (`alpha > 0`), but it is `0.0`.


    >>> from paramcheckup import numbers
    >>> output = numbers.is_greater_than(
        number=-0.05,
        lower=0,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        inclusive=True,
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The value of `alpha` in function `ttest` must be equal or greater than `0` (`alpha >= 0`), but it is `-0.05`.


    """

    if inclusive:
        if number < lower:
            user_warning(
                f"The value of `{param_name}` in {kind} `{kind_name}` must be equal or greater than `{lower}` (`{param_name} >= {lower}`), but it is `{number}`.\n",
                stacklevel=stacklevel,
            )
            if error is False:
                sys.exit(1)
            else:
                try:
                    raise ValueError("OutofBoundsError")
                except ValueError:
                    raise
    else:
        if number <= lower:
            user_warning(
                f"The value of `{param_name}` in {kind} `{kind_name}` must be greater than `{lower}` (`{param_name} > {lower}`), but it is `{number}`.\n",
                stacklevel=stacklevel,
            )
            if error is False:
                sys.exit(1)
            else:
                try:
                    raise ValueError("OutofBoundsError")
                except ValueError:
                    raise
    return True


@docs.docstring_parameter(
    number=docs.NUMBER["type"],
    number_desc=docs.NUMBER["description"],
    upper=docs.UPPER["type"],
    upper_desc=docs.UPPER["description"],
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    inclusive=docs.INCLUSIVE["type"],
    inclusive_desc=docs.INCLUSIVE["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def is_lower_than(
    number,
    upper,
    param_name,
    kind,
    kind_name,
    inclusive=True,
    stacklevel=4,
    error=True,
):
    """This function checks if a `number` is equal (open or closed) or lower than `upper`.

    Parameters
    ----------
    {number}
        {number_desc}
    {upper}
        {upper_desc}
    {param_name}
        {param_name_desc} `number`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {inclusive}
        {inclusive_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If `numer` **IS** lower than `upper` (or `number` **IS** lower/equal than `upper`);
    raises : ValueError
        If `numer` is **NOT** lower than `upper` (or `number` is **NOT** lower/equal than `upper`);


    Examples
    --------

    >>> from paramcheckup import numbers
    >>> output = numbers.is_lower_than(
        number=0.05,
        upper=1,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        inclusive=True,
        stacklevel=3,
        error=False,
    )
    >>> print(output)
    True


    >>> from paramcheckup import numbers
    >>> output = numbers.is_lower_than(
        number=1,
        upper=1,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        inclusive=False,
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The value of `alpha` in function `ttest` must be lower than `1` (`alpha < 1`), but it is `1`.


    >>> from paramcheckup import numbers
    >>> output = numbers.is_lower_than(
        number=1.05,
        upper=1,
        param_name="alpha",
        kind="function",
        kind_name="ttest",
        inclusive=True,
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The value of `alpha` in function `ttest` must be equal or lower than `1` (`alpha <= 1`), but it is `1.05`.



    """
    if inclusive:
        if number > upper:
            user_warning(
                f"The value of `{param_name}` in {kind} `{kind_name}` must be equal or lower than `{upper}` (`{param_name} <= {upper}`), but it is `{number}`.\n",
                stacklevel=stacklevel,
            )
            if error is False:
                sys.exit(1)
            else:
                try:
                    raise ValueError("OutofBoundsError")
                except ValueError:
                    raise
    else:
        if number >= upper:
            user_warning(
                f"The value of `{param_name}` in {kind} `{kind_name}` must be lower than `{upper}` (`{param_name} < {upper}`), but it is `{number}`.\n",
                stacklevel=stacklevel,
            )
            if error is False:
                sys.exit(1)
            else:
                try:
                    raise ValueError("OutofBoundsError")
                except ValueError:
                    raise
    return True


@docs.docstring_parameter(
    number=docs.NUMBER["type"],
    number_desc=docs.NUMBER["description"],
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
def is_float_or_int(number, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a variable `value` is of the `int` or `float` type.


    Parameters
    ----------
    {number}
        {number_desc}
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
    Output : True
        If variable `number` **IS** of the `int` or `float` type;
    raises : TypeError
        If variable `number` is **NOT** of the `int` or `float` type;


    Notes
    -----
    The following types are considered to be `True`:

    * `int`;
    * `float`;
    * `np.floating`;
    * `np.integer`;
    * `np.uint`;


    Examples
    --------

    >>> from paramcheckup import numbers
    >>> result = numbers.is_float_or_int(
        number=2,
        param_name="hypotenuse",
        kind="function",
        kind_name="pitagoras",
        stacklevel=3,
        error=True,
    )
    >>>  print(result)
    True


    >>> from paramcheckup import numbers
    >>> result = numbers.is_float_or_int(
        number="2",
        param_name="hypotenuse",
        kind="function",
        kind_name="pitagoras",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The `hypotenuse` in function `pitagoras` must be of type `int` or `float`, but its type is `str`.


    """
    if isinstance(number, (int, np.uint, np.integer, float, np.floating)) is False:
        user_warning(
            f"The `{param_name}` in {kind} `{kind_name}` must be of type `int` or `float`, but its type is `{type(number).__name__}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise TypeError("NotNumberError")
            except TypeError:
                raise
    else:
        return True


@docs.docstring_parameter(
    number=docs.NUMBER["type"],
    number_desc=docs.NUMBER["description"],
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
def is_negative(number, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether `number` is a negative number (lower than zero, not included).

    Parameters
    ----------
    {number}
        {number_desc}
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
        If `number` **IS** negative;
    ValueError
        If `number` is **NOT** negative;

    Examples
    --------
    >>> from paramcheckup import numbers
    >>> result = numbers.is_negative(
        number=-10,
        param_name="hypotenuse",
        kind="function",
        kind_name="pitagoras",
        stacklevel=3,
        error=True,
    )
    >>> print(result)
    True


    >>> from paramcheckup import numbers
    >>> result = numbers.is_negative(
        number=0,
        param_name="hypotenuse",
        kind="function",
        kind_name="pitagoras",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The `hypotenuse` in function `pitagoras` must be a negative number, but it is equal to `0`.


    >>> from paramcheckup import numbers
    >>> result = numbers.is_negative(
        number=3.1416,
        param_name="hypotenuse",
        kind="function",
        kind_name="pitagoras",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The `hypotenuse` in function `pitagoras` must be a negative number, but it is equal to `3.1416`.


    """
    if number >= 0:
        user_warning(
            f"The `{param_name}` in {kind} `{kind_name}` must be a negative number, but it is equal to `{number}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("NotNegativeError")
            except ValueError:
                raise
    return True


@docs.docstring_parameter(
    number=docs.NUMBER["type"],
    number_desc=docs.NUMBER["description"],
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
def is_positive(number, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether `number` is a positive number (lower than zero, not included).

    Parameters
    ----------
    {number}
        {number_desc}
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
    True
        If variable *value* **IS** positive;
    ValueError
        If variable *value* is **NOT** positive;

    Examples
    --------
    >>> from paramcheckup import numbers
    >>> result = numbers.is_positive(
        number=3.1416,
        param_name="hypotenuse",
        kind="function",
        kind_name="pitagoras",
        stacklevel=3,
        error=False,
    )
    >>> print(result)
    True


    >>> from paramcheckup import numbers
    >>> result = numbers.is_positive(
        number=0,
        param_name="hypotenuse",
        kind="function",
        kind_name="pitagoras",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The `hypotenuse` in function `pitagoras` must be a positive number, but it is equal to `0`.


    >>> from paramcheckup import numbers
    >>> result = numbers.is_positive(
        number=-273.15,
        param_name="hypotenuse",
        kind="function",
        kind_name="pitagoras",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 2: The `hypotenuse` in function `pitagoras` must be a positive number, but it is equal to `-273.15`.


    """
    if number <= 0:
        user_warning(
            f"The `{param_name}` in {kind} `{kind_name}` must be a positive number, but it is equal to `{number}`.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("NotPositiveError")
            except ValueError:
                raise
    return True
