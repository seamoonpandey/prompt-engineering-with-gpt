import time


def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


def get_user_choice(options):
    while True:
        choice = input("Enter the number of your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return choice
        print("Invalid input. Please enter the number corresponding to your choice.")


def scenario_intro(scenario_text):
    print_slow(scenario_text)


def game_over():
    print_slow("Game over! Thanks for playing.")
    # You can add more messages or actions here if you like.


def main():
    # Start the game with a welcome message.
    print_slow("Welcome to the Text-based Adventure Game!")
    player_name = input("Enter your name: ")
    print_slow(f"Hello, {player_name}! Let's begin the adventure.")

    # Start of the game scenarios.
    # You can define and structure your scenarios here.

    # For testing purposes, we'll just create a simple example scenario.
    scenario_intro("You find yourself standing in front of two doors.")
    print_slow("Do you choose:")
    print("1. The left door.")
    print("2. The right door.")

    user_choice = get_user_choice([1, 2])

    if user_choice == 1:
        scenario_intro("You open the left door and find a treasure chest!")
        print_slow("Congratulations! You win!")
    elif user_choice == 2:
        scenario_intro("You open the right door and are greeted by a fierce dragon.")
        print_slow("You have been eaten by the dragon. Game over!")
        game_over()


if __name__ == "__main__":
    main()
