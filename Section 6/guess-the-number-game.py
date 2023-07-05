from random import randint 

# create a global constent difficulty function
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# Create a global var to deduct the number of turns 
turns = 0 

# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of remaining"""
    if guess > answer:
       print("Too high!")
       return turns - 1 
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make a function to set difficulty
def set_difficulty():
   level = (input("Choose a difficulty. Type 'easy' or 'hard': ")) 
   if level == "easy":
       return EASY_LEVEL_TURNS
   else:
       return HARD_LEVEL_TURNS
   
# Choosing a random number between 1 - 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 an 100.")
answer = randint(1, 100)


turns = set_difficulty()    

# Repeat the guessing functionality if they get it wrong
guess = 0
while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    # Let the user guess the number
    guess = int(input("Make a guess: "))


# Track the number of turns and reduce by 1 if they get it wrong
# Call the check_answer function to check if the number was correct
turns = check_answer(guess, answer, turns)
if turns == 0:
    print("You've run out of guesses, you lose!")
