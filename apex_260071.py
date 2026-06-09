# Program: Guessing Game
# Author: Sandesh Shrestha
# Date: 09/06/2026
# Description: A number guessing game that tracks guesses, games played, and prints a summary.

import random # Required to generate the random number

# Class Constant equivalent in Python
MAX_GUESS = 100

def generate_random_number():
    """Generates a random number between 1 and MAX_GUESS."""
    return random.randint(1, MAX_GUESS)

def display_instructions():
    """Displays the game instructions to the user."""
    print("Guessing game")
    print(f"I will think of a number between 1 and {MAX_GUESS}")
    print("Please guess my number. For each guess, I will tell you whether the")
    print("correct answer (my number) is higher or lower than your guess.")

def play_single_round():
    """Plays a single round of the game and returns the number of guesses."""
    target_number = generate_random_number()
    print("I am thinking of a number...")
    
    guesses = 0
    # The game loop for a single round
    while True:
        # Prompting the user for input
        user_guess = int(input("Your guess? "))
        guesses += 1
        
        # Checking the guess against the target number
        if user_guess < target_number:
            print("higher")
        elif user_guess > target_number:
            print("lower")
        else:
            print(f"You got it right in {guesses} guesses")
            return guesses

def main():
    """Main function that handles the overall program loop and statistics."""
    total_games = 0
    total_guesses = 0
    max_guesses = 0
    
    display_instructions()
    
    play_again = True
    # The main loop that keeps the game running until the user quits
    while play_again:
        # Run a round and capture how many guesses it took
        guesses_this_game = play_single_round()
        
        # Update our tracking variables
        total_games += 1
        total_guesses += guesses_this_game
        
        # Check if the current game had the highest number of guesses
        if guesses_this_game > max_guesses:
            max_guesses = guesses_this_game
        
        # Using input() combined with string methods to act like Java's Scanner next()
        response = input("Would you like to play again? (Press 'Yes' or 'No'): ").strip().lower()
        
        # Check if the user's response starts with 'y'
        if not response.startswith('y'):
            play_again = False
    
    # Print the final summary report
    print("\nOverall results:")
    print(f"Total games = {total_games}")
    print(f"Total guesses = {total_guesses}")
    
    if total_games > 0:
        avg_guesses = total_guesses / total_games
        # .2f formats the average to 2 decimal places
        print(f"Average guesses/game = {avg_guesses:.2f}")
        
    print(f"Max guesses = {max_guesses}")

# This ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()