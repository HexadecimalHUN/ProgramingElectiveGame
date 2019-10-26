import random

hp = 2
def dice_game(hp):
    endgame = 0

    def roll_dice(endgame):
        pd1 = random.randrange(1, 6, 1)
        print ("Your first number is:", pd1)
        input("Press Enter to continue...")
        pd2 = random.randrange(1, 6, 1)
        print("Your second number is:", pd2)
        input("Press Enter to continue...")
        pd3 = random.randrange(1, 6, 1)
        print("Your third number is:", pd3)
        input("Press Enter to continue...")
        pdd = pd1 + pd2 + pd3

        bd1 = random.randrange(1, 6, 1)
        print("Your enemies first number is:", bd1)
        input("Press Enter to continue...")
        bd2 = random.randrange(1, 6, 1)
        print("Your enemies first number is:", bd2)
        input("Press Enter to continue...")
        bd3 = random.randrange(1, 6, 1)
        print("Your enemies first number is:", bd3)

        bdd = bd1 + bd2 + bd3

        if pdd > bdd:
            print("Ohh, lucky you!")
            endgame = 2
            return endgame

        if pdd < bdd:
            print("Nice, you lost the game!")
            endgame = 3
            return endgame

        if pdd == bdd:
            print("You god damn gangster, its a draw!-you said, but suddenly they raised a revolver to your had! I think we all understand the situation! ")
            endgame = 3
            return  endgame




    print("A few cheeky bastard come next to you. They asking you want to play dice with them? Of course you say yes!")
    print("But suddenly you dont know what is the bet? “Here we playing in lifepoints“-they said! ")
    print("How many lifepoints you want to play with?")
    lifep = int(input())
    if lifep >  hp:
        print("You dont have that much healthpoint")
        print("The bandits got annoyed about your altitude and left you!")
        endgame = 1
        return endgame
    elif lifep <= hp:
        endgame=roll_dice(endgame)

        if endgame == 2:
            hp = 2 + lifep
            print("Your new hp is:",hp)
        elif endgame == 3:
            hp = hp -lifep
            if hp <= 0:
                exit("You lost the game!")

dice_game(hp)
