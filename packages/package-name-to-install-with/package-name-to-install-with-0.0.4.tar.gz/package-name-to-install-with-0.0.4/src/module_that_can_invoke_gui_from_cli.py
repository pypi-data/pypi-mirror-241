"""Calculate arithmetic expressions from GUI."""
import pydantic
import PySimpleGUI

import package_name_to_import_with

FIRST_NUMBER_INPUT = "first_number"
SECOND_NUMBER_INPUT = "second_number"
OPERATOR_INPUT = "operator"
OPERATION_RESULT = "result"
CLOSE_BUTTON = "Close"


@pydantic.validate_call(validate_return=True)
def define_gui_layout() -> list[list[pydantic.InstanceOf[PySimpleGUI.Element]]]:
    """Prepare design of the GUI.

    Returns
    -------
    list[list[PySimpleGUI.Element]]
        elements of the GUI
    """
    layout = [
        [PySimpleGUI.Text("Enter first number"), PySimpleGUI.Input(key=FIRST_NUMBER_INPUT)],
        [
            PySimpleGUI.Text("Enter operator"),
            PySimpleGUI.OptionMenu(
                package_name_to_import_with.calculator_sub_package.ArithmeticOperator,
                key=OPERATOR_INPUT,
            ),
        ],
        [PySimpleGUI.Text("Enter second number"), PySimpleGUI.Input(key=SECOND_NUMBER_INPUT)],
        [PySimpleGUI.Button(button_text="Submit")],
        [PySimpleGUI.Text("Operation Result", key=OPERATION_RESULT)],
        [PySimpleGUI.Button(button_text=CLOSE_BUTTON)],
    ]

    return layout


@pydantic.validate_call(validate_return=True)
def define_gui_window(
    gui_layout: list[list[pydantic.InstanceOf[PySimpleGUI.Element]]],
) -> pydantic.InstanceOf[PySimpleGUI.Window]:
    """Create GUI with provided design.

    Parameters
    ----------
    gui_layout : list[list[PySimpleGUI.Element]]
        design of the GUI

    Returns
    -------
    PySimpleGUI.Window
        designed GUI
    """
    window = PySimpleGUI.Window("GUI Calculator", layout=gui_layout)

    return window


@pydantic.validate_call(validate_return=True)
def orchestrate_interaction(gui_window: pydantic.InstanceOf[PySimpleGUI.Window]) -> None:
    """Control flow of the GUI.

    Parameters
    ----------
    gui_window : PySimpleGUI.Window
        designed GUI
    """
    while True:
        gui_event, gui_elements = gui_window.read()  # pyright: ignore [reportGeneralTypeIssues]

        if PySimpleGUI.WINDOW_CLOSED or gui_event == CLOSE_BUTTON:
            break

        try:
            operation_result = package_name_to_import_with.calculate_results(
                gui_elements[FIRST_NUMBER_INPUT],
                gui_elements[OPERATOR_INPUT],
                gui_elements[SECOND_NUMBER_INPUT],
            )
        except Exception as error:  # noqa: BLE001  # pylint: disable=broad-except
            gui_window[OPERATION_RESULT].update(value=str(error))
        else:
            gui_window[OPERATION_RESULT].update(value=operation_result)


@pydantic.validate_call(validate_return=True)
def gui_calculator() -> None:
    """Calculate arithmetic expressions."""
    gui_layout = define_gui_layout()
    gui_window = define_gui_window(gui_layout)

    try:
        orchestrate_interaction(gui_window)
    finally:
        gui_window.close()


if __name__ == "__main__":
    gui_calculator()
