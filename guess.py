# 1. Store a number
number = 11

# 2. Ask the user to guess the number we have stored
print("Guess the number I am holding")
# Type casting: converting from one data type to another data type
# For example, "8" to 8.
user_number = int(input())

# 3. Check if the user number is the number we have stored
# 4. Give an output to tell the user if it is right or wrong

# This is an if block. Starts here
if user_number == number:
    print("You are right!")
else:
    print("You are wrong!")
# Ends here

print("Thanks for playing my game!")
