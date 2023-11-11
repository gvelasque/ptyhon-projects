# dice.py

import random
import os


DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DICE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

MIN_DICE_VALUE = 1
MAX_DICE_VALUE = 6


def parse_input(input_string: str) -> int:
    """
    Check if the input is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, inform
    the user to enter a valid number and exit the program.

    Args:
        input_string (str): The input to be checked.

    Raises:
        SystemExit: Exits the app if the input is incorrect.

    Returns:
        int: An integer between 1 and 6.
    """
    try:
        parsed_input = int(input_string)
        if parsed_input in range(MIN_DICE_VALUE, MAX_DICE_VALUE + 1):
            return parsed_input
        else:
            raise ValueError("Please enter a number from 1 to 6.")
    except ValueError as e:
        raise ValueError("Please enter a valid integer.") from e


def roll_dice(num_dice: int) -> list:
    """Each integer in the returned list is a random number between
    1 and 6, inclusive.

    Args:
        num_dice (int): The number of dice to roll in a given call.

    Returns:
        list: Return list of random number between 1 and 6, inclusive.
    """
    roll_results = []
    for _ in range(num_dice):
        roll_results.append(random.randint(MIN_DICE_VALUE, MAX_DICE_VALUE))
    return roll_results


def generate_dice_faces_diagram(dice_values: list) -> str:
    """The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:

    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘

    Args:
        dice_values (list): Generate a list of dice faces from DICE_ART.

    Returns:
        str: Return an ASCII diagram of dice faces.
    """
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # Generate header with the word "RESULT" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")
    return "\n".join([diagram_header] + dice_faces_rows)


def _get_dice_faces(dice_values: list) -> list:
    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces


def _generate_dice_faces_rows(dice_faces: list) -> list:
    # Generate a list containig the dice face rows
    dices_face_rows = []
    for row_idx in range(DICE_HEIGHT):
        row_componets = []
        for die in dice_faces:
            row_componets.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_componets)
        dices_face_rows.append(row_string)
    return dices_face_rows


# ~~~ App's main code block ~~~
# Ger and validate user's input
while True:
    num_dice_input = input(
        "How many dice do you want to roll? Enter a number between 1 and 6: ")
    try:
        num_dice = parse_input(num_dice_input)
        break
    except ValueError as e:
        print(e)

# Roll the dice
roll_results = roll_dice(num_dice)
# Generate the ASCII diagram of die faces
dice_face_diagram = generate_dice_faces_diagram(roll_results)
# Display the diagram
print(f"\n{dice_face_diagram}")
