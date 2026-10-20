import random

from battle import Battle
from pokemon import (
    ElectricPokemon,
    FightingPokemon,
    FirePokemon,
    FlyingPokemon,
    GhostPokemon,
    GrassPokemon,
    PoisonPokemon,
    PsychicPokemon,
    RockPokemon,
    WaterPokemon,
)
from trainer import Trainer
from utils import Utils

if __name__ == "__main__":
    # Create initial Pokemon instances
    pikachu = ElectricPokemon("Pikachu", 35, 35, 55)
    charmander = FirePokemon("Charmander", 39, 39, 52)
    bulbasaur = GrassPokemon("Bulbasaur", 45, 45, 49)
    squirtle = WaterPokemon("Squirtle", 44, 44, 48)

    # Create more Pokemon instances
    pidgeot = FlyingPokemon("Pidgeot", 83, 83, 80)
    arcanine = FirePokemon("Arcanine", 90, 90, 110)
    lapras = WaterPokemon("Lapras", 130, 130, 85)
    dragonite = FlyingPokemon("Dragonite", 91, 91, 134)
    gengar = GhostPokemon("Gengar", 60, 60, 65)
    machamp = FightingPokemon("Machamp", 90, 90, 130)
    golem = RockPokemon("Golem", 80, 80, 120)
    alakazam = PsychicPokemon("Alakazam", 55, 55, 50)
    arbok = PoisonPokemon("Arbok", 60, 60, 85)

    initial_pokemon_pool = [pikachu, charmander, bulbasaur, squirtle]
    wild_pokemon_pool = [
        pidgeot,
        arcanine,
        lapras,
        dragonite,
        gengar,
        machamp,
        golem,
        alakazam,
        arbok,
    ]

    # Create trainers and add Pokemon to their teams
    misty = Trainer("Misty")
    misty.add_pokemon(squirtle)
    brock = Trainer("Brock")
    brock.add_pokemon(golem)
    trace = Trainer("Trace")
    trace.add_pokemon(pidgeot)

    # === Trainer and Game Logic ===
    # Welcome message
    print("\nWelcome to the Pokemon Game!")

    # Create a trainer and add Pokemon to their team
    trainer_name = input("Enter your trainer name: ")
    player = Trainer(trainer_name)
    player_pokemon = Utils.choose_pokemon_from_list(
        initial_pokemon_pool, "Choose your starter Pokemon:"
    )
    player.add_pokemon(player_pokemon)
    print(f"You chose {player_pokemon.name}!")

    # Menu for user interaction
    while True:
        print("\nWhat would you like to do?")
        print("1. Search for Pokemon")
        print("2. Battle a trainer")
        print("3. Train your Pokemon")
        print("4. Heal")
        print("5. Check your team")
        print("0. Exit")
        action = Utils.ask_integer("Enter your choice: ", 0, 5)
        if action == 1:
            print("You found a wild Pokemon!")
            wild_pokemon = random.choice(wild_pokemon_pool)
            print(f"A wild {wild_pokemon.name} appeared!")
            print(wild_pokemon)
            if Utils.ask_yes_no("Do you want to try to catch it? (y/n): "):
                player.catch_pokemon(wild_pokemon)
            else:
                print("You decided not to catch the Pokemon.")
        elif action == 2:
            print("You encountered a trainer!")
            opponent = random.choice([misty, brock, trace])
            print(f"You are battling {opponent.name}!")
            battle = Battle(player, opponent)
            battle.battle()
        elif action == 3:
            player.train_pokemon()
        elif action == 4:
            player.heal_pokemon()
        elif action == 5:
            player.check_team()
        elif action == 0:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
