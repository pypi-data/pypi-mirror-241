"""Exceptions for the LRC Core package.
"""

from typing import Union

class LrcException(Exception):
    """
    Custom exception class for LRC-related errors.

    Args:
        message_or_exception (Union[str, Exception]): The error message or the original exception.
        html_code (int, optional): The HTTP status code to return in the response.

    Attributes:
        type (type): The type of the original exception, if any.
        html_code (int): The HTTP status code to return in the response.

    Methods:
        __repr__(): Returns a string representation of the exception.
        __str__(): Returns a string representation of the exception.
    """

    def __init__(self, message_or_exception: Union[str, Exception], html_code: int = None):
        if isinstance(message_or_exception, str):
            super().__init__(message_or_exception)
            self.type = None
        else:
            super().__init__(str(message_or_exception))
            self.type = type(message_or_exception)
        self.html_code = html_code

    def __repr__(self):
        if self.type is None:
            msg = f"LRC Exception: \"{', '.join(super().args)}\""
        else:
            msg = f"LRC Exception: (original Exception: {self.type}) \"{', '.join(super().args)}\""
        if self.html_code is not None:
            msg += f" (HTML Code: {self.html_code})"
        return msg

    def __str__(self):
        return self.__repr__()


def exception_decorator(*exceptions):
    """
    A decorator that catches specified exceptions and raises them as LrcExceptions.

    Args:
        *exceptions: A variable-length argument list of exceptions to catch.

    Returns:
        A decorator function that can be applied to other functions.

    Example:
        @exception_decorator(ValueError, TypeError)
        def my_function():
            # code here
    """
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                ret = func(*args, **kwargs)
                return ret
            except exceptions as e:
                raise LrcException(e) from e

        return new_func

    return decorator
