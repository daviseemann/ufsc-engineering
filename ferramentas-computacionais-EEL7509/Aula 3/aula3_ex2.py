# Exercício 2: Escreva o código correspondente a uma classe chamada Carta
# que represente uma carta de baralho com suas propriedades principais.
class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __repr__(self):
        return f"{self.valor} de {self.naipe}"
