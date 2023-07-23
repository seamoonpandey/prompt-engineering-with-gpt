import random

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        damage -= self.defense
        if damage < 0:
            damage = 0
        self.hp -= damage

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def is_alive(self):
        return self.hp > 0

    def reset_health(self):
        self.hp = self.max_hp

    def special_attack(self, enemy):
        damage = random.randint(self.attack, self.attack * 2)
        self.take_damage(self.max_hp // 10)  # Cost of using special attack
        enemy.take_damage(damage)
        print(f"{self.name} performs a special attack on {enemy.name} for {damage} damage!")

    def use_potion(self):
        heal_amount = random.randint(15, 25)
        self.hp = min(self.hp + heal_amount, self.max_hp)
        print(f"{self.name} uses a healing potion and regains {heal_amount} HP!")

    def critical_hit(self, enemy):
        if random.random() < 0.3:  # 30% chance of critical hit
            damage = self.attack * 2
            enemy.take_damage(damage)
            print(f"{self.name} lands a critical hit on {enemy.name} for {damage} damage!")
