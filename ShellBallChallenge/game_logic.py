import random

def initialize_game(difficulty):
    num_cups = difficulty + 2
    shells = ['[ ]'] * num_cups
    ball_location = random.randint(0, num_cups - 1)
    return shells, ball_location

def get_user_guess(num_cups):
    while True:
        try:
            guess = int(input(f"Enter your guess (0 to {num_cups - 1}): "))
            if 0 <= guess < num_cups:
                return guess
            else:
                print(f"Invalid input. Please enter a number between 0 and {num_cups - 1}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
