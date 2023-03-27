"""
Number guessing game

"""
# Put your import statements here
import random

# Put your named constants here
MAX_GUESS = 6
GAME_WON = 'W'
GAME_LOST = 'L'


# Put function definitions here
# Describe what the function does
def get_user_guess():
    """
    Ask the user for their guess. Validate that the user enters a number between 1 and 100.
    This function does not return until the user enters a number between 1 and 100.

    Return the number guesses as an int data type
    """
    user_guess = 0
    while user_guess < 1 or user_guess > 100:
        user_guess = input("Guess a number between 1 and 100: ")
        if user_guess.isdigit() is True:
            user_guess = int(user_guess)
        else:
            user_guess = 0
            print("Enter a numeric value.")
    return user_guess


def play_game(number_to_guess):
    """
    The input to this function is the number the user is attempting to guess.
    It is an int data type.
    Plays the game until the user correctly guesses the number or
    runs out of guesses without correctly guessing number.
    Return 'W' when the game is won and return 'L' when the game is lost.
    """
    result = None
    guess_cnt = 0
    guess_left = MAX_GUESS - guess_cnt

    while guess_left > 0 and result != GAME_WON:
        guess = get_user_guess()
        if guess < number_to_guess:
            guess_cnt += 1
            guess_left -= 1
            print(f"Your guess is to low! You have {guess_left} guesses remaining.")
        elif guess > number_to_guess:
            guess_cnt += 1
            guess_left -= 1
            print(f"Your guess is to high! You have {guess_left} guesses remaining.")
        elif guess == number_to_guess:
            guess_cnt += 1
            print('')
            print(f"Congratulations, you guessed the number after {guess_cnt} guesses!")
            result = GAME_WON

    if guess_left <= 0:
        result = GAME_LOST
        print('')
        print(f"Sorry, you ran out of guesses. The number was {number_to_guess}.")

    return result


def main():
    """
    This function ends when the user no longer wants to play.
    """
    again = 'y' or 'Y'
    while again == ('y' or 'Y'):
        #  while again == 'y' or again == 'Y'
        print("Let's play!")
        print('')
        number = random.randint(1, 100)
        play_game(number)
        again = input("Do you want to play again? (Yes/No) ")
        print('')


if __name__ == '__main__':
    main()

    
    
    
