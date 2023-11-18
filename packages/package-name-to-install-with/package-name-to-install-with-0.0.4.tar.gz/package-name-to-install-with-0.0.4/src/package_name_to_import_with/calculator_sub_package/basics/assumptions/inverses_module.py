"""Define additive and multiplicative identities and inverses."""
import enum

import pydantic


@enum.unique
class IdentityElements(float, enum.Enum):
    """Define assumed identity elements."""

    ADDITIVE_IDENTITY = 0
    MULTIPLICATIVE_IDENTITY = 1


@enum.unique
class InverseElements(float, enum.Enum):
    """Define supported inverse elements."""

    ADDITIVE_INVERSE = -1
    MULTIPLICATIVE_INVERSE = 1


@pydantic.validate_call(validate_return=True)
def get_negative(input_number: float) -> float:
    """Get additive inverse of a real number.

    Parameters
    ----------
    input_number : float
        value of number

    Returns
    -------
    float
        negative of ``input_number``

    Examples
    --------
    .. code-block:: pycon

        >>> from package_name_to_import_with.calculator_sub_package import get_negative
        >>> get_negative(1)
        -1.0
        >>> get_negative(-1)
        1.0
    """
    additive_inverse = InverseElements.ADDITIVE_INVERSE * input_number

    return additive_inverse


@pydantic.validate_call(validate_return=True)
def get_reciprocal(input_number: float) -> float:
    """Get multiplicative inverse of a real number.

    Parameters
    ----------
    input_number : float
        value of number

    Returns
    -------
    float
        reciprocal of ``input_number``

    Raises
    ------
    ValueError
        if ``input_number`` is additive identity, viz. zero

    Examples
    --------
    .. code-block:: pycon

        >>> from package_name_to_import_with.calculator_sub_package import get_reciprocal
        >>> get_reciprocal(2)
        0.5
        >>> get_reciprocal(0.5)
        2.0
    """
    try:
        multiplicative_inverse = InverseElements.MULTIPLICATIVE_INVERSE / input_number
    except ZeroDivisionError as error:
        raise ValueError("Multiplicative inverse is not defined for additive identity") from error

    return multiplicative_inverse


__all__ = ["IdentityElements", "InverseElements", "get_negative", "get_reciprocal"]
