import random
import time


PLAY_AGAIN = "yes"


# 1. introduce the user to the dragon realm
def intro():
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly and
    will share his treasure with you. The other dragon is 
    greedy and hunger, and will eat you on sight.''')


# 2. User chooses a cave
def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave do you want to go into? (1 or 2)")
        cave = input()

    return cave


# 3. Check the cave the user chooses
def check_cave(choice: str):
    friendly_cave = random.randint(1, 2)
    print("You approach the cave...")
    time.sleep(3)
    print("It is dark and spooky...")
    time.sleep(3)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(3)

    if choice == str(friendly_cave):
        print("Gives you his treasure!")
    else:
        print("Eats you up!")


while PLAY_AGAIN == "yes":
    intro()
    user_choice = choose_cave()
    check_cave(user_choice)  # function interface for check_cave function

    print("Do you want to play again (yes or no)")
    PLAY_AGAIN = input()



