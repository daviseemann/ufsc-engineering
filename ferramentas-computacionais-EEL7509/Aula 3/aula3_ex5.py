# Exercício 5: Crie uma classe Jogador21 que permita gerar instâncias de
# jogadores de 21. Os objetos de tal classe deverão ter capacidade de armazenar o
# nome do jogador, armazenar as cartas sorteadas, calcular o total de pontos,
# além de perguntar para o usuário se ele deseja continuar ou não o sorteio de
# cartas.

from aula3_ex3 import BaralhoDeCartas


class Jogador21(BaralhoDeCartas):
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []
        self.pontos = 0

    def sortear_carta(self, baralho):
        carta = baralho.sortear_carta()
        self.cartas.append(carta)

    def somar_pontos(self):
        self.pontos = 0
        for carta in self.cartas:
            if carta.valor in ["J", "Q", "K"]:
                self.pontos += 10
            elif carta.valor == "A":
                if self.pontos + 11 > 21:
                    self.pontos += 1
                else:
                    self.pontos += 11
            else:
                self.pontos += int(carta.valor)

    def rodada(self, baralho):
        while self.continuar():
            self.sortear_carta(baralho)
            self.somar_pontos()
            self.checar_cartas()

    def checar_cartas(self):
        if self.pontos > 21:
            print(f"{self.nome} estourou com {self.pontos} pontos!")
        else:
            print(f"{self.nome} tem {self.pontos} pontos.")

    def __str__(self):
        return f"{self.nome} tem {self.pontos} pontos com as cartas {', '.join(map(str, self.cartas))}"

    def continuar(self):
        return input("Deseja continuar? (s/n) ") == "s"


class Mesa(Jogador21):
    def __init__(self):
        super().__init__("Mesa")

    def continuar(self):
        return True if self.pontos < 17 else False
