class Utils:
    @staticmethod
    def ask_integer(message, min_val=None, max_val=None):
        while True:
            try:
                choice = int(input(message))
                if min_val is not None and choice < min_val:
                    print(f"Please choose a number >= {min_val}.")
                    continue
                if max_val is not None and choice > max_val:
                    print(f"Please choose a number <= {max_val}.")
                    continue
                return choice
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    @staticmethod
    def ask_yes_no(message):
        while True:
            response = input(message).strip().lower()
            if response in ["y", "yes", "sim", "s"]:
                return True
            elif response in ["n", "no", "nao"]:
                return False
            print("Invalid input. Please type 'y' or 'n'.")

    @staticmethod
    def choose_pokemon_from_list(pokemon_list, message="\nChoose a Pokemon:"):
        if not pokemon_list:
            print("No Pokemon available.")
            return None

        print(message)
        for i, p in enumerate(pokemon_list):
            print(f"{i + 1}. {p.name} (HP: {p.hp}/{p.hp_max})")

        choice = Utils.ask_integer(
            "Enter the number of your choice: ", min_val=1, max_val=len(pokemon_list)
        )
        return pokemon_list[choice - 1]
