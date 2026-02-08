"""
CLI Number Guessing Game.

The program randomly selects a number between 1 and 100.
The user attempts to guess the number with feedback after each guess.
"""
import random

def generate_random_number() -> int:
    """ Generate a random number between 1 and 100. """
    return random.randint(1, 100)

def get_guess() -> int:
    """ Prompt the user for a valid guess between 1 and 100. """
    prompt = "\nEnter your guess> "
    invalid_input_msg = "Invalid input. Please enter an integer."
    invalid_range_msg = "Number must be between 1 and 100."

    while True:
        try:
            guess = int(input(prompt).strip())
        except ValueError:
            print(invalid_input_msg)
            continue

        if guess >= 1 and guess <= 100:
            break
        else:
            print(invalid_range_msg)

    return guess

def play_game() -> None:
    """ Run a single round of the guessing game. """
    n_attempts = 0
    random_number = generate_random_number()

    while True:
        guess = get_guess()
        n_attempts += 1
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {n_attempts} attempts.\n")
            break

def main() -> None:
    welcome_msg = "Welcome to the Number Guessing Game!\n"
    thinking_msg = "I'm thinking of a number between 1 and 100."
    retry_msg = "Play again? (y/n)> "
    goodbye_msg = "\nGoodbye!"

    print(welcome_msg)
    print(thinking_msg)

    play_again = 'y'
    while play_again == 'y':
        play_game()

        while True:
            play_again = input(retry_msg).strip()
            if play_again == 'y' or play_again == 'n':
                break

    print(goodbye_msg)

if __name__ == "__main__":
    main()

