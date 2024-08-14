#python dice_roll.py

import random

def number_of_dice():
    return int(input("How many times do you want to roll?[1-6]: "))

frequency = number_of_dice()


def dice_roll(frequency):
    dices = []
    for i in range(frequency):
        dices.append(random.randint(1,6))
    return dices

print(dice_roll(frequency))
