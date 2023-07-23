from game_logic import initialize_game, get_user_guess
from game_utils import welcome_player, display_shells


def play_game():
    welcome_player()

    difficulty = int(input("Choose the difficulty level (1 to 10): "))

    print("Welcome to the ShellBall Challenge!")
    print("Try to guess which shell the ball is under.")

    while True:
        shells, ball_location = initialize_game(difficulty)

        display_shells(shells)

        user_guess = get_user_guess(len(shells))

        if user_guess == ball_location:
            print("Congratulations! You found the ball!")
        else:
            print(f"Sorry, you guessed wrong. The ball was under shell {ball_location}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break


if __name__ == "__main__":
    play_game()
