import sys
import random
from string import hexdigits
from ipaddress import IPv4Address
from string import ascii_lowercase


# Color Declarations
class colors:
    WARNING = '\033[93m'
    GOBLIN = '\033[92m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'


# Declarations should go here
# Self REM: Check wich is important wich is not
key = [0]
health = [3]
result_ipgame = 0
go_val = int(3)
python_result = int(0)
potion_grave = int(0)
potion_dice = 0
solved2 = 0
grave_outc = 0
solved = 0
potion_forest = 0
damage_village = 0
damage_curch = 0
IOT_result = 3
end_dice = 0
math1 = 0
hangmank = 2
runningoutofnames = 2


# Hangman Game
def hangman(hangmank):
    num_attempts = 12
    word = "village"

    # Generting the next letter, checking if its correct
    def get_next_letter(letters_left):
        # Get the next letter from the user
        while True:
            next_letter = input("Write your next character: ").lower()
            if len(next_letter) != 1:
                print("{0} is not one character".format(next_letter))
            elif next_letter not in ascii_lowercase:
                print("{0} is not a letter".format(next_letter))
            elif next_letter not in letters_left:
                print("{0} has been typed before".format(next_letter))
            else:
                letters_left.remove(next_letter)
                return next_letter

    # Implemented for outcome
    xyc = 0

    def play_game(xyc):
        # The game function
        print("You have entered the Hangman game")
        attempts_left = num_attempts

        # Variables inside the game
        current_word = [letter not in ascii_lowercase for letter in word]
        letters_left = set(ascii_lowercase)
        wrong_letters = []
        word_solved = False

        # Game loop
        while attempts_left > 0 and not word_solved:
            print('Word: {0}'.format(current_word))
            print('Attempts left: {0}'.format(attempts_left))
            print('Previous guesses: {0}'.format(' '.join(wrong_letters)))

            # Get next letter from the user
            next_letter = get_next_letter(letters_left)

            # Checks if the letter is in the word
            if next_letter in word:
                # Correct guess
                print('{0} is in the word!'.format(next_letter))
                # Show the letter inside the word
                for i in range(len(word)):
                    if word[i] == next_letter:
                        current_word[i] = next_letter

            else:
                # Wrong guess
                print('{0} is not in the word!'.format(next_letter))

                # remove an attempt
                attempts_left -= 1
                wrong_letters.append(next_letter)

            # Check if the word is solved
            if False not in current_word:
                word_solved = True
            print()

        # Give feedback of win or defeat
        if word_solved:
            # print("Congratulations! You have won! The correct word was", word,"!")
            xyc = 1
            return xyc
        else:
            # print("You have failed, try again!")
            xyc = 0
            return xyc

    # Give feedback of win or defeat
    xyc = play_game(xyc)
    if int(xyc) == 0:
        hangmank = 0
        return hangmank
    else:
        hangmank = 1
        return hangmank


# Mtah Game
def math_game(math1):
    score = 0
    questions = {}
    passed = False

    print("Hello to the Math game! \nHere you will get 10 math problems to solve. \nSolve at least 8 to proceed")
    for i in range(10):
        # Grabbing random values
        int_a = random.randint(10, 20)
        int_b = random.randint(1, 9)
        # Declare operators
        operators = ['+', '-', '*', '//']
        # Random Operator
        operator_value = random.choice(operators)
        question = str(int_a) + " " + operator_value + " " + str(int_b)
        answer = str(eval(question))
        question += ": "
        questions.update({question: answer})

    for q in questions.keys():
        user_answer = input(q)
        if questions.get(q) == user_answer:
            print("Correct!")
            score += 1
        else:
            print("You're Wrong!")
    print("You have " + str(score) + " points!")
    # Scoreing Stuff
    if score < 8:
        math1 = 0
        return math1
    else:
        passed = True
        math1 = 1
        return math1


# IOT Game
def IOT_Game(IOT_result):
    def resistor(resist_sum, IOT_result, resistor1, resistor2, resistor3):
        if resist_sum == resistor1 + resistor2 + resistor3:
            IOT_result = 1
            return IOT_result
        else:
            IOT_result = 2
            return IOT_result

    # Current Calculate Function, Check if Input is = Calculated
    def current(resist_sum):
        voltage = random.randrange(1, 1000, 1)
        print("Voltage", voltage, "Guess the current!")
        current_num = voltage // resist_sum
        guess_current = int(input())
        if current_num == guess_current:
            IOT_result = 1
            return IOT_result
        else:
            IOT_result = 2
            return IOT_result

    # Generating 3 resistors
    resistor1 = random.randrange(1, 10, 1)
    print("Resistor 1 =", resistor1)
    resistor2 = random.randrange(1, 10, 1)
    print("Resistor 2 =", resistor2)
    resistor3 = random.randrange(1, 10, 1)
    print("Resistor 3 =", resistor3)

    print("Please calculate the resistors sum value!")

    resist_sum = int(input())
    IOT_result = resistor(resist_sum, IOT_result, resistor1, resistor2, resistor3)
    # Outcome value stuff
    if IOT_result == 1:
        print("Great work, keep on going!")
        IOT_result = current(resist_sum)
        if IOT_result == 1:
            print("Good job!")
            return IOT_result
        elif IOT_result == 2:
            print("Wrong anwser")
            return IOT_result
    elif IOT_result == 2:
        print("Wrong Anwser")
        return IOT_result


# The Custom IP Game
# It works properly now, crazy shit
def ipgame(result_ipgame):
    def random_ip(seed):
        random.seed(seed)
        return str(IPv4Address(random.getrandbits(32)))

    print("Please calculate the subnet of the following ip:")

    # IP Random generation
    game_ip = (random_ip(seed=random))  # type: str
    print(game_ip)

    # Dividing the IP into four 8 bit sections
    assert game_ip.count(".") == 3
    ip_parts = game_ip.split(".")
    ip_parts = [int(part) for part in ip_parts]
    first, second, third, fourth = ip_parts

    if first < 128:  # Type A Address
        # Generating a custom subnet mask
        cus_subn_mask = random.randrange(9, 32, 1)
        print(cus_subn_mask, "is the custom subnet mask")

        # Looking for user input if it is the same:
        print("Please type your sollution, it should be one number without dots:")
        user_input = input()

        # Adding -8 all the time, because we doesn't wana to deal with the first 8 bit of the IP
        upc = cus_subn_mask - 8

        # If the subnet mask is 8 or less character long belongs to here
        if upc < 9:
            # Casting binear from the IP-s important section
            lst_num_sec = [int(j) for j in list('{0:08b}'.format(second))]

            # Making a fake unary format from the Custom subnet mask
            unar_num = upc * "1"
            ' '.join(format(ord(x), 'b') for x in unar_num)

            # Filling up a list from the custom subnet mask in fake 8 bit binary
            kgt = int(float(unar_num))
            a = int(unar_num, 2)
            unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

            # Now doing some neat segragation
            # Fillig up a list in reverse from the fake binary list
            def seg1and0(arr, n):
                count = 0
                for i in range(0, n):
                    if (arr[i] == 1):
                        count = count + 1
                for i in range(0, count):
                    arr[i] = 1
                for i in range(count, n):
                    arr[i] = 0
                return arr

            # Using the function in the field
            n = len(unar_num_lst)
            unar_num_lst_rev = seg1and0(unar_num_lst, n)

            # The actual comparison part
            if unar_num_lst_rev[0] == 0:
                lst_num_sec[0] = 0
            if unar_num_lst_rev[1] == 0:
                lst_num_sec[1] = 0
            if unar_num_lst_rev[2] == 0:
                lst_num_sec[2] = 0
            if unar_num_lst_rev[3] == 0:
                lst_num_sec[3] = 0
            if unar_num_lst_rev[4] == 0:
                lst_num_sec[4] = 0
            if unar_num_lst_rev[5] == 0:
                lst_num_sec[5] = 0
            if unar_num_lst_rev[6] == 0:
                lst_num_sec[6] = 0
            if unar_num_lst_rev[7] == 0:
                lst_num_sec[7] = 1

            # Generating a binear number from the list
            masked_ip_bin = ''.join(str(e) for e in lst_num_sec)

            # Generating a decimal number from the binary
            masked_ip_dec = int(masked_ip_bin, 2)

            print("So guys we did it, the ip is the following:", first, masked_ip_dec, "0", "0")

            out_c = str(first) + str(masked_ip_dec) + '0' + '0'

            if str(user_input) == out_c:
                print("You done well, good job!")
                result_ipgame = 1
                return result_ipgame
            else:
                print("Sorry, you missed the chance!")
                result_ipgame = 0
                return result_ipgame


        elif upc < 17:
            # Adding -8 all the time, because we doesn't wana to deal with the first and the second 8 bit of the IP
            upc2 = upc - 8

            # Casting binear from the IP-s important section
            lst_num_third = [int(i) for i in list('{0:08b}'.format(third))]

            # Making a fake unary format from the Custom subnet mask
            unar_num = upc2 * "1"
            ' '.join(format(ord(x), 'b') for x in unar_num)

            # Filling up a list from the custom subnet mask in fake 8 bit binary
            kgt = int(float(unar_num))
            a = int(unar_num, 2)
            unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

            # Now doing some neat segragation
            # Filling up a list in reverse from the fake binary list
            def seg1and0(arr, n):
                count = 0
                for i in range(0, n):
                    if (arr[i] == 1):
                        count = count + 1
                for i in range(0, count):
                    arr[i] = 1
                for i in range(count, n):
                    arr[i] = 0
                return arr

            # Using the function in the field
            n = len(unar_num_lst)
            unar_num_lst_rev = seg1and0(unar_num_lst, n)

            # The actual comparison part
            if unar_num_lst_rev[0] == 0:
                lst_num_third[0] = 0
            if unar_num_lst_rev[1] == 0:
                lst_num_third[1] = 0
            if unar_num_lst_rev[2] == 0:
                lst_num_third[2] = 0
            if unar_num_lst_rev[3] == 0:
                lst_num_third[3] = 0
            if unar_num_lst_rev[4] == 0:
                lst_num_third[4] = 0
            if unar_num_lst_rev[5] == 0:
                lst_num_third[5] = 0
            if unar_num_lst_rev[6] == 0:
                lst_num_third[6] = 0
            if unar_num_lst_rev[7] == 0:
                lst_num_third[7] = 0

            # Generating a binear number from the list
            masked_ip_bin = ''.join(str(e) for e in lst_num_third)

            # Generating a decimal number from the binary
            masked_ip_dec = int(masked_ip_bin, 2)

            print("So guys we did it, the ip is the following:", first, second, masked_ip_dec, "0")

            out_c = str(first) + str(second) + str(masked_ip_dec) + '0'

            if str(user_input) == out_c:
                print("You done well, good job!")
                result_ipgame = 1
                return result_ipgame
            else:
                print("Sorry, you missed the chance!")
                result_ipgame = 0
                return result_ipgame

        elif upc < 25:

            # Adding -8 all the time, because we doesn't wana to deal with the first and the second and the third 8 bit of the IP
            upc3 = upc - 16

            # Casting binear from the IP-s important section
            lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]

            # Making a fake unary format from the Custom subnet mask
            unar_num = upc3 * "1"
            ' '.join(format(ord(x), 'b') for x in unar_num)
            kgt = int(float(unar_num))

            # Filling up a list from the custom subnet mask in fake 8 bit binary
            a = int(unar_num, 2)
            unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

            # Now doing some neat segragation
            # Filling up a list in reverse from the fake binary list
            def seg1and0(arr, n):
                count = 0
                for i in range(0, n):
                    if (arr[i] == 1):
                        count = count + 1
                for i in range(0, count):
                    arr[i] = 1
                for i in range(count, n):
                    arr[i] = 0
                return arr

            # Using the function in the field
            n = len(unar_num_lst)
            unar_num_lst_rev = seg1and0(unar_num_lst, n)

            # The actual comparison part
            if unar_num_lst_rev[0] == 0:
                lst_num_fourth[0] = 0
            if unar_num_lst_rev[1] == 0:
                lst_num_fourth[1] = 0
            if unar_num_lst_rev[2] == 0:
                lst_num_fourth[2] = 0
            if unar_num_lst_rev[3] == 0:
                lst_num_fourth[3] = 0
            if unar_num_lst_rev[4] == 0:
                lst_num_fourth[4] = 0
            if unar_num_lst_rev[5] == 0:
                lst_num_fourth[5] = 0
            if unar_num_lst_rev[6] == 0:
                lst_num_fourth[6] = 0
            if unar_num_lst_rev[7] == 0:
                lst_num_fourth[7] = 0

            # Generating a binear number from the list
            masked_ip_bin = ''.join(str(e) for e in lst_num_fourth)

            masked_ip_dec = int(masked_ip_bin, 2)

            print("So guys we did it, the ip is the following:", first, second, third, masked_ip_dec)

            out_c = str(first) + str(second) + str(third) + str(masked_ip_dec)

            if str(user_input) == out_c:
                print("You done well, good job!")
                result_ipgame = 1
                return result_ipgame
            else:
                print("Sorry, you missed the chance!")
                result_ipgame = 0
                return result_ipgame

    elif first < 192:  # Type B Address

        # Generating a custom subnet mask
        cus_subn_mask = random.randrange(17, 32, 1)
        print(cus_subn_mask, "is the custom subnet mask")

        # Looking for user input if it is the same:
        print("Please type your sollution, it should be one number without dots:")
        user_input = input()

        # Adding -16 all the time, because we doesn't wana to deal with the first 16 bit of the IP
        upc = cus_subn_mask - 16

        if upc < 9:
            # Casting binear from the IP-s important section
            lst_num_third = [int(i) for i in list('{0:08b}'.format(third))]

            # Making a fake unary format from the Custom subnet mask
            unar_num = upc * "1"
            ' '.join(format(ord(x), 'b') for x in unar_num)
            kgt = int(float(unar_num))

            # Filling up a list from the custom subnet mask in fake 8 bit binary
            a = int(unar_num, 2)
            unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

            # Now doing some neat segragation
            # Fillig up a list in reverse from the fake binary list
            def seg1and0(arr, n):
                count = 0
                for i in range(0, n):
                    if (arr[i] == 1):
                        count = count + 1
                for i in range(0, count):
                    arr[i] = 1
                for i in range(count, n):
                    arr[i] = 0
                return arr

            # Using the function in the field
            n = len(unar_num_lst)
            unar_num_lst_rev = seg1and0(unar_num_lst, n)

            # The actual comparison part

            if unar_num_lst_rev[0] == 0:
                lst_num_third[0] = 0
            if unar_num_lst_rev[1] == 0:
                lst_num_third[1] = 0
            if unar_num_lst_rev[2] == 0:
                lst_num_third[2] = 0
            if unar_num_lst_rev[3] == 0:
                lst_num_third[3] = 0
            if unar_num_lst_rev[4] == 0:
                lst_num_third[4] = 0
            if unar_num_lst_rev[5] == 0:
                lst_num_third[5] = 0
            if unar_num_lst_rev[6] == 0:
                lst_num_third[6] = 0
            if unar_num_lst_rev[7] == 0:
                lst_num_third[7] = 0

            # Generating a binear number from the list
            masked_ip_bin = ''.join(str(e) for e in lst_num_third)

            # Generating a decimal number from the binary
            masked_ip_dec = int(masked_ip_bin, 2)

            print("So guys we did it, the ip is the following:", first, second, masked_ip_dec, "0")

            out_c = str(first) + str(second) + str(masked_ip_dec) + '0'

            if str(user_input) == out_c:
                print("You done well, good job!")
                result_ipgame = 1
                return result_ipgame
            else:
                print("Sorry, you missed the chance!")
                result_ipgame = 0
                return result_ipgame


        elif upc < 17:

            # Adding -8 all the time, because we doesn't wana to deal with the first 8 bit of the IP
            upc2 = upc - 8

            # Casting binear from the IP-s important section
            lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]

            # Making a fake unary format from the Custom subnet mask
            unar_num = upc2 * "1"
            ' '.join(format(ord(x), 'b') for x in unar_num)
            kgt = int(float(unar_num))

            # Filling up a list from the custom subnet mask in fake 8 bit binary
            a = int(unar_num, 2)
            unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

            # Now doing some neat segragation
            # Fillig up a list in reverse from the fake binary list
            def seg1and0(arr, n):
                count = 0
                for i in range(0, n):
                    if (arr[i] == 1):
                        count = count + 1
                for i in range(0, count):
                    arr[i] = 1
                for i in range(count, n):
                    arr[i] = 0
                return arr

            # Using the function in the field
            n = len(unar_num_lst)
            unar_num_lst_rev = seg1and0(unar_num_lst, n)

            # The actual comparison part
            if unar_num_lst_rev[0] == 0:
                lst_num_fourth[0] = 0
            if unar_num_lst_rev[1] == 0:
                lst_num_fourth[1] = 0
            if unar_num_lst_rev[2] == 0:
                lst_num_fourth[2] = 0
            if unar_num_lst_rev[3] == 0:
                lst_num_fourth[3] = 0
            if unar_num_lst_rev[4] == 0:
                lst_num_fourth[4] = 0
            if unar_num_lst_rev[5] == 0:
                lst_num_fourth[5] = 0
            if unar_num_lst_rev[6] == 0:
                lst_num_fourth[6] = 0
            if unar_num_lst_rev[7] == 0:
                lst_num_fourth[7] = 0

            # Generating a binear number from the list
            masked_ip_bin = ''.join(str(e) for e in lst_num_fourth)

            # Generating a decimal number from the binary
            masked_ip_dec = int(masked_ip_bin, 2)

            print("So guys we did it, the ip is the following:", first, second, third, masked_ip_dec)

            out_c = str(first) + str(second) + str(third) + str(masked_ip_dec)

            if str(user_input) == out_c:
                print("You done well, good job!")
                result_ipgame = 1
                return result_ipgame
            else:
                print("Sorry, you missed the chance!")
                result_ipgame = 0
                return result_ipgame



    elif first < 256:  # Type C Address

        # Generating Custom subnet
        cus_subn_mask = random.randrange(25, 32, 1)
        print(cus_subn_mask, "is the custom subnet mask")

        # Looking for user input if it is the same:
        print("Please type your sollution, it should be one number without dots:")
        user_input = input()

        # Casting binear from the IP-s important section
        lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]
        # Adding -24, because we doesn't wana to deal with the first 24 bit of the IP
        upc = cus_subn_mask - 24

        # Making a fake unary format from the Custom subnet mask
        unar_num = upc * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        kgt = int(float(unar_num))

        # Filling up a list from the custom subnet mask in fake 8 bit binary
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

        # Now doing some neat segragation
        # Fillig up a list in reverse from the fake binary list
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0
            return arr

        # Using the function in the field
        n = len(unar_num_lst)
        unar_num_lst_rev = seg1and0(unar_num_lst, n)

        # The actual comparison part
        if unar_num_lst_rev[0] == 0:
            lst_num_fourth[0] = 0
        if unar_num_lst_rev[1] == 0:
            lst_num_fourth[1] = 0
        if unar_num_lst_rev[2] == 0:
            lst_num_fourth[2] = 0
        if unar_num_lst_rev[3] == 0:
            lst_num_fourth[3] = 0
        if unar_num_lst_rev[4] == 0:
            lst_num_fourth[4] = 0
        if unar_num_lst_rev[5] == 0:
            lst_num_fourth[5] = 0
        if unar_num_lst_rev[6] == 0:
            lst_num_fourth[6] = 0
        if unar_num_lst_rev[7] == 0:
            lst_num_fourth[7] = 0

        # Generating a binear number from the list
        masked_ip_bin = ''.join(str(e) for e in lst_num_fourth)

        # Generating a decimal number from the binary
        masked_ip_dec = int(masked_ip_bin, 2)

        print("So guys we did it, the ip is the following:", first, second, third, masked_ip_dec)
        out_c = str(first) + str(second) + str(third) + str(masked_ip_dec)

        if str(user_input) == out_c:
            print("You done well, good job!")
            result_ipgame = 1
            return result_ipgame
        else:
            print("Sorry, you missed the chance!")
            result_ipgame = 0
            return result_ipgame


# Dice Game ------------------------------------------------------------------------------------------------------------
# Now works as it should
def dice_game(end_dice, end_roll, health):
    end_roll = 0

    def roll_dice(end_roll):
        # Generating 3 randoms for the user
        pd1 = random.randrange(1, 6, 1)
        print("Your first number is:", pd1)
        input("Press Enter to continue...")
        pd2 = random.randrange(1, 6, 1)
        print("Your second number is:", pd2)
        input("Press Enter to continue...")
        pd3 = random.randrange(1, 6, 1)
        print("Your third number is:", pd3)
        input("Press Enter to continue...")
        # Sum Gen. Numbers
        pdd = pd1 + pd2 + pd3

        # Generating 3 randoms for the computer
        bd1 = random.randrange(1, 6, 1)
        print("Your enemies first number is:", bd1)
        input("Press Enter to continue...")
        bd2 = random.randrange(1, 6, 1)
        print("Your enemies second number is:", bd2)
        input("Press Enter to continue...")
        bd3 = random.randrange(1, 6, 1)
        print("Your enemies third number is:", bd3)
        # Sum Gen. Numbers
        bdd = bd1 + bd2 + bd3
        # Compare + Outcome Stuff
        if pdd > bdd:
            print("Ohh, lucky you!")
            end_roll = 1
            return end_roll

        if pdd < bdd:
            print("Nice, you lost the game!")
            end_roll = 2
            return end_roll

        if pdd == bdd:
            print(
                "You god damn gangster, its a draw!-you said, but suddenly they raised a revolver to your had! I think we all understand the situation! ")
            end_roll = 2
            return end_roll

    # Health stuff, kinda complicated, from list gen str.
    print(health)
    print("A few cheeky bastard come next to you. They asking you want to play dice with them? Of course you say yes!")
    print("But suddenly you dont know what is the bet? “Here we playing in lifepoints“-they said! ")
    print("How many lifepoints you want to play with?")
    print("One Hp is looks eniough for me, doesnt it?")
    healthpoint = str(health).strip('[]')
    print(health)
    lifep = int(input())
    print("Hp", healthpoint)
    if lifep > int(healthpoint):
        print("You dont have that much healthpoint")
        print("The bandits got annoyed about your altitude and left you!")
        print("You proceed to follow the road out of the forest. There you find a church.")
        goto_curch(damage_curch, IOT_result)
    elif lifep == 1:
        # Function Call
        end_roll = roll_dice(end_roll)
        if end_roll == 1:
            end_dice = 1
            return end_dice
        elif end_roll == 2:
            end_dice = 2
            if healthpoint == 0:
                exit("-You lost the game!")
            return end_dice
    elif lifep != 1:
        print("-One HP! No more, no less! Dont be greedy!")
        lifep = 1
        end_roll = roll_dice(end_roll)
        if end_roll == 1:
            end_dice = 1
            return end_dice
        elif end_roll == 2:
            end_dice = 2
            if healthpoint == 0:
                exit("-You lost the game!")
            return end_dice


# Minesweeper Game -----------------------------------------------------------------------------------------------------
# Most likely needs debug
def minesweeper(solved):
    class Cell(object):
        def __init__(self, is_mine, is_visible=False, is_flagged=False):
            self.is_mine = is_mine
            self.is_visible = is_visible
            self.is_flagged = is_flagged

        # Show function
        def show(self):
            self.is_visible = True

        # Flag Function
        def flag(self):
            self.is_flagged = not self.is_flagged

        # Mine function
        def place_mine(self):
            self.is_mine = True

    class Board(tuple):
        def __init__(self, tup):
            super().__init__()
            self.is_playing = True

        def mine_repr(self, row_id, col_id):
            cell = self[row_id][col_id]
            if cell.is_visible:
                if cell.is_mine:
                    return "M"
                else:
                    surr = self.count_surrounding(row_id, col_id)
                    return str(surr) if surr else " "
            elif cell.is_flagged:
                return "F"
            else:
                return "X"

        # Board Sting function, writes out useful stuff
        def __str__(self):
            board_string = ("Mines: " + str(self.remaining_mines) + "\n  " +
                            "".join([str(i) for i in range(len(self))]))
            for (row_id, row) in enumerate(self):
                board_string += ("\n" + str(row_id) + " " +
                                 "".join(self.mine_repr(row_id, col_id) for (col_id, _) in enumerate(row)) +
                                 " " + str(row_id))
            board_string += "\n  " + "".join([str(i) for i in range(len(self))])
            return board_string

        # Reveal cell function
        def show(self, row_id, col_id):
            cell = self[row_id][col_id]
            if not cell.is_visible:
                cell.show()

                if (cell.is_mine and not
                cell.is_flagged):
                    self.is_playing = False
                elif self.count_surrounding(row_id, col_id) == 0:
                    for (surr_row, surr_col) in self.get_neighbours(row_id, col_id):
                        if self.is_in_range(surr_row, surr_col):
                            self.show(surr_row, surr_col)

        # Whatif already visible, but try to flag
        def flag(self, row_id, col_id):
            cell = self[row_id][col_id]
            if not cell.is_visible:
                cell.flag()
            else:
                print("Cannot add flag, cell already visible.")

        # Mine Gen
        def place_mine(self, row_id, col_id):
            self[row_id][col_id].place_mine()

        # Calculate surr.
        def count_surrounding(self, row_id, col_id):
            return sum(1 for (surr_row, surr_col) in self.get_neighbours(row_id, col_id)
                       if (self.is_in_range(surr_row, surr_col) and
                           self[surr_row][surr_col].is_mine))

        # Neighbour values
        def get_neighbours(self, row_id, col_id):
            SURROUNDING = ((-1, -1), (-1, 0), (-1, 1),
                           (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1))
            return ((row_id + surr_row, col_id + surr_col) for (surr_row, surr_col) in SURROUNDING)

        def is_in_range(self, row_id, col_id):
            return 0 <= row_id < len(self) and 0 <= col_id < len(self)

        @property
        # Calculate remaining mines
        def remaining_mines(self):
            remaining = 0
            for row in self:
                for cell in row:
                    if cell.is_mine:
                        remaining += 1
                    if cell.is_flagged:
                        remaining -= 1
            return remaining

        @property
        # If the maze solved
        def is_solved(self):
            return all((cell.is_visible or cell.is_mine) for row in self for cell in row)

    # Board Creation function
    def create_board(size, mines):
        board = Board(tuple([tuple([Cell(False) for i in range(size)])
                             for j in range(size)]))
        available_pos = list(range((size - 1) * (size - 1)))
        for i in range(mines):
            new_pos = random.choice(available_pos)
            available_pos.remove(new_pos)
            (row_id, col_id) = (new_pos % 9, new_pos // 9)
            board.place_mine(row_id, col_id)
        return board

    # Input help, because i cant eneter the program here, that would be disguasting
    def get_move(board):
        INSTRUCTIONS = ("First, enter the column, followed by the row. To add or "
                        "remove a flag, add \"f\" after the row (for example, 64f "
                        "would place a flag on the 6th column, 4th row). Enter "
                        "your move: ")

        move = input("Enter your move (for help enter \"H\"): ")
        if move == "H":
            move = input(INSTRUCTIONS)

        while not is_valid(move, board):
            move = input("Invalid input. Enter your move (for help enter \"H\"): ")
            if move == "H":
                move = input(INSTRUCTIONS)

        return (int(move[1]), int(move[0]), move[-1] == "f")

    # Validate Input
    def is_valid(move_input, board):
        if move_input == "H" or (len(move_input) not in (2, 3) or
                                 not move_input[:1].isdigit() or
                                 int(move_input[0]) not in range(len(board)) or
                                 int(move_input[1]) not in range(len(board))):
            return False

        if len(move_input) == 3 and move_input[2] != "f":
            return False

        return True

    # Main driver function
    def main(solved):
        SIZE = 10
        MINES = 9
        board = create_board(SIZE, MINES)
        print(board)
        while board.is_playing and not board.is_solved:
            (row_id, col_id, is_flag) = get_move(board)
            if not is_flag:
                board.show(row_id, col_id)
            else:
                board.flag(row_id, col_id)
            print(board)

        if board.is_solved:
            solved = 1
            print("Congrats, you solved the puzzle")
            return solved
        else:
            print("Uh oh! You blew up!")
            solved = 2
            return solved

    # Function Call
    solved = main(solved)

    if solved == 1:
        print("you won the minesweeper game \n")
    return solved


# The first driver
# Not much, works fine
def driver():
    print("Where do you want to go first?")
    print(colors.WARNING + "Graveyard = 0, Forest = 1" + colors.ENDC)
    go_val = int(input())
    if go_val == 0:
        goto_grave(potion_grave, key)
    elif go_val == 1:
        goto_forest(potion_forest, potion_dice, health)
    else:
        print(colors.WARNING + "Please press 0 or 1" + colors.ENDC)
        exit("Fallow the instructions Kaj")


# The Curch chapter
# Done, needs test
def goto_curch(health, IOT_result):
    health = [1]
    print("You arrive at a large wooden church, it seems abandoned.\n"
          "Was the monk in the forest really the only one from the church? Or is there more you wonder. \n"
          "The door to the church seems unlocked, will you try to open it?\n")
    print(colors.WARNING + "Yes = 0, No = 1" + colors.ENDC)
    door = int(input())
    if door == 0:
        print("The door opens and you see a priest standing at the alter, otherwise the church is empty.\n"
              "The priest welcomes you to his church “Welcome stranger, come inside”.\n"
              "You walk inside the church, the priest doesn’t seem to sense your evil aura, but you definitely can tell that this man is in possession of holy magic.\n")
        print(
            "The priest walk towards you “I can tell you are not one of the living, you do not belong in this world.\n "
            "I will save your soul child, so you can find rest in the world of the dead.”\n"
            "You are left no choice but to fight the priests holy magic with your own dark powers.\n")
        IOT_result = IOT_Game(IOT_result)
        if IOT_result == 1:
            print("You done great job\n\n")
            goto_village(damage_village)
        elif IOT_result == 2:
            print("You failed\n\n")
            print("You lost a hp!")
            health[0] = health[0] - 1
            print("Courrent hp= = ", health)
            if health[0] == 0:
                exit("You lost the game")
            goto_village()



    elif door == 1:
        goto_forest(potion_forest, potion_dice, health)
    else:
        print(colors.WARNING + "Please press 0 or 1" + colors.ENDC)
        exit("Fallow the instructions Kaj")


# The forest chapter
# Now it kinda works fine
def goto_forest(health, end_dice, end_roll):
    print("You enter the forest, its dark and gloomy everywhere.\n "
          "As you walk along the road you meet a an evil looking cheeky bestard.\n"
          "“STOP RIGHT THERE EVILDOER! I WILL NOT ALLOW YOU TO PROCEED!”-he yells.\n")
    print(
        colors.WARNING + "If you would like to get closer press 0 or if you would like to go to the graveyard press 1" + colors.ENDC)
    health = [1]
    print(health)
    python_game = int(input())
    if python_game == 0:
        end_dice = dice_game(end_dice, end_roll, health)

        if end_dice == 1:
            print(
                "After defeating him the bandit collapses on the ground. You walk towards him.\n “Don’t kill me, please!” he says as he starts to cry. What do you do?")
            print(
                colors.WARNING + "If you would like kill him press 0, or if you might like to let him alive press 1" + colors.ENDC)
            python_dec = int(input())
            if python_dec == 0:
                print(
                    "Without doubt in your mind you raise your sword high and slices the bandit in half. His body falls to the ground.")
                potion_dice = potion_forest
            elif python_dec == 1:
                print("The bandit runs into the forest, you do not know whereto.")
                potion_dice = potion_forest
            else:
                print(colors.WARNING + "Please press 0 or 1" + colors.ENDC)
                exit("Fallow the instructions Kaj")

            print("You earned a hp!")
            print(health)
            health[0] = health[0] + 1
            print("Courrent hp = ", health)
            if int(str(health).strip('[]')) == 0:
                exit("You lost the game")
            goto_curch(health, IOT_result)

        elif end_dice == 2:
            print(health)
            print("You lost a hp!")
            health[0] = health[0] - 1
            print("Courrent hp = ", health)
            if int(str(health).strip('[]')) == 0:
                exit("You lost the game")
            goto_curch(health, IOT_result)


    elif python_game == 1:
        goto_grave(potion_grave,key)
    else:
        print(colors.WARNING + "Please press 0 or 1" + colors.ENDC)
        exit("Fallow the instructions Kaj")


# The Graveyard chapter
# It also works fine
# Cant loose hp
def goto_grave(health, key):
    health = [1]
    print("You arrive at the graveyard, here you meet an old man\n"
          "“Greetings my armored friend, what are you doing out here at this time of the night? Are you here to rob graves hehe?”\n")
    print(colors.WARNING + "Yes = 0 or No = 1" + colors.ENDC)
    grave1 = int(2)
    grave1 = int(input())
    if grave1 == 0:
        print(
            "“Hahaha you’re a funny guy. However on the more serious note, something has happened down in the catacombs. \nA grave has been opened, you don’t happen to be the man who opened it, do you?”")
    elif grave1 == 1:
        print(
            "“Oh, that is sad. It should be a very profitable business! I have heard that there should be a tomb in the catacombs where a lord is buried, he should have some treasure buried with him.\n If I was younger I think I would open that grave just to take a look”")
    else:
        print("Please press 0 or 1")
        exit("Fallow the instructions Kaj")

    print("The old man walks toward the catacombs. What do you do?")
    print(colors.WARNING + "Follow him = 0 , Look around = 1, Go back and go the forest = 2" + colors.ENDC)
    grave2 = int(3)
    grave2 = int(input())
    if grave2 == 0:
        print("The old man leads you to the catacombs, inside it you see the grave where you woke up.\n"
              "“There could be a treasure in here somewhere… by the way who are you? I can’t see your face underneath that helmet of yours”")
        print("What do you do?")
        print(colors.WARNING + "Remove helmet = 0 , Ignore his question and search the room = 1" + colors.ENDC)
        grave3 = int(2)
        grave3 = int(input())
        if grave3 == 0:
            print("You remove your helmet, revealing your skull. \n"
                  "The old man screams in terror and runs out of the catacombs. \n"
                  "You are now free to search the tomb without the old man.\n")
            goto_armory(health)
        if grave3 == 1:
            print("You find a chest hidden behind the coffin, there is a mysterious lock on it.")
            ipgame_result = ipgame(result_ipgame)
            if ipgame_result == 0:
                print("Oh No, you broke your lockpick")
                goto_armory(health)
            elif ipgame_result == 1:
                print("Great job, you succesfully opened the chest")
                print("Great job, you succesfully opened the chest")
                print(
                    colors.OKBLUE + "A Key and a Healt Potion has been added to your inventory!\nHealt Potion increase your Healt Point by 1! Great job!" + colors.ENDC)
                key[0] = 1
                print("You earned a hp!")
                print(health)
                health[0] = health[0] + 1
                print("Courrent hp = ", health)
                if int(str(health).strip('[]')) == 0:
                    exit("You lost the game")
                goto_armory(health)
    if grave2 == 1:
        print("You see a road that leads out of the graveyard and into a nearby village.")
        goto_village(health)

    if grave2 == 2:
        print("You goes ahead to the forest")
        goto_forest(health)


# Hero Chapter
def goto_hero(health):
    health = [1]
    print("After the dust has settled and the village has been pillaged you stand with a group of prisoners.\n"
          "“SIRE! We have captured the hero that crushed our castle and slayed you, we are ready to\n"
          " punish him for his crimes against the Goblin race and the forces of evil!” Rufus says.")
    print("“HANG HIM, HANG HIM!” the goblin army shouts.")
    runningoutofnames = hangman(hangmank)
    if runningoutofnames == 1:
        print("You won")
        goto_door(key, health)

    elif runningoutofnames == 0:
        print("You failed\n\n")
        print("You lost a hp!")
        health[0] = health[0] - 1
        print("Courrent hp= = ", health)
        if health[0] == 0:
            exit("You lost the game")
        goto_village(health)


# Game Ending
def goto_door(key, health):
    health = [1]
    keyk = str(key).strip('[]')
    if int(keyk) == 1:
        print("Great job, you won the game")
        exit()
    else:
        print("You havent find the key yet! Go back to the Grceyard to look around!")
        goto_grave(health, key)
    return


# The armory chapter
# Should be done - math game!
def goto_armory(health):
    print("On your road to the village you find an armory guarded by a paladin in shining armor. "
          "He sees you and yells at you “UNHOLY BEING I SHALL SMITE THEE!”")
    math1 = 0
    math1 = math_game(math1)
    if math1 == 1:
        print("Congratulations, you won!")
        goto_village(health)
    elif math1 == 0:
        print("You failed\n\n")
        print("You lost a hp!")
        health[0] = health[0] - 1
        print("Courrent hp = ", health)
        if health[0] == 0:
            exit("You lost the game")
        goto_village(health)


# The vilage chapter
# Can loose hp there
def goto_village(health):
    health = [1]
    print("As you arrive at the village you are greeted by the goblin Rufus.\n"
          "“Sire, we have gathered an army of goblins ready to raid the village at your command.\n"
          "You will have to lead us into combat. \n"
          "Are you ready for war, sire?”\n")
    print(colors.WARNING + "Ready for war = 0 , Not ready for war= 1" + colors.ENDC)
    vilage_dic = 2
    vilage_dic = int(input())
    if vilage_dic == 0:
        solved2 = minesweeper(solved)
        if solved2 == 1:
            goto_hero(health)
        if solved2 == 2:
            print("You failed\n\n")
            print("You lost a hp!")
            health[0] = health[0] - 1
            print("Courrent hp = ", health)
            if health[0] == 0:
                exit("You lost the game")
            goto_hero(health)

    if vilage_dic == 1:
        print("As you aren’t ready to raid the village you decide to return to the armory to prepare for war")
        goto_armory(health)


# First dialogue
print("You wake up in a dungeon, you don’t know where you are and everything is dark. \n"
      "You are in some sort of box, where the top is loose.\n"
      "You can see a small light shining through a crack in the roof of the box.\n"
      "You push the roof off the box and a flashing light shines into your face.You are in a catacomb.\n"
      "You see a small green goblin looking at you, it starts to yell “HES AWAKE! HES AWAKE!”\n"
      "Suddenly a group of goblins comes down into the catacomb and they all cheer.\n"
      "“Welcome back from the grave, my lord, I am Rufus your loyal servant” says an old goblin.\n"
      "Your body feels very fragile and weak, you look down at yourself and discover that you are nothing but a mere skeleton.\n"
      "“We have been waiting for you for a long time now, my lord, since the hero came and destroyed our castle and killed you sire.\n"
      "But now you are back and we can start to build your forces of evil once again!” Rufus says.\n"
      "\n"
      "You get up from your tomb, the box you were in was your grave, how are you alive you’re wondering? What has happened?\n"
      "\n"
      "You follow the goblins up the stairs and you arrive at a graveyard. It is night.\n"
      "The goblins leads you to a ruin of a castle.\n"
      "“here we are, you might not recognize it in its current state, but this used to be your home, our home. The Hero destroyed it and slaughtered many of us, including you”\n"
      "\n"
      "As you enter the main hall you are greeted by a goblin holding an armor and a sword.\n"
      "“Put this on sire, this will protect you from those pesky humans!”\n"
      "\n"
      "“Now you are ready sire! Come lets gather your forces of evil and take back what was taken from us!” Rufus says as he leads you out of the castle.\n"
      "“I am sadly too old to tag along with you, but you will do fine by yourself for now.\n"
      "\n"
      "Outside of the castle there is a road, which you follow, you meet a crossroad. One road leads to the graveyard where you woke up, the other leads to the forest.\n")

# Driver Function
goto_village(health)
driver()
