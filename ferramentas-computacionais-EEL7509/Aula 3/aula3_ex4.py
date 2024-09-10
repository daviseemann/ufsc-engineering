# Exercício 4: Modifique sua classe Carta criada anteriormente, adicionando
# um mecanismo, baseado em execeções, para verificar se o valor e o naipe da
# carta são válidos. A exceção gerada pode ser genérica:
# (raise Exception("Mensagem de erro")).


class Carta:
    def __init__(self, valor, naipe):
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        naipes = ["Paus", "Ouros", "Copas", "Espadas"]
        if valor in valores:
            self.valor = valor
        else:
            raise Exception("Valor inválido")
        if naipe in naipes:
            self.naipe = naipe
        else:
            raise Exception("Naipe inválido")

    def __str__(self):
        return f"{self.valor} de {self.naipe}"
