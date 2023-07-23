from character import Character
from dragon import Dragon
import random
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class DragonSlayerGame:
    def __init__(self):
        self.levels = 3
        self.current_level = 1

    def load_scores(self):
        scores = {}
        try:
            with open('scores.txt', 'r') as file:
                for line in file:
                    name, score = line.strip().split(',')
                    scores[name] = int(score)
        except FileNotFoundError:
            pass
        return scores

    def save_score(self, player_name, score):
        with open('scores.txt', 'a') as file:
            file.write(f"{player_name},{score}\n")

    def print_status(self, player, enemy):
        print(f"{player.name}'s HP: {player.hp}/{player.max_hp}")
        print(f"{enemy.name}'s HP: {enemy.hp}/{enemy.max_hp}")

    def create_enemy(self, level):
        name = f"Dragon Level {level}"
        hp = random.randint(80 + level * 20, 100 + level * 30)
        attack = random.randint(15 + level * 2, 20 + level * 3)
        defense = random.randint(5 + level * 2, 8 + level * 3)
        return Dragon(name, hp, attack, defense)

    def play(self):
        print("Welcome to the Dragon Slayer game!")

        player_name = input("Enter your name: ")
        scores = self.load_scores()

        if player_name in scores:
            print(f"Welcome back, {player_name}! Your highest score is {scores[player_name]}.")

        player = Character(player_name, hp=100, attack=20, defense=5)

        print("You are facing a mighty dragon! Prepare for battle!")

        while player.is_alive() and self.current_level <= self.levels:
            print(f"\n--- Level {self.current_level} ---")
            dragon = self.create_enemy(self.current_level)

            while player.is_alive() and dragon.is_alive():
                print("\nYour turn:")
                action = input("Enter 'a' to attack, 's' for special attack, 'h' to use healing potion, or 'q' to quit: ")

                if action.lower() == 'q':
                    print("You have chosen to quit. Thanks for playing!")
                    return

                if action.lower() == 'a':
                    player.attack_enemy(dragon)
                elif action.lower() == 's':
                    player.special_attack(dragon)
                elif action.lower() == 'h':
                    player.use_potion()
                else:
                    print("Invalid input! Try again.")

                if dragon.is_alive():
                    print("\nDragon's turn:")
                    time.sleep(1)  # Adding a slight delay for dramatic effect
                    dragon.attack_enemy(player)

                self.print_status(player, dragon)

            if player.is_alive():
                print("\n" + Fore.GREEN + f"Congratulations! You have defeated {dragon.name}!")
                score = player.max_hp - player.hp
                self.save_score(player_name, score)
            else:
                print("\n" + Fore.RED + f"You were defeated by {dragon.name}. Game Over!")
                return

            player.reset_health()
            self.current_level += 1

        print("\n" + Fore.CYAN + "You have successfully completed all levels! You are a true Dragon Slayer!")
        return

if __name__ == "__main__":
    game = DragonSlayerGame()
    game.play()
