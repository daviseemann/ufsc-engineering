# Exercício 3: Crie uma classe BaralhoDeCartas que administre o sorteio de
# cartas para fins de implementação de um jogo de baralho. Tal classe deverá
# armazenar cartas criadas a partir da classe Carta definida anteriormente e,
# além disso, possuir um método que, ao ser chamado, retorne uma carta
# sorteada aleatoriamente e remova tal carta do baralho.

from aula3_ex4 import Carta

import random


class BaralhoDeCartas(Carta):
    def __init__(self):
        self.naipes = ["Copas", "Espadas", "Ouros", "Paus"]
        self.valores = ["A"] + list(range(2, 11)) + ["J", "Q", "K"]
        self.baralho = [
            Carta(naipe, valor) for naipe in self.naipes for valor in self.valores
        ]

    def __repr__(self):
        return f"{self.baralho}"

    def embaralhar(self):
        random.shuffle(self.baralho)

    def sortear_carta(self):
        carta = random.choice(self.baralho)
        self.baralho.remove(carta)
        return carta

    def sortear_cartas(self, n):
        cartas = []
        for _ in range(n):
            carta = self.sortear_carta()
            cartas.append(carta)
        return cartas

    def contar_cartas(self):
        len_cartas = len(self.baralho)
        return print(f"Quantidade de cartas no baralho: {len_cartas}")

    def truco(self):
        print("Vamos jogar truco!")
        jogadores = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4"]
        for jogador in jogadores:
            print(f"{self.sortear_cartas(3)} para o {jogador}")
