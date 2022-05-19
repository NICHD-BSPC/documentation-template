"""
Module documentation goes here.

Can link to :func:`super_complex_operation`, :meth:`
"""


def super_complex_operation(x, raise_error=False):
    """
    Prints the first argument.

    Parameters
    ----------

    x : obj
        Any arbitrary object that can be printed.

    raise_error : bool
        Just an argument to make it easy to break this function to demonstrate
        doctests.
    """

    if raise_error:
        raise ValueError("See? This is is why we can't have nice things.")

    print(x)


class Demo(object):
    def __init__(self, setup):
        """
        Docstring of the class

        Parameters
        ----------

        setup : str
            Arbitrary string
        """
        pass

    def run(self):
        """
        Runs something.
        """
        pass
