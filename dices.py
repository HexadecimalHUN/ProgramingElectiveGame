import random

diceroll1  = random.randint(1, 7)
diceroll2 = random.randint(1, 7)
myrole = (diceroll1 + diceroll2)
while myrole != 7
    if myrole == 7:
        print("Your roll was a 7 you eaerned press enter to roll again:  ")
        break
    elif myrole != 0:
        print("Sorry you did not roll a 7 press enter to roll again: ")
        break
    elif mypot != 0:
        print("Sorry you do not have no more money in your pot")
        break