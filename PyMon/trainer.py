import random
from utils import Utils


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def __str__(self):
        return f"Trainer {self.name} with Pokemon: {[p.name for p in self.pokemon]}"

    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)

    def choose_pokemon(self):
        return Utils.choose_pokemon_from_list(self.pokemon)

    def catch_pokemon(self, pokemon):
        if len(self.pokemon) < 6:
            self.pokemon.append(pokemon)
            print(f"{self.name} caught {pokemon.name}!")
        else:
            print("You can't catch more than 6 Pokemon!")
            if Utils.ask_yes_no(
                "Do you want to release a Pokemon to catch the new one? (y/n): "
            ):
                released_pokemon = Utils.choose_pokemon_from_list(self.pokemon)
                self.pokemon.remove(released_pokemon)
                self.pokemon.append(pokemon)
                print(
                    f"{self.name} released {released_pokemon.name} to catch {pokemon.name}!"
                )

    def release_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            self.pokemon.remove(pokemon)
            print(f"{self.name} released {pokemon.name}.")
        else:
            print(f"{pokemon.name} is not in {self.name}'s team.")

    def get_random_pokemon(self):
        return random.choice(self.pokemon)

    def heal_pokemon(self):
        for p in self.pokemon:
            p.heal()

    def train_pokemon(self):
        for p in self.pokemon:
            p.train()

    def check_team(self):
        print(f"{self.name}'s team:")
        for p in self.pokemon:
            print(f"{p.name}, type: {p.type} (HP: {p.hp}/{p.hp_max})")
