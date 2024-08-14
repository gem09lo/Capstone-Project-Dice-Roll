#python dice_roll.py

import random

def number_of_dice():
    return input("How many times do you want to roll?[1-6]: ")
frequency_input = number_of_dice()


def parse_input(frequency_input):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
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

print(dice_roll(frequency))
