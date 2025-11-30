from model.player import Player, Warrior
from model.weapon import Weapon

player1 = Player("Misterbear", 25, 3)
player2 = Player("Silence", 20, 4)
knife = Weapon("Couteau", 5)
player2.set_weapon(knife)
player1.attack_player(player2)
player2.attack_player(player1)
warrior = Warrior("Conan", 20, 5)
player2.attack_player(warrior)
warrior.display_player_info()


