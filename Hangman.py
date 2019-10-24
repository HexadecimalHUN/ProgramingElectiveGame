# Hangman game

from string import ascii_lowercase

num_attempts = 12
word = "Village"

def get_next_letter(letters_left):
    #Get the next letter from the user
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

xyc = 0
def play_game(xyc):
    #The game function
    print("You have entered the Hangman game")
    attempts_left = num_attempts

    #Variables inside the game
    current_word = [letter not in ascii_lowercase for letter in word]
    letters_left = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False

    #Game loop
    while attempts_left > 0 and not word_solved:
        print('Word: {0}'.format(current_word))
        print('Attempts left: {0}'.format(attempts_left))
        print('Previous guesses: {0}'.format(' '.join(wrong_letters)))

        #Get next letter from the user
        next_letter = get_next_letter(letters_left)

        #Checks if the letter is in the word
        if next_letter in word:
            #Correct guess
            print('{0} is in the word!'.format(next_letter))
            #Show the letter inside the word
            for i in range(len(word)):
                if word[i] == next_letter:
                    current_word[i] = next_letter

        else:
            #Wrong guess
            print('{0} is not in the word!'.format(next_letter))

            #remove an attempt
            attempts_left -= 1
            wrong_letters.append(next_letter)

        #Check if the word is solved
        if False not in current_word:
            word_solved = True
        print()

    #Give feedback of win or defeat
    if word_solved:
        print("Congratulations! You have won! The correct word was", word,"!")
        xyc = 1
        return xyc
    else:
        print("You have failed, try again!")
        xyc = 0
        return xyc

xyc = play_game(xyc)
if int(xyc) == 0:
    print("You failed")
else:
    print("Good job, you may proceed")