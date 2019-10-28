import random

succeeded_rolls = 0

while succeeded_rolls == 0:
    dice1 = random.randrange(1, 6, 1)
    dice2 = random.randrange(1, 6, 1)
    roll_dices = input("Would you like to roll the dices [y/Y]: ")
    print(dice1 + dice2)
    if dice1 + dice2 == 7:
        succeeded_rolls = 1
        print("You rolled a seven, you have completed the game")
    else:
        print("That's not a seven")

