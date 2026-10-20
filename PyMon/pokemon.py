from typing import override

SUPER_EFFECTIVE = 2.0
NOT_VERY_EFFECTIVE = 0.5
NORMAL_EFFECTIVE = 1.0

class Pokemon:
    def __init__(self, name, type, hp, hp_max, attack):
        self.name = name
        self.type = type
        self.hp = hp
        self.hp_max = hp_max
        self.attack = attack

    def __str__(self):
        return f"{self.name} (Type: {self.type}, HP: {self.hp}/{self.hp_max}, Attack: {self.attack})"

    def attack_pokemon(self, other):
        multiplier = self.get_type_multiplier(other.type)
        damage = int(self.attack * multiplier)

        if multiplier > 1:
            print(f"{self.name} it's super effective against {other.name}!")
        elif multiplier < 1:
            print(f"{self.name} it's not very effective against {other.name}.")

        other.hp = max(0, other.hp - damage)
        print(
            f"{self.name} attacks {other.name} for {damage} damage! {other.name} has {other.hp}/{other.hp_max} HP left."
        )

    def get_type_multiplier(self, other):
        return 1.0

    def heal(self):
        self.hp = self.hp_max
        print(
            f"{self.name} is fully healed! {self.name} has {self.hp}/{self.hp_max} HP now."
        )

    def train(self):
        self.attack += 10
        print(f"{self.name} has trained and increased its attack to {self.attack}!")

    def is_alive(self):
        return self.hp > 0


class FirePokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Fire", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Grass":
            return SUPER_EFFECTIVE
        if other_type == "Water":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class WaterPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Water", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Fire":
            return SUPER_EFFECTIVE
        if other_type == "Grass":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class GrassPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Grass", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Water":
            return SUPER_EFFECTIVE
        if other_type == "Fire":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class ElectricPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Electric", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Water":
            return SUPER_EFFECTIVE
        if other_type == "Grass":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class FlyingPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Flying", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Fighting":
            return SUPER_EFFECTIVE
        if other_type == "Rock":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class GhostPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Ghost", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Psychic":
            return SUPER_EFFECTIVE
        if other_type == "Ghost":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class FightingPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Fighting", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Normal":
            return SUPER_EFFECTIVE
        if other_type == "Flying":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class RockPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Rock", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Flying":
            return SUPER_EFFECTIVE
        if other_type == "Fighting":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class PsychicPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Psychic", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Fighting":
            return SUPER_EFFECTIVE
        if other_type == "Ghost":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE


class PoisonPokemon(Pokemon):
    def __init__(self, name, hp, hp_max, attack):
        super().__init__(name, "Poison", hp, hp_max, attack)

    @override
    def get_type_multiplier(self, other_type):
        if other_type == "Grass":
            return SUPER_EFFECTIVE
        if other_type == "Ground":
            return NOT_VERY_EFFECTIVE
        return NORMAL_EFFECTIVE
