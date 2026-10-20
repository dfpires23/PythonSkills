class Battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2

    def battle(self):
        pokemon1 = self.trainer1.choose_pokemon()
        pokemon2 = self.trainer2.get_random_pokemon()
        print(f"{self.trainer1.name} chose {pokemon1.name}!")
        print(f"{self.trainer2.name} chose {pokemon2.name}!")
        while pokemon1.is_alive() and pokemon2.is_alive():
            pokemon1.attack_pokemon(pokemon2)
            if pokemon2.is_alive():
                pokemon2.attack_pokemon(pokemon1)
        if pokemon1.is_alive():
            print(f"{self.trainer1.name} wins the battle!")
        else:
            print(f"{self.trainer2.name} wins the battle!")
