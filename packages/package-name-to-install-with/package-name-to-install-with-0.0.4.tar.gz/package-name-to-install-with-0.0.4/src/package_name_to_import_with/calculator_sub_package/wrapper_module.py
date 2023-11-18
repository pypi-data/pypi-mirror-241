"""Define function for basic binary operations."""
import collections.abc
import enum
import typing

import pydantic

from .basics import add_numbers, divide_numbers, multiply_numbers, subtract_numbers

ArithmeticOperation: typing.TypeAlias = collections.abc.Callable[[float, float], float]


@enum.unique
class ArithmeticOperator(str, enum.Enum):
    """Define supported arithmetic operators."""

    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"


ARITHMETIC_OPERATIONS: dict[ArithmeticOperator, ArithmeticOperation] = {
    ArithmeticOperator.ADDITION: add_numbers,
    ArithmeticOperator.SUBTRACTION: subtract_numbers,
    ArithmeticOperator.MULTIPLICATION: multiply_numbers,
    ArithmeticOperator.DIVISION: divide_numbers,
}


class ArithmeticExpression(pydantic.BaseModel):
    """Define arithmetic expression.

    Parameters
    ----------
    first_number : float
        value of first number
    operator : ArithmeticOperator
        value of arithmetic operator
    second_number : float
        value of second number
    """

    first_number: float
    operator: ArithmeticOperator
    second_number: float

    @property
    def operation(self: "ArithmeticExpression") -> ArithmeticOperation:
        """Store arithmetic operation.

        Returns
        -------
        ArithmeticOperation
            function to perform arithmetic operation corresponding to ``self.operator``
        """
        return ARITHMETIC_OPERATIONS[self.operator]

    @property
    def result(self: "ArithmeticExpression") -> float:
        """Store result of arithmetic expression.

        Returns
        -------
        float
            result of arithmetic expression
        """
        return self.operation(self.first_number, self.second_number)


@pydantic.validate_call(validate_return=True)
def calculate_results(
    first_input: float, operator: ArithmeticOperator, second_input: float
) -> float:
    """Perform basic arithmetic expressions.

    Parameters
    ----------
    first_input : float
        value of first number
    operator : ArithmeticOperator
        type of arithmetic expression
    second_input : float
        value of second number

    Returns
    -------
    float
        result of arithmetic expression

    Examples
    --------
    .. code-block:: pycon

        >>> from package_name_to_import_with import calculate_results
        >>> calculate_results(1, "+", 2)
        3.0
        >>> calculate_results(1, "-", 2)
        -1.0
        >>> calculate_results(1, "*", 2)
        2.0
        >>> calculate_results(1, "/", 2)
        0.5
    """
    arithmetic_expression = ArithmeticExpression(
        first_number=first_input, operator=operator, second_number=second_input
    )

    return arithmetic_expression.result


__all__ = [
    "ARITHMETIC_OPERATIONS",
    "ArithmeticExpression",
    "ArithmeticOperation",
    "ArithmeticOperator",
    "calculate_results",
]
