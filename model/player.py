class Player:
    #constructor
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None

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

    def set_weapon(self, weapon):
        self.weapon = weapon

    #specific methods
    def display_player_info(self):
        print(f"Nom du joueur : {self.get_pseudo()}")
        print(f"Points de vie  : {self.get_health()}")
        print(f"Puissance d'attaque : {self.get_attack()}")

    def damage_player(self, damage):
        if damage>=self.health:
            self.health = 0
            print(f"{self.pseudo} est hors combat!")
        elif damage <= 0:
            print(f"{self.pseudo} est indemne")
        else :
            self.health -= damage
            print(f"{self.pseudo} est blessé, point de vie : {self.health}")

    def attack_player(self, target_player):
        if self.weapon :
            attack_power = self.attack + self.weapon.get_damage_amount()
        else :
            attack_power = self.attack
        print(f"{self.pseudo} attaque {target_player.get_pseudo()}")
        target_player.damage_player(attack_power)

class Warrior(Player):

    def __init__(self, pseudo, health, attack, armor = 3):
        super().__init__(pseudo, health, attack)
        self.armor = armor

    def get_armor(self):
        return self.armor

    def display_player_info(self):
        print(f"Classe : guerrier")
        super().display_player_info()
        print(f"Armure : {self.get_armor()}")

    def damage_player(self, damage):
        if self.armor > 0 :
            self.armor -= 1
            damage=0
            print(f"L'armure de {self.pseudo} bloque l'attaque")
        super().damage_player(damage)

    def repare(self, power=2):
        self.armor += power