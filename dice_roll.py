#python dice_roll.py

import random

def number_of_dice():
    return input("How many times do you want to roll?[1-6]: ")
frequency_input = number_of_dice()


def parse_input(frequency_input):
    """Return `frequency_input` as an integer between 1 and 6.

    Checks if `frequency_input` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if frequency_input.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(frequency_input)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)
frequency = parse_input(frequency_input)


def dice_roll(frequency):
    dices = []
    for i in range(frequency):
        dices.append(random.randint(1,6))
    return dices

dices = dice_roll(frequency)


"""Draw six dice faces using ASCII characters and store them in DICE_ART dictionary
DIE_HEIGHT - Holds number of rows a given face will occupy(5 rows)
DIE_WIDTH - Holds number of columns required to draw a die face(11 characters)
DIE_FACE_SEPARATOR - Holds a whitespace character"""
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
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def dice_faces_diagram():
    dice_faces = []
    for die in dices:
        dice_faces.append(DICE_ART[die])

    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


print(dice_faces_diagram())
