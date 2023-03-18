# 1. We want the computer to randomly choose from a set of numbers and store
import random

MIN_NUMBER = 1
MAX_NUMBER = 10
NUM_TRIALS = 5
NUM_ATTEMPTS = 1

NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)

# 2. Guess the number in 5 trials
while NUM_ATTEMPTS <= NUM_TRIALS:  # Scope of while loop starts here
    user_guess = int(input("Guess the number I am holding: "))  # user_guess is a local variable

    if user_guess == NUMBER:
        print(f"You are right! You guessed my number in {NUM_ATTEMPTS} guesses")
        break
    else:
        num_trials_left = NUM_TRIALS - NUM_ATTEMPTS
        if NUM_ATTEMPTS == NUM_TRIALS:
            print(f"You are wrong! You have {num_trials_left} attempts left. The right number is {NUMBER}")
        else:
            print(f"You are wrong! You have {num_trials_left} attempts left")

    NUM_ATTEMPTS += 1
    # Scope of while loop ends here

