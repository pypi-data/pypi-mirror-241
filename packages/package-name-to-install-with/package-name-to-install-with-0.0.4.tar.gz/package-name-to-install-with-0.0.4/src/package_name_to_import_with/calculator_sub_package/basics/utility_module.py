"""Define functions to subtract and divide."""
import pydantic

from .assumptions import add_numbers, get_negative, get_reciprocal, multiply_numbers


@pydantic.validate_call(validate_return=True)
def subtract_numbers(first_number: float, second_number: float) -> float:
    """Perform subtraction of two real numbers.

    Parameters
    ----------
    first_number : float
        value of first number
    second_number : float
        value of second number

    Returns
    -------
    float
        difference of ``first_number`` from ``second_number``

    Examples
    --------
    .. code-block:: pycon

        >>> from package_name_to_import_with.calculator_sub_package import subtract_numbers
        >>> subtract_numbers(1, 2)
        -1.0
        >>> subtract_numbers(1, -2)
        3.0
        >>> subtract_numbers(-1, 2)
        -3.0
        >>> subtract_numbers(-1, -2)
        1.0
    """
    difference_of_two_numbers = add_numbers(first_number, get_negative(second_number))

    return difference_of_two_numbers


@pydantic.validate_call(validate_return=True)
def divide_numbers(first_number: float, second_number: float) -> float:
    """Perform division of two real numbers.

    Parameters
    ----------
    first_number : float
        value of first number
    second_number : float
        value of second number

    Returns
    -------
    float
        quotient of ``first_number`` by ``second_number``

    Examples
    --------
    .. code-block:: pycon

        >>> from package_name_to_import_with.calculator_sub_package import divide_numbers
        >>> divide_numbers(1, 2)
        0.5
        >>> divide_numbers(1, -2)
        -0.5
        >>> divide_numbers(-1, 2)
        -0.5
        >>> divide_numbers(-1, -2)
        0.5
    """
    quotient_of_two_numbers = multiply_numbers(first_number, get_reciprocal(second_number))

    return quotient_of_two_numbers


__all__ = ["divide_numbers", "subtract_numbers"]
