class Player:
    #constructor
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack

    #assesseurs
    def get_pseudo(self):
        return self.pseudo

    def set_pseudo(self, pseudo):
        self.pseudo = pseudo
        return self

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health
        return self

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack
        return self

    #specific methods
    def display_player_info(self):
        print(f"Nom du joueur : {self.pseudo}")
        print(f"Points de vie  : {self.health}")
        print(f"Puissance d'attaque : {self.attack}")


player1 = Player("Misterbear", 25, 3)
player1.display_player_info()


