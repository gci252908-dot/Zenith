import random

from src.entities.player import Player
from src.entities.entity import Entity
from pyterminal import PyTerminal

class Battle:
    def __init__(self, player: Player, enemy: Entity):
        self.player = player
        self.enemy = enemy
        self.active = True

    def update(self, terminal: PyTerminal):
        print(f"\nBATTLE: {self.enemy.name}")
        print(f"Player HP: {self.player.hp} | Enemy HP: {self.enemy.hp}")

        action = terminal.get_input("Choose (attack / heal): ").lower().strip()

        if action == "attack":
            dmg = random.randint(8, self.player.attack)
            self.enemy.hp -= dmg
            print(f"You hit {self.enemy.name} for {dmg} damage.")
        elif action == "heal":
            heal = random.randint(5, 10)
            self.player.hp += heal
            print(f"You heal for {heal} HP.")
        else:
            print("You hesitate.")

        if self.enemy.hp <= 0:
            print(f"You defeated {self.enemy.name}.")
            self.active = False
            return

        dmg = random.randint(5, self.enemy.attack)
        self.player.hp -= dmg
        print(f"{self.enemy.name} hits you for {dmg} damage.")

        if self.player.hp <= 0:
            print("You were defeated...")
            self.active = False
