class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack

    def display_player_info(self):
        print(f"Nom du joueur : {self.pseudo}")
        print(f"Points de vie  : {self.health}")
        print(f"Puissance d'attaque : {self.attack}")


player1 = Player("Misterbear", 25, 3)
player1.display_player_info()


