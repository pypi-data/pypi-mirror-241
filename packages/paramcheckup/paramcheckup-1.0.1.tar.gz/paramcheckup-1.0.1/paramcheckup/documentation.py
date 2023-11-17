### FUNCTIONS ###


def docstring_parameter(*args, **kwargs):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*args, **kwargs)
        return obj

    return dec


### CONSTANTS ###

ERROR = {
    "type": "error : bool, optional",
    "description": "Whether to display error text (`True`, default) or not (`False`);",
}


INCLUSIVE = {
    "type": "inclusive : bool, optional",
    "description": "Specify whether the boundaries should be open (`False`) or closed (`True`, default);",
}


KIND = {
    "type": "kind : str",
    "description": "The object where `param_name` is applied (function, method, class, etc.);",
}


KIND_NAME = {"type": "kind_name : str", "description": "The name of the object `kind`;"}


LOWER = {
    "type": "lower : int or float",
    "description": "The lower bound;",
}

NDIM = {
    "type": "ndim : int, optional",
    "description": "The number of dimentions that `array` must have;",
}


NUMBER = {
    "type": "number : int or float",
    "description": "The number that needs to be checked;",
}


PARAM_NAME = {
    "type": "param_name : str",
    "description": "The name of the parameter that received the variable ",
}


STACKLEVEL = {
    "type": "stacklevel : int, optional",
    "description": "The stacking level (default is ``4``);",
}


UPPER = {
    "type": "upper : int or float",
    "description": "The upper bound;",
}


VALUE = {
    "type": "value : any type",
    "description": "The variable that is tested as being of type",
}


# PARAM = {
#     "type":
#     "description":
# }
