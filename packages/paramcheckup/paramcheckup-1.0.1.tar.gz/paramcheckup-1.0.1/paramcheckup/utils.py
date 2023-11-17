import warnings


def user_warning(text, stacklevel=4):
    def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
        # return "%s:%s: %s: %s\n" % (filename, lineno, category.__name__, message)
        # return "%s: %s: %s\n" % (lineno, category.__name__, message)
        return "%s at line %s: %s\n" % (category.__name__, lineno, message)

    warnings.formatwarning = warning_on_one_line

    warnings.warn(text, stacklevel=stacklevel)
