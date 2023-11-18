"""Evaluate simplification expressions."""
import collections.abc
import enum
import re
import string
import typing

import pydantic

from .calculator_sub_package import ArithmeticOperator, calculate_results


@enum.unique
class Parentheses(str, enum.Enum):
    """Define supported brackets."""

    LEFT = "("
    RIGHT = ")"


@enum.unique
class TokenType(str, enum.Enum):
    """Define supported token types."""

    POSITIVE_NUMBER = "positive_number"
    NEGATIVE_NUMBER = "negative_number"
    OPERATOR = "operator"
    LEFT_PARENTHESIS = "left_parenthesis"
    RIGHT_PARENTHESIS = "right_parenthesis"


SUPPORTED_CHARACTERS = set.union(
    set(string.digits + "."), set(ArithmeticOperator), set(Parentheses)
)
ACCEPTABLE_CHARACTERS = set(" ")

REGULAR_EXPRESSION_PATTERNS = {
    TokenType.POSITIVE_NUMBER: r"\d+(?:\.\d+)?",
    TokenType.NEGATIVE_NUMBER: rf"(?<![\d|{Parentheses.RIGHT.value}])-\d+(?:\.\d+)?",
    TokenType.OPERATOR: (
        "[" + "".join(rf"\{operator.value}" for operator in ArithmeticOperator) + "]"
    ),
    TokenType.LEFT_PARENTHESIS: rf"\{Parentheses.LEFT.value}",
    TokenType.RIGHT_PARENTHESIS: rf"\{Parentheses.RIGHT.value}",
}
SUPPORTED_TOKEN_PATTERN = "|".join(
    f"(?P<{token_type.value}>{token_pattern})"
    for token_type, token_pattern in REGULAR_EXPRESSION_PATTERNS.items()
)

OPERATION_PRECEDENCES: dict[ArithmeticOperator | Parentheses, int] = {
    Parentheses.LEFT: 0,
    Parentheses.RIGHT: 0,
    ArithmeticOperator.ADDITION: 1,
    ArithmeticOperator.SUBTRACTION: 1,
    ArithmeticOperator.MULTIPLICATION: 2,
    ArithmeticOperator.DIVISION: 2,
}


@pydantic.validate_call(validate_return=True)
def clean_and_tokenise_expression(
    raw_expression: str,
) -> pydantic.InstanceOf[collections.abc.Iterator[re.Match[str]]]:
    """Extract tokens from arithmetic expression after pre-processing.

    Parameters
    ----------
    raw_expression : str
        infix expression

    Returns
    -------
    collections.abc.Iterator[re.Match[str]]
        tokens in standard arithmetic expression

    Raises
    ------
    ValueError
        if unsupported characters are passed
    """
    clean_expression = raw_expression.translate(
        str.maketrans(dict.fromkeys(ACCEPTABLE_CHARACTERS, None))
    )

    if unsupported_characters := set(clean_expression).difference(SUPPORTED_CHARACTERS):
        raise ValueError(f"Unexpected characters: {unsupported_characters}")

    tokens = re.finditer(SUPPORTED_TOKEN_PATTERN, clean_expression)

    return tokens


@pydantic.validate_call(validate_return=True)
def convert_infix_expression(  # noqa: C901 # skipcq: PY-R1000
    infix_expression_tokens: pydantic.InstanceOf[collections.abc.Iterator[re.Match[str]]],
) -> list[ArithmeticOperator | float]:
    """Convert standard arithmetic expression into reverse Polish notation.

    This implements shunting yard algorithm following pseudocode section in Wikipedia.

    Parameters
    ----------
    infix_expression_tokens : collections.abc.Iterator[re.Match[str]]
        tokens in standard arithmetic expression

    Returns
    -------
    list[ArithmeticOperator | float]
        postfix arithmetic expression

    Raises
    ------
    ValueError
        if brackets are not matching

    Notes
    -----
    #. Initiate operator stack and output queue.
    #. Modify based on token type.

        * Number

            #. Convert to number (using ``float``).
            #. Add to ``output_queue``.

        * Operator

            #. Convert to operator (using ``ArithmeticOperator``).
            #. Move top lower precedence operators from ``operator_stack`` into ``output_queue``.
            #. Add to ``operator_stack``.

        * Left Parenthesis

            #. Convert to bracket (using ``Parentheses``).

        * Right Parenthesis

            #. Convert to bracket (using ``Parentheses``).
            #. Move operators from ``operator_stack`` into ``output_queue`` till left bracket.
            #. Discard left bracket from top of ``operator_stack``.

    References
    ----------
    `Wikipedia <https://en.wikipedia.org/wiki/Shunting_yard_algorithm#The_algorithm_in_detail>`_.
    """
    operator_stack: list[ArithmeticOperator | typing.Literal[Parentheses.LEFT]] = []
    output_queue: list[ArithmeticOperator | float] = []

    @pydantic.validate_call
    def __process_number_token(number_token: str) -> None:
        """Modify ``output_queue``.

        Parameters
        ----------
        number_token : str
            a real number as a string

        Notes
        -----
        #. Convert to number.
        #. Add to ``output_queue``.
        """
        valid_number = float(number_token)

        output_queue.append(valid_number)

    @pydantic.validate_call
    def __process_operator_token(operator_token: str) -> None:
        """Modify ``operator_stack`` and ``output_queue``.

        Parameters
        ----------
        operator_token : str
            a binary operator as a string

        Notes
        -----
        #. Convert to operator.
        #. Move previous lower precedence operators from ``operator_stack`` into ``output_queue``.
        #. Add to ``operator_stack``.
        """
        valid_operator = ArithmeticOperator(operator_token)

        while (
            operator_stack
            and (last_operator := operator_stack[-1]) != Parentheses.LEFT
            and OPERATION_PRECEDENCES[last_operator] >= OPERATION_PRECEDENCES[valid_operator]
        ):
            _ = operator_stack.pop()
            output_queue.append(last_operator)

        operator_stack.append(valid_operator)

    @pydantic.validate_call
    def __process_left_parenthesis_token(parenthesis_token: str) -> None:
        """Modify ``operator_stack``.

        Parameters
        ----------
        parenthesis_token : str
            left bracket as a string

        Raises
        ------
        ValueError
            if token is not left bracket

        Notes
        -----
        #. Convert to bracket.
        #. Add to ``operator_stack``.
        """
        valid_parenthesis = Parentheses(parenthesis_token)

        if valid_parenthesis != Parentheses.LEFT:
            raise ValueError(f"Unexpected token: {parenthesis_token}")  # pragma: no cover

        operator_stack.append(valid_parenthesis)

    @pydantic.validate_call
    def __process_right_parenthesis_token(parenthesis_token: str) -> None:
        """Modify ``operator_stack`` and ``output_queue``.

        Parameters
        ----------
        parenthesis_token : str
            right bracket as a string

        Raises
        ------
        ValueError
            if token is not right bracket
        ValueError
            if brackets are not matching

        Notes
        -----
        #. Convert to bracket.
        #. Move operators from ``operator_stack`` into ``output_queue`` till left bracket.
        #. Discard left bracket from top of ``operator_stack``.
        """
        valid_parenthesis = Parentheses(parenthesis_token)

        if valid_parenthesis != Parentheses.RIGHT:
            raise ValueError(f"Unexpected token: {parenthesis_token}")  # pragma: no cover

        while operator_stack and (last_operator := operator_stack[-1]) != Parentheses.LEFT:
            _ = operator_stack.pop()
            output_queue.append(last_operator)

        if not operator_stack or (last_operator := operator_stack[-1]) != Parentheses.LEFT:
            raise ValueError("Mismatched right parenthesis")

        _ = operator_stack.pop()

    for token in infix_expression_tokens:
        try:
            token_type, token_value = next(
                (element_type, element_value)
                for element_type, element_value in token.groupdict().items()
                if element_value is not None
            )
        except StopIteration:  # pragma: no cover
            continue

        match token_type:
            case TokenType.POSITIVE_NUMBER | TokenType.NEGATIVE_NUMBER:
                __process_number_token(token_value)
            case TokenType.OPERATOR:
                __process_operator_token(token_value)
            case TokenType.LEFT_PARENTHESIS:
                __process_left_parenthesis_token(token_value)
            case TokenType.RIGHT_PARENTHESIS:
                __process_right_parenthesis_token(token_value)

    while operator_stack:
        if (last_operator := operator_stack[-1]) == Parentheses.LEFT:
            raise ValueError("Mismatched left parenthesis")

        _ = operator_stack.pop()
        output_queue.append(last_operator)

    return output_queue


@pydantic.validate_call(validate_return=True)
def evaluate_postfix_expression(postfix_expression: list[ArithmeticOperator | float]) -> float:
    """Evaluate postfix arithmetic expression in reverse Polish notation.

    Parameters
    ----------
    postfix_expression : list[ArithmeticOperator | float]
        elements of arithmetic expression in postfix format

    Returns
    -------
    float
        result of arithmetic expression
    """
    stack: list[float] = []
    for element in postfix_expression:
        if isinstance(element, float | int):
            stack.append(element)
        else:
            operator = ArithmeticOperator(element)

            second_input = stack.pop()
            first_input = stack.pop()

            result = calculate_results(first_input, operator, second_input)
            stack.append(result)

    return stack.pop()


@pydantic.validate_call(validate_return=True)
def solve_simplification(expression: str) -> float:
    """Evaluate arithmetic expression.

    Parameters
    ----------
    expression : str
        standard arithmetic expression

    Returns
    -------
    float
        result of arithmetic expression

    Examples
    --------
    .. code-block:: pycon

        >>> from package_name_to_import_with import solve_simplification
        >>> solve_simplification("0 + 1 - 2 * 3 / 4")
        -0.5
        >>> solve_simplification("5 * 6 / (7 + 8) - 9")
        -7.0
    """
    raw_infix_tokens = clean_and_tokenise_expression(expression)
    ordered_postfix_tokens = convert_infix_expression(raw_infix_tokens)
    expression_value = evaluate_postfix_expression(ordered_postfix_tokens)

    return expression_value


__all__ = [
    "OPERATION_PRECEDENCES",
    "Parentheses",
    "clean_and_tokenise_expression",
    "convert_infix_expression",
    "evaluate_postfix_expression",
    "solve_simplification",
]
