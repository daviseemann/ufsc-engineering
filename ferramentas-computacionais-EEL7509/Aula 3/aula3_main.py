from aula3_ex5 import Jogador21, Mesa
from aula3_ex3 import BaralhoDeCartas


def JogoDe21():
    baralho = BaralhoDeCartas()
    mesa = Mesa()
    jogador_1 = Jogador21("Jogador 1")
    jogando = True

    print("Bem-vindo ao jogo de 21!")

    while jogando:
        jogador_1.rodada(baralho)
        mesa.rodada(baralho)
        jogando = jogador_1.continuar() or mesa.continuar()

    if jogador_1.pontos <= mesa.pontos:
        print("Mesa venceu!")
    else:
        print("Jogador 1 venceu!")


if __name__ == "__main__":
    JogoDe21()
