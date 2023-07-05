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