"""
01/06/26 - cli.py
Command-Line utilities for the CS:GUI app's CLI menu
"""

import subprocess
from core.constants import Env
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def _(message: str) -> str: ...
    """Dev only - Stops IDE errors"""

class CLIUtils:
    
    
    @staticmethod
    def clear() -> None:
        """Clears the terminal screen based on the operating system."""
        subprocess.run(('cls' if Env.OS_NAME == 'Windows' else 'clear'), shell=True)


    @staticmethod
    def pause() -> None:
        """Pauses the script and waits for user input before continuing."""
        input(_("\nPress enter to continue..."))


    @staticmethod
    def get_sanitized_num_input(prompt: str,
                            target_type: type,
                            min_value: int | float| None = None,
                            max_value: int | float | None = None) -> int | float:
        """
        Prompts the user for a numeric input and safely handles invalid data.

        Args:
            prompt (str): The text displayed to the user.
            target_type (type): The expected Python type (usually `int` or `float`).
            min_value (int/float, optional): The minimum allowed boundary.
            max_value (int/float, optional): The maximum allowed boundary.

        Returns:
            The cleaned numeric input matching the target_type.
        """
        while True:
            unclean_input = input(prompt)
            try:
                clean_input = target_type(unclean_input)
                if min_value is not None and clean_input < min_value:
                    print(_("Error: Value cannot be below {min_value}.").format(min_value=min_value))
                    continue
                if max_value is not None and clean_input > max_value:
                    print(_("Error: Value cannot be above {max_value}.").format(max_value=max_value))
                    continue
                return clean_input
            except ValueError:
                if target_type is int:
                    print(_("Error: Invalid input. Please enter an integer."))
                else:
                    print(_("Error: Invalid input. Please enter a number."))


    @staticmethod
    def get_sanitized_str_input(prompt: str,
                                string_list: list[str] | None = None,
                                allow_anycase: bool = False,
                                should_strip: bool = True) -> str:
        """
        Prompts the user for string input, sanitizes it, and restricts choices if needed.

        Args:
            prompt (str): The text displayed to the user.
            string_list (list, optional): A list of valid exact string matches allowed.
            allow_anycase (bool): If True, adherence to the list is not affected by caps.
            should_strip (bool): If True, removes leading/trailing whitespace.

        Returns:
            str: The sanitized string input.
        """
        if string_list is not None and allow_anycase:
            string_list = [item.lower() for item in string_list]
        while True:
            string_input = input(prompt)
            if should_strip:
                string_input = string_input.strip()
            if allow_anycase:
                string_input = string_input.lower()
            if string_list is not None and string_input not in string_list:
                print(_("Error: You must enter one of these options: "))
                print(*string_list, sep = ', ')
                continue
            return string_input