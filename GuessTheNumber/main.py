import random
import os

def play_game():
    
    logo = """
   ___                          _____  _                 __                    _                 
  / _ \ _   _   ___  ___  ___  /__   \| |__    ___    /\ \ \ _   _  _ __ ___  | |__    ___  _ __ 
 / /_\/| | | | / _ \/ __|/ __|   / /\/| '_ \  / _ \  /  \/ /| | | || '_ ` _ \ | '_ \  / _ \| '__|
/ /_\\ | |_| ||  __/\__ \\__ \  / /   | | | ||  __/ / /\  / | |_| || | | | | || |_) ||  __/| |   
\____/  \__,_| \___||___/|___/  \/    |_| |_| \___| \_\ \/   \__,_||_| |_| |_||_.__/  \___||_|   

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
"""

    os.system("clear")
    print(logo)
    difficult_type = input("Choose a difficulty. Type 'easy' or 'hard':")

    if difficult_type.lower() == "easy":
        attempts = 10
    elif difficult_type.lower() == "hard":
        attempts = 5
    else:
        print("You entered the wrong thing. So I picked it with hard :)")
        attempts = 5

    random_number = random.randrange(1,101)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guessing_number = int(input("Make a guess: "))
            if random_number == guessing_number:
                break
            elif random_number < guessing_number:
                print("Too high.")
            elif random_number > guessing_number:
                print("Too low.")
        except:
            guessing_number = None
            print("You have to enter properly")
        
        attempts -= 1
        print("Guess again.")

    print(f"Number is {random_number}!")
    if guessing_number and isinstance(guessing_number, int):
        if random_number == guessing_number:
            print(f"You Win!")
        else:
            print("You Lose")
    else:
        print("What are you doing?")

if __name__ == "__main__":
    play_game()