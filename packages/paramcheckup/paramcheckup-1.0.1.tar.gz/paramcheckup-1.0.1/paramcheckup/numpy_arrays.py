"""
##### List of functions (alphabetical order) #####

## Functions WITH TESTS ###

- empty_array(array, param_name, kind, kind_name, stacklevel=4, error=True)
- size_is_greater_than_lower(array, param_name, kind, kind_name, lower, inclusive=True, stacklevel=4, error=True)
- matching_size(arrays, param_names, kind, kind_name, stacklevel=4, error=True)
- n_dimensions(array, param_name, ndim, kind, kind_name, stacklevel=4, error=True)

## Functions WITH some TESTS (needs improvements) ###
- cast(array, param_name, kind, kind_name, ndim, stacklevel=4, error=True) (first error does not have a test)

## Functions WITHOUT tests ###



##### List of CLASS (alphabetical order) #####



Author: Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

Created: October 26, 2023.

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
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    ndim=docs.NDIM["type"],
    ndim_desc=docs.NDIM["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def cast(array, param_name, kind, kind_name, ndim, stacklevel=4, error=True):
    """This function attempts to transform an `array` into a ndim :doc:`numpy array <numpy:reference/generated/numpy.array>`.

    Parameters
    ----------
    array : list, tuple or pd.Series
        The variable that will be converted into a ndim :doc:`numpy array <numpy:reference/generated/numpy.array>`;
    {param_name}
        {param_name_desc} `array`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {ndim}
        {ndim_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}

    Returns
    -------
    array :  :doc:`numpy array <numpy:reference/generated/numpy.array>`
        One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>`;
    raises : ValueError
        If it was not possible to transform `array` into a :doc:`numpy array <numpy:reference/generated/numpy.array>`;


    Examples
    --------
    >>> from paramcheckup import numpy_arrays
    >>> x_exp = [1, 2, 3, 4]
    >>> x_exp = numpy_arrays.cast(
        array=x_exp,
        param_name="x",
        kind="function",
        kind_name="ttest",
        ndim=1,
        stacklevel=3,
        error=True,
    )
    >>> print(x_exp)
    [1 2 3 4]


    >>> from paramcheckup import numpy_arrays
    >>> x_exp = [1, 2, 3, 4]
    >>> x_exp = numpy_arrays.cast(
        array=x_exp,
        param_name="x",
        kind="function",
        kind_name="ttest",
        ndim=2,
        stacklevel=3,
        error=False,
    )
    UserWarning at line 3: The array generated for `x` in function `ttest` contains `1` dimensions, but it should contain `2` dimensions.


    """
    array = np.asarray(array)
    if isinstance(array, np.ndarray) is False:
        user_warning(
            f"Unable to transform `{param_name}` in {kind} `{kind_name}` into a NumPyArray satisfactorily.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("CastingError")
            except ValueError:
                raise
    elif array.ndim != ndim:
        user_warning(
            f"The array generated for `{param_name}` in {kind} `{kind_name}` contains `{array.ndim}` dimensions, but it should contain `{ndim}` dimensions.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("CastingError")
            except ValueError:
                raise
    elif array.size == 0:
        user_warning(
            f"The array generated for `{param_name}` in {kind} `{kind_name}` is empty. \n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("CastingError")
            except ValueError:
                raise
    else:
        return array


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
def empty_array(array, param_name, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a :doc:`numpy array <numpy:reference/generated/numpy.array>` is empty.

    Parameters
    ----------
    array : :doc:`numpy array <numpy:reference/generated/numpy.array>`
        The :doc:`numpy array <numpy:reference/generated/numpy.array>` to check for emptiness;
    {param_name}
        {param_name_desc} `array`;
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
        If the `array` is **NOT** empty;
    raises : ValueError
        If the `array` **IS** empty;


    Examples
    --------
    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> data = np.array([1, 2, 3, 4, 5])
    >>> output = numpy_arrays.empty_array(
        array=data,
        param_name="x_data",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> data = np.array([])
    >>> output = numpy_arrays.empty_array(
        array=data,
        param_name="x_data",
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 4: The `x_data` in function `ttest` cannot be an empty array.


    """
    if array.size == 0:
        user_warning(
            f"The `{param_name}` in {kind} `{kind_name}` cannot be an empty array.\n",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("EmptyArrayError")
            except ValueError:
                raise
    else:
        return True


@docs.docstring_parameter(
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    lower=docs.LOWER["type"],
    lower_desc=docs.LOWER["description"],
    inclusive=docs.INCLUSIVE["type"],
    inclusive_desc=docs.INCLUSIVE["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def size_is_greater_than_lower(
    array,
    param_name,
    kind,
    kind_name,
    lower,
    inclusive=True,
    stacklevel=4,
    error=True,
):
    """This function checks if the size of the :doc:`numpy array <numpy:reference/generated/numpy.array>` `array` is greater;equal than `lower`.


    Parameters
    ----------
    array :  :doc:`numpy array <numpy:reference/generated/numpy.array>`
        One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>`;
    {param_name}
        {param_name_desc} `array`;
    {kind}
        {kind_desc}
    {kind_name}
        {kind_name_desc}
    {lower}
        {lower_desc}
    {inclusive}
        {inclusive_desc}
    {stacklevel}
        {stacklevel_desc}
    {error}
        {error_desc}


    Returns
    -------
    output : True
        If the size of the `array` **IS** greater than `lower` (or **IS** equal/greater than `lower`);
    raises : ValueError
        If the size of the `array` is **NOT** greater than `lower` (or is **NOT** equal/greater than `lower`);


    Examples
    --------
    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> x_exp = np.array([1, 1, 2, 4, 4, 2, 3])
    >>> output = numpy_arrays.size_is_greater_than_lower(
        array=x_exp,
        param_name="x_data",
        kind="function",
        kind_name="linear_regression",
        lower=3,
        inclusive=True,
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> x_exp = np.array([1, 2, 4])
    >>> output = numpy_arrays.size_is_greater_than_lower(
        array=x_exp,
        param_name="x_data",
        kind="function",
        kind_name="linear_regression",
        lower=3,
        inclusive=True,
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> x_exp = np.array([1, 2])
    >>> output = numpy_arrays.size_is_greater_than_lower(
        array=x_exp,
        param_name="x_data",
        kind="function",
        kind_name="linear_regression",
        lower=3,
        inclusive=True,
        stacklevel=3,
        error=False,
    )
    UserWarning at line 4: The size of the array `x_data` in function `linear_regression` must be equal or greater than `3` (`x_data.size >= 3`), but it is `2`.


    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> x_exp = np.array([1, 2, 4])
    >>> output = numpy_arrays.size_is_greater_than_lower(
        array=x_exp,
        param_name="x_data",
        kind="function",
        kind_name="linear_regression",
        lower=3,
        inclusive=False,
        stacklevel=3,
        error=False,
    )
    UserWarning at line 4: The size of the array `x_data` in function `linear_regression` must be greater than `3` (`x_data.size > 3`), but it is `3`.

    """
    if inclusive:
        if array.size < lower:
            user_warning(
                f"The size of the array `{param_name}` in {kind} `{kind_name}` must be equal or greater than `{lower}` (`{param_name}.size >= {lower}`), but it is `{array.size}`.",
                stacklevel=stacklevel,
            )
            if error is False:
                sys.exit(1)
            else:
                try:
                    raise ValueError("SmallSizeError")
                except ValueError:
                    raise
    else:
        if array.size <= lower:
            user_warning(
                f"The size of the array `{param_name}` in {kind} `{kind_name}` must be greater than `{lower}` (`{param_name}.size > {lower}`), but it is `{array.size}`.",
                stacklevel=stacklevel,
            )
            if error is False:
                sys.exit(1)
            else:
                try:
                    raise ValueError("SmallSizeError")
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
    lower=docs.LOWER["type"],
    lower_desc=docs.LOWER["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def matching_size(
    arrays,
    param_names,
    kind,
    kind_name,
    stacklevel=4,
    error=True,
):
    """This function checks if the size of multiple arrays are equal;

    Parameters
    ----------
    arrays :  list of one dimension :doc:`numpy array <numpy:reference/generated/numpy.array>`;
        A `list` of one dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` that must have the same size;
    param_names : list of str
        A `list` with the name of each parameter that received the arrays contained in `arrays`
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
        If the size of all arrays are the same;
    ValueError
        If at least one array has a different size than the others;

    Examples
    --------
    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> x_data = np.array([1, 2, 3, 4, 5, 6])
    >>> z_data = np.array([1, 4, 9, 16, 25, 36])
    >>> output = numpy_arrays.matching_size(
        arrays=[x_data, z_data],
        param_names=["concentration", "absorbance"],
        kind="function",
        kind_name="calibration",
        stacklevel=3,
        error=False,
    )
    >>> print(output)
    True


    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> x_data = np.array([1, 2, 3, 4, 5, 6])
    >>> y_data = np.array([1, 4, 9, 16, 25,])
    >>> z_data = np.array([1, 4, 9, 16, 25, 36])
    >>> output = numpy_arrays.matching_size(
        arrays=[x_data, y_data, z_data],
        param_names=["x_data", "y_data", "z_data"],
        kind="function",
        kind_name="Tukey",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 6: The arrays `x_data` and `y_data` and `z_data` in function `Tukey` must have the same size, but at least one of them has a different
    size than the others.
    -->  x_data = 6
    -->  y_data = 5
    -->  z_data = 6

    """
    sizes = []
    names = ""
    for i in range(len(arrays)):
        sizes.append(arrays[i].size)
        if i == len(arrays) - 1:
            names += "`" + param_names[i] + "`"
        else:
            names += "`" + param_names[i] + "` and "

    if len(set(sizes)) != 1:
        user_warning(
            f"The arrays {names} in {kind} `{kind_name}` must have the same size, but at least one of them has a different size than the others.",
            stacklevel=stacklevel,
        )
        for i in range(len(arrays)):
            print("--> ", param_names[i], "=", arrays[i].size)
        print("\n")
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("SizeMismatchError")
            except ValueError:
                raise

    else:
        return True


@docs.docstring_parameter(
    param_name=docs.PARAM_NAME["type"],
    param_name_desc=docs.PARAM_NAME["description"],
    ndim=docs.NDIM["type"],
    ndim_desc=docs.NDIM["description"],
    kind=docs.KIND["type"],
    kind_desc=docs.KIND["description"],
    kind_name=docs.KIND_NAME["type"],
    kind_name_desc=docs.KIND_NAME["description"],
    stacklevel=docs.STACKLEVEL["type"],
    stacklevel_desc=docs.STACKLEVEL["description"],
    error=docs.ERROR["type"],
    error_desc=docs.ERROR["description"],
)
def n_dimensions(array, param_name, ndim, kind, kind_name, stacklevel=4, error=True):
    """This function checks whether a :doc:`numpy array <numpy:reference/generated/numpy.array>` has *n_dimensions*.


    Parameters
    ----------
    array : :doc:`numpy array <numpy:reference/generated/numpy.array>`
        The :doc:`numpy array <numpy:reference/generated/numpy.array>` to check the dimensions;
    {param_name}
        {param_name_desc} in `arrays`;
    {ndim}
        {ndim_desc}
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
        If `array` **HAS** `ndim`;
    raises : ValueError
        If `array` **DOES NOT HAVE** `ndim`;


    Examples
    --------
    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> output = numpy_arrays.n_dimensions(
        array=np.array([1, 2, 3, 4, 5]),
        param_name="x_data",
        ndim=1,
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=True,
    )
    >>> print(output)
    True


    >>> from paramcheckup import numpy_arrays
    >>> import numpy as np
    >>> output = numpy_arrays.n_dimensions(
        array=np.array([1, 2, 3, 4, 5]),
        param_name="x_data",
        ndim=2,
        kind="function",
        kind_name="ttest",
        stacklevel=3,
        error=False,
    )
    UserWarning at line 3: The array `x_data` in function `ttest` must have `2` dimensions, but it has `ndim = 1'.


    """
    if array.ndim != ndim:
        user_warning(
            f"The array `{param_name}` in {kind} `{kind_name}` must have `{ndim}` dimensions, but it has `ndim = {array.ndim}'.",
            stacklevel=stacklevel,
        )
        if error is False:
            sys.exit(1)
        else:
            try:
                raise ValueError("DimensionMismatchError")
            except ValueError:
                raise
    return True
