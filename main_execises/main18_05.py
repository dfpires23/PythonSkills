# INÍCIO DO CÓDIGO ORIENTADO A OBJETOS
from typing import override


class Main:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


if __name__ == "__main__":
    main = Main("World")
    print(main.greet())


class Mamífero:
    # __init__ É O CONSTRUTOR DA CLASSE, ELE É CHAMADO QUANDO UM OBJETO É CRIADO
    def __init__(self, cor, peso, idade, energia=100, distancia_percorrida=0):
        self.cor = cor
        self.peso = peso
        self.idade = idade
        self.energia = energia
        self.distancia_percorrida = distancia_percorrida

    def respirar(self):
        return "Respirando..."

    def comer(self):
        return "Comendo..."

    def dormir(self):
        return "Dormindo..."

    def mover(self):
        self.energia -= 5
        self.distancia_percorrida += 10
        return "Movendo-se..."


class Cachorro(Mamífero):
    def __init__(self, cor, peso, idade, raca):
        super().__init__(cor, peso, idade)
        self.raca = raca

    def latir(self):
        return "Au au!"


class Gato(Mamífero):
    def __init__(self, cor, peso, idade, raca):
        super().__init__(cor, peso, idade)
        self.raca = raca

    def miar(self):
        return "Miau!"


class Cavalo(Mamífero):
    def __init__(self, cor, peso, idade, raca):
        super().__init__(cor, peso, idade)
        self.raca = raca
        # USO DE ENCAPSULAMENTO PARA PROTEGER O ATRIBUTO ENERGIA, QUE É USADO PARA CONTROLAR A ENERGIA DO CAVALO, E GARANTIR QUE ELE NÃO FIQUE COM ENERGIA NEGATIVA, E QUE ELE DURMA QUANDO FICAR EXAUSTO
        self.__energia = self.energia

    def get_energia(self):
        return self.__energia
    
    def set_energia(self, energia):
        self.__energia = energia
        self.energia = energia

    def relinchar(self):
        return "Hiii!"
    
    @override
    def mover(self):
        while self.__energia > 20:
            self.__energia -= 10
            self.energia = self.__energia
            self.distancia_percorrida += 20
            return "O cavalo está correndo!"
        self.dormir()
        return "O cavalo está exausto!"
    
    @override
    def dormir(self):
        self.__energia += 40
        self.energia = self.__energia
        return "O cavalo está descansando..."


if __name__ == "__main__":
    meu_cao = Cachorro("Preto", 20, 5, "Labrador")
    print(meu_cao.latir())
    meu_gato = Gato("Branco", 10, 3, "Siamês")
    print(meu_gato.miar())
    meu_cavalo = Cavalo("Cinza", 500, 10, "Quarter Horse")
    print(meu_cavalo.relinchar())

    print("\nMovendo os animais...\n")

    for _ in range(10):
        meu_cao.mover()
        meu_gato.mover()
        meu_cavalo.mover()

    print(f"Cão - Energia: {meu_cao.energia}, Distância Percorrida: {meu_cao.distancia_percorrida}")
    print(f"Gato - Energia: {meu_gato.energia}, Distância Percorrida: {meu_gato.distancia_percorrida}")
    print(f"Cavalo - Energia: {meu_cavalo.energia}, Distância Percorrida: {meu_cavalo.distancia_percorrida}")

    def menu():
        print("\n=== MENU ===")
        print("1. Verificar energia do cavalo")
        print("2. Definir energia do cavalo")
        print("3. Galopar o cavalo")
        print("4. Descansar o cavalo")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
        return escolha

    # === EXERCÍCIOS ===
    menu_opcao = menu()
    while menu_opcao != "0":
        if menu_opcao == "1":
            print(f"Energia do cavalo: {meu_cavalo.get_energia()}")
        elif menu_opcao == "2":
            nova_energia = int(input("Digite a nova energia para o cavalo: "))
            meu_cavalo.set_energia(nova_energia)
            print("Energia do cavalo atualizada.")
        elif menu_opcao == "3":
            print(meu_cavalo.mover())
        elif menu_opcao == "4":
            print(meu_cavalo.dormir())
        else:
            print("Opção inválida. Tente novamente.")
        
        menu_opcao = menu()
