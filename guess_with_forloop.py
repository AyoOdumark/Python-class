import random

# Computer holds a random number between minimum number and maximum number
MIN_NUMBER = 1
MAX_NUMBER = 10
NUM_TRIALS = 5
# NUM_ATTEMPTS = 1

NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)

# num_attempts keeps track of the number of attempts as we go through our iterator
for num_attempts in range(1, NUM_TRIALS + 1):  # [1, 2, 3, 4, 5]
    user_guess = int(input("Guess the number I am holding: "))

    if user_guess == NUMBER:
        print(f"You are right! You guessed my number in {num_attempts} guesses")
        break
    else:
        num_trials_left = NUM_TRIALS - num_attempts
        if num_attempts == NUM_TRIALS:
            print(f"You are wrong! You have {num_trials_left} attempts left. The right number is {NUMBER}")
        else:
            print(f"You are wrong! You have {num_trials_left} attempts left")
