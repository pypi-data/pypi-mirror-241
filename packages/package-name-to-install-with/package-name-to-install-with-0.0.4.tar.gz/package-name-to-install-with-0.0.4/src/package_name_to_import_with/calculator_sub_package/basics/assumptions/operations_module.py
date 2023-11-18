"""Define functions to add and multiply."""
import pydantic


@pydantic.validate_call(validate_return=True)
def add_numbers(first_number: float, second_number: float) -> float:
    """Perform addition of two real numbers.

    Parameters
    ----------
    first_number : float
        value of first number
    second_number : float
        value of second number

    Returns
    -------
    float
        sum of ``first_number`` and ``second_number``

    Examples
    --------
    .. code-block:: pycon

        >>> from package_name_to_import_with.calculator_sub_package import add_numbers
        >>> add_numbers(1, 2)
        3.0
        >>> add_numbers(1, -2)
        -1.0
        >>> add_numbers(-1, 2)
        1.0
        >>> add_numbers(-1, -2)
        -3.0
    """
    sum_of_two_numbers = first_number + second_number

    return sum_of_two_numbers


@pydantic.validate_call(validate_return=True)
def multiply_numbers(first_number: float, second_number: float) -> float:
    """Perform multiplication of two real numbers.

    Parameters
    ----------
    first_number : float
        value of first number
    second_number : float
        value of second number

    Returns
    -------
    float
        product of two ``first_number`` and ``second_number``

    Examples
    --------
    .. code-block:: pycon

        >>> from package_name_to_import_with.calculator_sub_package import multiply_numbers
        >>> multiply_numbers(1, 2)
        2.0
        >>> multiply_numbers(1, -2)
        -2.0
        >>> multiply_numbers(-1, 2)
        -2.0
        >>> multiply_numbers(-1, -2)
        2.0
    """
    product_of_two_numbers = first_number * second_number

    return product_of_two_numbers


__all__ = ["add_numbers", "multiply_numbers"]
