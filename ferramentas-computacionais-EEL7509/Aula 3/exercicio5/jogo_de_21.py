import random


class Carta:
    def __init__(self, valor, naipe):
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        naipes = ["Paus", "Ouros", "Copas", "Espadas"]
        if valor in valores:
            self.valor = valor
        else:
            raise ValueError("Valor inválido")
        if naipe in naipes:
            self.naipe = naipe
        else:
            raise ValueError("Naipe inválido")

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

    def __repr__(self):
        return self.__str__()


class BaralhoDeCartas:
    def __init__(self):
        self.naipes = ["Copas", "Espadas", "Ouros", "Paus"]
        self.valores = ["A"] + list(map(str, range(2, 11))) + ["J", "Q", "K"]
        self.baralho = [
            Carta(valor, naipe) for naipe in self.naipes for valor in self.valores
        ]
        self.embaralhar()

    def __repr__(self):
        return f"{self.baralho}"

    def embaralhar(self):
        random.shuffle(self.baralho)

    def sortear_carta(self):
        if not self.baralho:
            raise ValueError("Não há mais cartas no baralho")
        return self.baralho.pop()

    def contar_cartas(self):
        return len(self.baralho)


class Jogador21(BaralhoDeCartas):
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []
        self.pontos = 0
        self.estourou = False

    def sortear_carta(self, baralho):
        carta = baralho.sortear_carta()
        self.cartas.append(carta)
        self.somar_pontos()

    def somar_pontos(self):
        self.pontos = 0
        for carta in self.cartas:
            if carta.valor in ["J", "Q", "K"]:
                self.pontos += 10
            elif carta.valor == "A":
                self.pontos += 11 if self.pontos + 11 <= 21 else 1
            else:
                self.pontos += int(carta.valor)

    def rodada(self, baralho):
        while self.continuar():
            self.sortear_carta(baralho)
            self.checar_cartas()
            if self.estourou:
                break

    def checar_cartas(self):
        if self.pontos > 21:
            print(f"{self.nome} estourou com {self.pontos} pontos!")
            self.estourou = True
        else:
            print(f"{self.nome} tem as cartas{self.cartas}, e {self.pontos} pontos.")

    def __str__(self):
        return f"{self.nome} tem {self.pontos} pontos com as cartas {', '.join(map(str, self.cartas))}"

    def continuar(self):
        return input(f"{self.nome}, deseja continuar? (s/n) ") == "s"

    def limpar_mao(self):
        self.cartas = []
        self.pontos = 0
        self.estourou = False


class Mesa(Jogador21):
    def __init__(self):
        super().__init__("Mesa")

    def continuar(self):
        return self.pontos < 17


def JogoDe21():
    baralho = BaralhoDeCartas()
    mesa = Mesa()
    jogador_1 = Jogador21("Jogador 1")

    print("Bem-vindo ao jogo de 21!")

    while True:
        status = input("Deseja um jogo? (s/n) ")
        jogador_1.limpar_mao()
        mesa.limpar_mao()

        if status != "s":
            print("Até a próxima!")
            break

        while True:
            jogador_1.rodada(baralho)
            if jogador_1.estourou:
                print("Mesa venceu!")
                break

            mesa.rodada(baralho)

            if mesa.pontos > 21 or jogador_1.pontos > mesa.pontos:
                print("Jogador 1 venceu!")
                break
            else:
                print("Mesa venceu!")
                break


if __name__ == "__main__":
    JogoDe21()
